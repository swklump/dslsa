from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QFileDialog, QVBoxLayout, QMainWindow, QApplication, QListWidgetItem
# from PyQt5.QtCore import QUrl, pyqtSignal, Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView

import os, sys, shutil, folium, io, markupsafe
import pandas as pd
from config import folder
from functions.windowdefaults import window_defaults

from ui_main import Ui_appmainwindow

appname = 'DOWL Soils Library Search App'
icon_path = 'png/icon.ico'

# GLOBAL VARS
reports, resultsDialogSuccess = '', ''
client, project, area, city = 'None selected...','None selected...','None selected...','None selected...'
searchclientvar, searchprojectvar,searchareavar, searchcityvar = '','','',''
df = pd.read_excel('SoilsReportRecord.xls')
for x in ['Client','Project Name','Area','CITY']:
    df[x] = df[x].str.title()
authorizedcredentials = {'sklump':'dowluser'}
adminvalidated = False

class Master():

    def backto_mainmenu(self):
        self.close()
        ControlMainWindow().show()
    # Function for the hyperlink
    # def link(self, linkStr):
    #     QDesktopServices.openUrl(QUrl(linkStr))


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

        global client, project, area, city, adminvalidated
        dict_dropdown = {self.ui.list_client:[client,'Client'], self.ui.list_project:[project,'Project Name'], self.ui.list_area:[area,'Area'], self.ui.list_city:[city,'CITY']}

        # add options to combo box from excel file
        for k,v in dict_dropdown.items():
            combolist = list(df[v[1]].unique())
            combolist = sorted([item for item in combolist if not(pd.isnull(item)) == True])
            for x in combolist:
                k.addItem(x)

        self.ui.line_searchclient.setText(searchclientvar)
        self.ui.line_searchproject.setText(searchprojectvar)
        self.ui.line_searcharea.setText(searchareavar)
        self.ui.line_searchcity.setText(searchcityvar)
        
        # add map
        coordinate = (37.8199286, -122.4782551)
        m = folium.Map(
        	tiles='Stamen Terrain',
        	zoom_start=13,
        	location=coordinate
        )

        # save map data to data object
        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        self.ui.verticalLayout_2.addWidget(webView)

        self.ui.list_client.setCurrentItem(QListWidgetItem('Adot&Pf'))
        # Set previous selections
        # for k, v in dict_dropdown.items():
        #     k.setCurrentText(v[0])

        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(0))
        self.ui.btn_about.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(1))
        self.ui.btn_admin.clicked.connect(lambda adminvalidated: self.ui.stackedWidget_2.setCurrentIndex(2) if adminvalidated == False else self.ui.stackedWidget_2.setCurrentIndex(3))

        self.ui.btn_search.setDefault(True)
        self.ui.btn_search.clicked.connect(self.get_results)
        self.ui.btn_reset.clicked.connect(self.reset)

        self.ui.btn_searchclient.clicked.connect(self.filter_client_list)
        self.ui.btn_searchproject.clicked.connect(self.filter_project_list)
        self.ui.btn_searcharea.clicked.connect(self.filter_area_list)
        self.ui.btn_searchcity.clicked.connect(self.filter_city_list)
        self.ui.btn_adminsubmit.clicked.connect(self.submitcredentials)
        self.ui.btn_submitexcelpath.clicked.connect(self.changeexcelpath)

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
    def filter_client_list(self):
        global searchclientvar
        searchinput = self.ui.line_searchclient.text()
        searchclientvar = searchinput
        
        # if search is blank, load all options
        if searchinput == '':
            combolist = list(df['Client'].unique())
            combolist = sorted([item for item in combolist if not(pd.isnull(item)) == True])
            self.ui.list_client.clear()
            self.ui.list_client.addItems(combolist)
        
        # else get list of items with search input contained
        else:
            matching_results = []
            for x in df['Client'].values.tolist():
                if str(searchinput).lower() in str(x).lower():
                    matching_results.append(x)
            matching_results = sorted(set(matching_results))
            self.ui.list_client.clear()
            for x in matching_results:
                self.ui.list_client.addItem(x)
        
    def filter_project_list(self):
        global searchprojectvar
        searchinput = self.ui.line_searchproject.text()
        searchprojectvar = searchinput

        
        # if search is blank, load all options
        if searchinput == '':
            combolist = list(df['Project Name'].unique())
            combolist = sorted([item for item in combolist if not(pd.isnull(item)) == True])
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
        
    def filter_area_list(self):
        global searchareavar
        searchinput = self.ui.line_searcharea.text()
        searchareavar = searchinput

        
        # if search is blank, load all options
        if searchinput == '':
            combolist = list(df['Area'].unique())
            combolist = sorted([item for item in combolist if not(pd.isnull(item)) == True])
            self.ui.list_area.clear()
            self.ui.list_area.addItems(combolist)
        
        # else get list of items with search input contained
        else:
            matching_results = []
            for x in df['Area'].values.tolist():
                if str(searchinput).lower() in str(x).lower():
                    matching_results.append(x)
            matching_results = sorted(set(matching_results))
            self.ui.list_area.clear()
            for x in matching_results:
                self.ui.list_area.addItem(x)
        
    def filter_city_list(self):
        global searchcityvar
        searchinput = self.ui.line_searchcity.text()
        searchcityvar = searchinput

        
        # if search is blank, load all options
        if searchinput == '':
            combolist = list(df['CITY'].unique())
            combolist = sorted([item for item in combolist if not(pd.isnull(item)) == True])
            self.ui.list_city.clear()
            self.ui.list_city.addItems(combolist)
        
        # else get list of items with search input contained
        else:
            matching_results = []
            for x in df['CITY'].values.tolist():
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

        combolist = list(df['Client'].unique())
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
        global reports, client, project, area, city

        client = self.ui.list_client.selectedItems()
        project = self.ui.list_project.selectedItems()
        area = self.ui.list_area.selectedItems()
        city = self.ui.list_city.selectedItems()

        # apply selected filters
        results = df
        search_dict = {'Client':client, 'Project Name':project, 'Area':area, 'CITY':city}
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
        global reports, resultsDialogSuccess, client, project, area, city
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