from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QProgressBar, QFileDialog, QMainWindow, QApplication, QListWidgetItem
from PyQt5.QtCore import QUrl, pyqtSignal, Qt

import os, sys, shutil
import pandas as pd
from config import folder
from functions.windowdefaults import window_defaults

from ui_main import Ui_appmainwindow

appname = 'DOWL Soils Library Search App'
icon_path = 'png/icon.ico'

# GLOBAL VARS
reports, resultsDialogSuccess = '', ''
client, project, area, city = 'None selected...','None selected...','None selected...','None selected...'
df = pd.read_excel('SoilsReportRecord.xls')
for x in df.columns.tolist():
    df[x] = df[x].str.title()
authorizedcredentials = {'sklump':'dowluser'}
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
        self.setFixedSize(self.size())
        self.btn_mainmenu.clicked.connect(self.backto_mainmenu)
        self.btn_submit.setDefault(True)

class ResultsDialogFailure(QDialog, Master):
    def __init__(self):
        super(ResultsDialogFailure, self).__init__()
        self.ui = uic.loadUi('ui/resultsdialog_failure.ui', self)
        self.setFixedSize(self.size())
        self.btn_mainmenu.clicked.connect(self.backto_mainmenu)

class ResultsDialogAfterOpen(QDialog, Master):
    def __init__(self):
        super(ResultsDialogAfterOpen, self).__init__()
        self.ui = uic.loadUi('ui/resultsdialog_afteropen.ui', self)
        self.setFixedSize(self.size())
        self.btn_mainmenu.clicked.connect(self.backto_mainmenu)



# MAIN WINDOW ---------------------------------------------------------------------------------------------------------
class ControlMainWindow(QMainWindow, Master):

    def __init__(self):
        super(ControlMainWindow, self).__init__()
        self.ui = Ui_appmainwindow()
        self.ui.setupUi(self)

        self.setFixedSize(self.size())
        self.setWindowTitle(appname)

        global client, project, area, city
        dict_dropdown = {self.ui.list_client:[client,'Client'], self.ui.list_project:[project,'Project Name'], self.ui.list_area:[area,'Area'], self.ui.list_city:[city,'CITY']}

        # add options to combo box from excel file
        for k,v in dict_dropdown.items():
            combolist = list(df[v[1]].unique())
            combolist = sorted([item for item in combolist if not(pd.isnull(item)) == True])
            for x in combolist:
                k.addItem(x)

        self.ui.list_client.setCurrentItem(QListWidgetItem('Adot&Pf'))
        # Set previous selections
        # for k, v in dict_dropdown.items():
        #     k.setCurrentText(v[0])

        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(0))
        self.ui.btn_about.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(1))
        self.ui.btn_admin.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(2))

        self.ui.btn_search.setDefault(True)
        self.ui.btn_search.clicked.connect(self.get_results)
        self.ui.btn_reset.clicked.connect(self.reset)

        self.ui.btn_searchclient.clicked.connect(self.filter_client_list)
        self.ui.btn_searchproject.clicked.connect(self.filter_project_list)
        self.ui.btn_searcharea.clicked.connect(self.filter_area_list)
        self.ui.btn_searchcity.clicked.connect(self.filter_city_list)
        self.ui.btn_adminsubmit.clicked.connect(self.submitcredentials)

    def submitcredentials(self):
        user = self.ui.line_user.text()
        password = self.ui.line_pass.text()
        if user in authorizedcredentials:
            if password == authorizedcredentials[user]:
                self.ui.lab_invalidcreds.setText('')
                self.ui.stackedWidget_2.setCurrentIndex(3)
                self.ui.lab_welcome.setText(f'Welcome {user}! This is the admin dashboard.')
            else:
                self.ui.lab_invalidcreds.setText('The password is not correct. Please try again.')
        else:
            self.ui.lab_invalidcreds.setText('The username is not correct. Please try again.')



    def filter_client_list(self):
        searchinput = self.ui.line_searchclient.text()
        
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
        searchinput = self.ui.line_searchproject.text()
        
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
        searchinput = self.ui.line_searcharea.text()
        
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
        searchinput = self.ui.line_searchcity.text()
        
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
        list_dropdown = [self.ui.combo_client, self.ui.combo_project, self.ui.combo_area, self.ui.combo_city]
        for x in list_dropdown:
            x.setCurrentText('None selected...')


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