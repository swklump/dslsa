from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QFileDialog, QVBoxLayout, QMainWindow, QApplication, QListWidgetItem
# from PyQt5.QtCore import QUrl, pyqtSignal, Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView

import os, sys, shutil, folium, io, markupsafe, requests
import pandas as pd
from config import folder
from functions.windowdefaults import window_defaults
from zipfile import ZipFile
from getplacemarkers import get_placemarkers
from folium.plugins.marker_cluster import MarkerCluster
from folium.plugins.fast_marker_cluster import FastMarkerCluster


from ui_main import Ui_appmainwindow


appname = 'DOWL Soils Library Search App'
icon_path = 'png/icon.ico'

# GLOBAL VARS
reports, resultsDialogSuccess = '', ''
projnumber, project, county, area, city = 'None selected...','None selected...','None selected...','None selected...','None selected...'
searchprojnumbervar, searchprojectvar,searchcountyvar, searchcityvar = '','','',''
df_placemarks = pd.DataFrame({'id':['test'],'lat':[61.165622],'lon':[-149.930321]})
authorizedcredentials = {'sklump':'dowluser'}
# df_counties = pd.read_csv('https://www2.census.gov/geo/docs/reference/codes/files/national_county.txt')
adminvalidated = False

dict_loc = {'Alaska':[64.200841,-149.493673]}
selectedstate = 'Alaska'

class Master():

    def backto_mainmenu(self):
        self.close()
        ControlMainWindow().show()


# DIALOG BOXES ------------------------------------------------------------------------------------------
class ResultsDialogSuccess(QDialog, Master):
    def __init__(self):
        super(ResultsDialogSuccess, self).__init__()
        self.ui = uic.loadUi('ui/resultsdialog_success.ui', self)
        window_defaults(self, appname, icon_path)

        self.btn_mainmenu.clicked.connect(self.backto_mainmenu)
        self.btn_submit.setDefault(True)

class ResultsDialogFailure(QDialog, Master):
    def __init__(self):
        super(ResultsDialogFailure, self).__init__()
        self.ui = uic.loadUi('ui/resultsdialog_failure.ui', self)
        window_defaults(self, appname, icon_path)

        self.btn_mainmenu.clicked.connect(self.backto_mainmenu)

class ResultsDialogAfterOpen(QDialog, Master):
    def __init__(self):
        super(ResultsDialogAfterOpen, self).__init__()
        self.ui = uic.loadUi('ui/resultsdialog_afteropen.ui', self)
        window_defaults(self, appname, icon_path)

        self.btn_mainmenu.clicked.connect(self.backto_mainmenu)



# MAIN WINDOW ---------------------------------------------------------------------------------------------------------
class ControlMainWindow(QMainWindow, Master):

    def __init__(self):
        super(ControlMainWindow, self).__init__()
        self.ui = Ui_appmainwindow()
        self.ui.setupUi(self)

        window_defaults(self, appname, icon_path)

        self.df = pd.read_excel('SoilsReportRecord.xls')
        for x in ['Project Name','Area','CITY']:
            self.df[x] = self.df[x].str.title()

        global projnumber, project, county, city, adminvalidated, selectedstate, dict_placemarkers
        dict_dropdown = {self.ui.list_projnumber:[projnumber,'W.O. #'], self.ui.list_project:[project,'Project Name'], self.ui.list_city:[city,'CITY']}

        # add options to combo box from excel file
        for k,v in dict_dropdown.items():
            combolist = list(self.df[v[1]].unique())
            combolist = sorted([str(item) for item in combolist if not(pd.isnull(str(item))) == True])
            for x in combolist:
                k.addItem(x)

        self.ui.line_searchprojnumber.setText(searchprojnumbervar)
        self.ui.line_searchproject.setText(searchprojectvar)
        # self.ui.line_searcharea.setText(searchareavar)
        self.ui.line_searchcity.setText(searchcityvar)
        
        # add map
        self.m = folium.Map(
        	tiles='openstreetmap',
        	zoom_start=4,
        	location=(dict_loc[selectedstate][0], dict_loc[selectedstate][1])
        )
        for i in range(len(df_placemarks)):
            folium.Marker(location=[df_placemarks['lat'].iloc[i],df_placemarks['lon'].iloc[i]],popup=df_placemarks['id'].iloc[i]).add_to(self.m)
        data = io.BytesIO()
        self.m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        self.ui.verticalLayout.addWidget(webView)

        # self.ui.list_client.setCurrentItem(QListWidgetItem('Adot&Pf'))
        # Set previous selections
        # for k, v in dict_dropdown.items():
        #     k.setCurrentText(v[0])

        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(0))
        self.ui.btn_about.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(1))
        self.ui.btn_admin.clicked.connect(lambda adminvalidated: self.ui.stackedWidget_2.setCurrentIndex(2) if adminvalidated == False else self.ui.stackedWidget_2.setCurrentIndex(3))

        self.ui.btn_search.setDefault(True)
        self.ui.btn_search.clicked.connect(self.get_results)
        self.ui.btn_reset.clicked.connect(self.reset)

        self.ui.btn_searchprojnumber.clicked.connect(self.filter_projnumber_list)
        self.ui.btn_searchproject.clicked.connect(self.filter_project_list)
        # self.ui.btn_searcharea.clicked.connect(self.filter_area_list)
        self.ui.btn_searchcity.clicked.connect(self.filter_city_list)
        self.ui.btn_adminsubmit.clicked.connect(self.submitcredentials)
        self.ui.btn_submitexcelpath.clicked.connect(self.changeexcelpath)

        self.ui.list_city.itemClicked.connect(self.showmarkers)
    
    def showmarkers(self):
        global df_placemarks
        selectedcity = self.ui.list_city.selectedItems()[0].text()
        df_placemarks = get_placemarkers(selectedcity)

        # reinitialize map
        self.m = folium.Map(
        	tiles='openstreetmap',
        )
        sw = df_placemarks[['lat', 'lon']].min().values.tolist()
        ne = df_placemarks[['lat', 'lon']].max().values.tolist()  
        self.m.fit_bounds([sw, ne]) 

        # add points to cluster
        # might have to make the popup div simpler to render Anchorage
        callback = """\
        function (row) {
            var marker;
            marker = L.marker(new L.LatLng(row[0], row[1]), {color:'blue'});
            
            var popup = L.popup();
            const display_text = {text1: row[3], text2: row[4]};
            var mytext = $(`

                <div>
                Project Name: ${display_text.text1} </br>
                File: ${display_text.text2}
                </div>

            `)[0];
            popup.setContent(mytext);
            marker.bindPopup(popup);
            
            return marker;
        };"""
        FastMarkerCluster(df_placemarks[['lat', 'lon','id','projectname','file']].values.tolist(), callback=callback).add_to(self.m)

        # save changes to map
        data = io.BytesIO()
        self.m.save(data, close_file=False)
        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        for i in reversed(range(self.ui.verticalLayout.count())): 
            self.ui.verticalLayout.itemAt(i).widget().setParent(None)
        self.ui.verticalLayout.addWidget(webView)


    def changeexcelpath(self):

        excelpath = self.ui.line_excelpath.text()
        excelname = self.ui.line_excelname.text()
        if excelname[-4:] == '.xls':
            pass
        else:
            excelname = excelname + '.xls'
        try:
            df_test = pd.read_excel(excelpath + '/' + excelname)
        except FileNotFoundError:
            self.ui.label_excelmessage.setText('Path and file name not found! Please try again.')
            self.ui.label_excelmessage.setStyleSheet('color: red;')
        else:
            self.ui.label_excelmessage.setText('Path and file name have been updated!')
            self.ui.label_excelmessage.setStyleSheet('color: green;')

    def submitcredentials(self):
        global adminvalidated

        user = self.ui.line_user.text()
        password = self.ui.line_pass.text()
        if user in authorizedcredentials:
            if password == authorizedcredentials[user]:
                adminvalidated = True
                self.ui.lab_invalidcreds.setText('')
                self.ui.stackedWidget_2.setCurrentIndex(3)
                self.ui.lab_welcome.setText(f'Welcome {user}! This is the admin dashboard.')
                
                
                # get files in source folder
                pdffiles = os.listdir(folder)
                reports_notinforlder = [str(x) for x in df['Report#'].values.tolist() if str(x).lstrip('0')+'.pdf' not in pdffiles]
                message = ''
                for x in reports_notinforlder:
                    message = message + x + '\n'
                self.ui.text_reportsnotinfolder.setText(message)
                self.ui.text_reportsnotinfolder.setReadOnly(True)

            else:
                self.ui.lab_invalidcreds.setText('The password is not correct. Please try again.')
        else:
            self.ui.lab_invalidcreds.setText('The username is not correct. Please try again.')


# FILTER FUNCTIONS--------------------------------------------
    def filter_projnumber_list(self):
        global searchprojnumbervar
        searchinput = self.ui.line_searchprojnumber.text()
        searchprojnumbervar = searchinput
        
        # if search is blank, load all options
        if searchinput == '':
            combolist = list(df['W.O. #'].unique())
            combolist = sorted([str(item) for item in combolist if not(pd.isnull(str(item))) == True])
            self.ui.list_projnumber.clear()
            self.ui.list_projnumber.addItems(combolist)
        
        # else get list of items with search input contained
        else:
            matching_results = []
            for x in df['W.O. #'].values.tolist():
                if str(searchinput).lower() in str(x).lower():
                    matching_results.append(x)
            matching_results = sorted(set(matching_results))
            self.ui.list_projnumber.clear()
            for x in matching_results:
                self.ui.list_projnumber.addItem(x)
        
    def filter_project_list(self):
        global searchprojectvar
        searchinput = self.ui.line_searchproject.text()
        searchprojectvar = searchinput

        
        # if search is blank, load all options
        if searchinput == '':
            combolist = list(df['Project Name'].unique())
            combolist = sorted([str(item) for item in combolist if not(pd.isnull(str(item))) == True])
            self.ui.list_project.clear()
            self.ui.list_project.addItems(combolist)
        
        # else get list of items with search input contained
        else:
            matching_results = []
            for x in df['Project Name'].values.tolist():
                if str(searchinput).lower() in str(x).lower():
                    matching_results.append(x)
            matching_results = sorted(set(matching_results))
            self.ui.list_project.clear()
            for x in matching_results:
                self.ui.list_project.addItem(x)
        
    # def filter_area_list(self):
    #     global searchareavar
    #     searchinput = self.ui.line_searcharea.text()
    #     searchareavar = searchinput

        
    #     # if search is blank, load all options
    #     if searchinput == '':
    #         combolist = list(df['Area'].unique())
    #         combolist = sorted([item for item in combolist if not(pd.isnull(item)) == True])
    #         self.ui.list_area.clear()
    #         self.ui.list_area.addItems(combolist)
        
    #     # else get list of items with search input contained
    #     else:
    #         matching_results = []
    #         for x in df['Area'].values.tolist():
    #             if str(searchinput).lower() in str(x).lower():
    #                 matching_results.append(x)
    #         matching_results = sorted(set(matching_results))
    #         self.ui.list_area.clear()
    #         for x in matching_results:
    #             self.ui.list_area.addItem(x)
        
    def filter_city_list(self):
        global searchcityvar
        searchinput = self.ui.line_searchcity.text()
        searchcityvar = searchinput

        
        # if search is blank, load all options
        if searchinput == '':
            combolist = list(self.df['CITY'].unique())
            combolist = sorted([str(item) for item in combolist if not(pd.isnull(str(item))) == True])
            self.ui.list_city.clear()
            self.ui.list_city.addItems(combolist)
        
        # else get list of items with search input contained
        else:
            matching_results = []
            for x in self.df['CITY'].values.tolist():
                if str(searchinput).lower() in str(x).lower():
                    matching_results.append(x)
            matching_results = sorted(set(matching_results))
            self.ui.list_city.clear()
            for x in matching_results:
                self.ui.list_city.addItem(x)

    def reset(self):
        self.ui.line_searchclient.setText('')
        self.ui.line_searchproject.setText('')
        self.ui.line_searcharea.setText('')
        self.ui.line_searchcity.setText('')

        combolist = list(df['W.O. #'].unique())
        combolist = sorted([item for item in combolist if not(pd.isnull(item)) == True])
        self.ui.list_client.clear()
        self.ui.list_client.addItems(combolist)

        combolist = list(df['Project Name'].unique())
        combolist = sorted([item for item in combolist if not(pd.isnull(item)) == True])
        self.ui.list_project.clear()
        self.ui.list_project.addItems(combolist)

        combolist = list(df['Area'].unique())
        combolist = sorted([item for item in combolist if not(pd.isnull(item)) == True])
        self.ui.list_area.clear()
        self.ui.list_area.addItems(combolist)

        combolist = list(df['CITY'].unique())
        combolist = sorted([item for item in combolist if not(pd.isnull(item)) == True])
        self.ui.list_city.clear()
        self.ui.list_city.addItems(combolist)


# RESULTS DIALOG FUNCTIONS-------------------------------------------
    def get_results(self):
        global reports, projnumber, project, area, city

        projnumber = self.ui.list_projnumber.selectedItems()
        project = self.ui.list_project.selectedItems()
        # area = self.ui.list_area.selectedItems()
        city = self.ui.list_city.selectedItems()

        # apply selected filters
        results = self.df
        search_dict = {'W.O. #':projnumber, 'Project Name':project, 
        # 'Area':area, 
        'CITY':city}
        for k,v in search_dict.items():
            if v:
                results = results[results[k]==v[0].text()]

        reports = results['Report#'].values.tolist()

        if not reports:
            self.showResultsDialogFailure()
        else:
            self.showResultsDialogSuccess()

    def showResultsDialogFailure(self):
        resultsDialogFailure = ResultsDialogFailure()
        resultsDialogFailure.show()
        self.close()
    
    def showResultsDialogSuccess(self):
        global reports, resultsDialogSuccess
        resultsDialogSuccess = ResultsDialogSuccess()
        resultsDialogSuccess.show()
        self.close()

        if len(reports) > 1:
            resultsDialogSuccess.label.setText(f'There were {len(reports)} results found!')
        else:
            resultsDialogSuccess.label.setText(f'There was {len(reports)} result found!')

        resultsDialogSuccess.label.setStyleSheet('color: green;')
        resultsDialogSuccess.btn_submit.setDefault(True)
        resultsDialogSuccess.btn_submit.clicked.connect(self.viewresults)
  
    def viewresults(self):
        global reports, resultsDialogSuccess
        resultsDialogAfterOpen = ResultsDialogAfterOpen()
        resultsDialogAfterOpen.show()
        results_option = resultsDialogSuccess.combo_showresults.currentText()
        resultsDialogSuccess.close()

        reports = [str(x).lstrip('0') for x in reports]
        reports.sort()

        if results_option in ['Save PDFs to zipped folder','Open and save PDFs']:
            savelocation = QFileDialog.getExistingDirectory(None, 'Select a folder:', '', QFileDialog.ShowDirsOnly)
            try:
                os.mkdir(os.path.join(savelocation,'soilsreports'))
            except FileExistsError:
                # at some point need to raise a flag that directory already exists
                for f in os.listdir(os.path.join(savelocation,'soilsreports')):
                    os.remove(os.path.join(os.path.join(savelocation,'soilsreports'),f))
                os.rmdir(os.path.join(savelocation,'soilsreports'))
                os.mkdir(os.path.join(savelocation,'soilsreports'))

        pdfsnotexist = []
        for r in reports:
            report = '/' + str(r) + '.pdf'
            try:
                if results_option in ['Save PDFs to zipped folder','Open and save PDFs']:
                    shutil.copyfile(folder + report,savelocation+'/soilsreports'+report)
                    
                if results_option in ['Open PDFs','Open and save PDFs']:
                    os.startfile(folder + report)
                

            except FileNotFoundError:
                pdfsnotexist.append(report[1:])
        
        if len(pdfsnotexist) != len(reports):
            if results_option == 'Save PDFs to zipped folder':
                resultsDialogAfterOpen.label.setText(f'{len(reports)-len(pdfsnotexist)} reports have been saved!')
            elif results_option == 'Open and save PDFs':
                resultsDialogAfterOpen.label.setText(f'{len(reports)-len(pdfsnotexist)} reports have been opened and saved!')
            else:
                resultsDialogAfterOpen.label.setText(f'{len(reports)-len(pdfsnotexist)} reports have been opened!')

        else:
            resultsDialogAfterOpen.label.setText('')

        if len(pdfsnotexist) > 0:
            message = 'The following pdfs do not exist in the folder but are present in the database:' + '\n'
            color = 'red'
            for x in pdfsnotexist:
                message = message + '\n' + x
        else:
            message = 'No errors occurred.'
            color = 'green'

        resultsDialogAfterOpen.text_reportfound.setText(message)
        resultsDialogAfterOpen.text_reportfound.setStyleSheet("color: "+color+';')
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ControlMainWindow()
    window.show()
    sys.exit(app.exec_())