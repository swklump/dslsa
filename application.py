from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QLabel, QProgressBar, QFileDialog, QMainWindow, QApplication
from PyQt5.QtGui import QPixmap, QIntValidator, QDesktopServices
from PyQt5.QtCore import QUrl, pyqtSignal

import os
import pandas as pd
from config import folder
import sys
from functions.windowdefaults import window_defaults

from ui_main import Ui_appmainwindow

appname = 'DOWL Soils Library Search App'
icon_path = 'png/icon.ico'
reports = ''
resultsDialog = ''
df = pd.read_excel('SoilsReportRecord.xls')


class Master():

    def backto_mainmenu(self):
        self.close()
        ControlMainWindow().show()
    # Function for the hyperlink
    # def link(self, linkStr):
    #     QDesktopServices.openUrl(QUrl(linkStr))


class ResultsDialog(QDialog, Master):
    def __init__(self):
        super(ResultsDialog, self).__init__()
        self.ui = uic.loadUi('ui/resultsdialog.ui', self)
        self.setFixedSize(self.size())
        self.btn_no.clicked.connect(self.backto_mainmenu)


class ControlMainWindow(QMainWindow, Master):

    def __init__(self):
        super(ControlMainWindow, self).__init__()
        self.ui = Ui_appmainwindow()
        self.ui.setupUi(self)

        self.setWindowTitle(appname) #SETS THE APPLICATION NAME IN THE WINDOW TOPBAR  

        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(0))
        self.ui.btn_about.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(1))

        self.ui.btn_search.clicked.connect(self.showResultsDialog)
    
    def showResultsDialog(self):
        global reports, resultsDialog
        resultsDialog = ResultsDialog()
        resultsDialog.show()
        self.close()

        client = self.ui.combo_client.currentText()
        project = self.ui.combo_project.currentText()
        area = self.ui.combo_area.currentText()
        city = self.ui.combo_city.currentText()

        # apply selected filters
        results = df
        search_dict = {client:'Client', project:'Project Name', area:'Area', city:'CITY'}
        for k,v in search_dict.items():
            if k != 'None selected...':
                results = results[results[v]==k]

        reports = results['Report#'].values.tolist()
        reports = [int(str(x).lstrip('0')) for x in reports]
        reports.sort()

        resultsDialog.text_reportfound.setText(f'There were {len(reports)} results found!')
        resultsDialog.text_reportfound.setReadOnly(True)
        resultsDialog.btn_yes.clicked.connect(self.openpdfs)

    
    def openpdfs(self):
        global reports, resultsDialog

        pdfsnotexist = []
        for r in reports:
            report = '/' + str(r) + '.pdf'
            try:
                os.startfile(folder + report)
            except FileNotFoundError:
                pdfsnotexist.append(report[1:])
        
        message = 'The pdfs have been opened!'
        color = 'green'
        if len(pdfsnotexist) > 0:
            message = 'The following pdfs do not exist in the folder but are present in the database:' + '\n'
            color = 'red'
            for x in pdfsnotexist:
                message = message + '\n' + x
        resultsDialog.label_2.setText('Would you like to search for more reports?')
        resultsDialog.text_reportfound.setText(message)
        resultsDialog.text_reportfound.setStyleSheet("color: "+color+';')
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ControlMainWindow()
    window.show()
    sys.exit(app.exec_())

# app = QtWidgets.QApplication(argv)
# mainWindow = HomePage()
# mainWindow.show()
# exit(app.exec_())