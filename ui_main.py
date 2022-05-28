# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_appmainwindow(object):
    def setupUi(self, appmainwindow):
        appmainwindow.setObjectName("appmainwindow")
        appmainwindow.resize(733, 447)
        self.centralwidget = QtWidgets.QWidget(appmainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame_west = QtWidgets.QFrame(self.frame)
        self.frame_west.setMinimumSize(QtCore.QSize(80, 0))
        self.frame_west.setMaximumSize(QtCore.QSize(80, 16777215))
        self.frame_west.setStyleSheet("background:rgb(51,51,51);")
        self.frame_west.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_west.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_west.setObjectName("frame_west")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_west)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_home = QtWidgets.QFrame(self.frame_west)
        self.frame_home.setMinimumSize(QtCore.QSize(80, 55))
        self.frame_home.setMaximumSize(QtCore.QSize(160, 55))
        self.frame_home.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_home.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_home.setObjectName("frame_home")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_home)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.btn_home = QtWidgets.QPushButton(self.frame_home)
        self.btn_home.setMinimumSize(QtCore.QSize(80, 55))
        self.btn_home.setMaximumSize(QtCore.QSize(160, 55))
        self.btn_home.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.btn_home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\../../../Downloads/Minimalistic-Flat-Modern-GUI-Template-master/Minimalistic-Flat-Modern-GUI-Template-master/icons/1x/homeAsset 46.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_home.setIcon(icon)
        self.btn_home.setIconSize(QtCore.QSize(22, 22))
        self.btn_home.setFlat(True)
        self.btn_home.setObjectName("btn_home")
        self.horizontalLayout_15.addWidget(self.btn_home)
        self.verticalLayout_3.addWidget(self.frame_home)
        self.frame_about_2 = QtWidgets.QFrame(self.frame_west)
        self.frame_about_2.setMinimumSize(QtCore.QSize(80, 55))
        self.frame_about_2.setMaximumSize(QtCore.QSize(160, 55))
        self.frame_about_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_about_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_about_2.setObjectName("frame_about_2")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_about_2)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.btn_about = QtWidgets.QPushButton(self.frame_about_2)
        self.btn_about.setMinimumSize(QtCore.QSize(80, 55))
        self.btn_about.setMaximumSize(QtCore.QSize(160, 55))
        self.btn_about.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.btn_about.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui\\../png/img_28891.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_about.setIcon(icon1)
        self.btn_about.setIconSize(QtCore.QSize(30, 30))
        self.btn_about.setFlat(True)
        self.btn_about.setObjectName("btn_about")
        self.horizontalLayout_16.addWidget(self.btn_about)
        self.verticalLayout_3.addWidget(self.frame_about_2)
        self.frame_west_bottom = QtWidgets.QFrame(self.frame_west)
        self.frame_west_bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_west_bottom.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_west_bottom.setObjectName("frame_west_bottom")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_west_bottom)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3.addWidget(self.frame_west_bottom)
        self.gridLayout_7.addWidget(self.frame_west, 0, 0, 1, 1)
        self.frame_east = QtWidgets.QFrame(self.frame)
        self.frame_east.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_east.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_east.setObjectName("frame_east")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_east)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_east_top = QtWidgets.QFrame(self.frame_east)
        self.frame_east_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_east_top.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_east_top.setObjectName("frame_east_top")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_east_top)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame_east_top)
        self.stackedWidget_2.setMinimumSize(QtCore.QSize(0, 55))
        self.stackedWidget_2.setStyleSheet("")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_home_2 = QtWidgets.QWidget()
        self.page_home_2.setStyleSheet("background:rgb(91,90,90);")
        self.page_home_2.setObjectName("page_home_2")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.page_home_2)
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.frame_home_main_2 = QtWidgets.QFrame(self.page_home_2)
        self.frame_home_main_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_home_main_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_home_main_2.setObjectName("frame_home_main_2")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_home_main_2)
        self.verticalLayout_15.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.lab_home_main_hed_2 = QtWidgets.QLabel(self.frame_home_main_2)
        self.lab_home_main_hed_2.setMinimumSize(QtCore.QSize(0, 55))
        self.lab_home_main_hed_2.setMaximumSize(QtCore.QSize(16777215, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(24)
        self.lab_home_main_hed_2.setFont(font)
        self.lab_home_main_hed_2.setStyleSheet("QLabel {\n"
"    color:rgb(255,255,255);\n"
"}")
        self.lab_home_main_hed_2.setTextFormat(QtCore.Qt.RichText)
        self.lab_home_main_hed_2.setObjectName("lab_home_main_hed_2")
        self.verticalLayout_15.addWidget(self.lab_home_main_hed_2)
        self.label_13 = QtWidgets.QLabel(self.frame_home_main_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_15.addWidget(self.label_13)
        self.combo_client = QtWidgets.QComboBox(self.frame_home_main_2)
        self.combo_client.setObjectName("combo_client")
        self.combo_client.addItem("")
        self.combo_client.addItem("")
        self.combo_client.addItem("")
        self.verticalLayout_15.addWidget(self.combo_client)
        self.label_14 = QtWidgets.QLabel(self.frame_home_main_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_15.addWidget(self.label_14)
        self.combo_project = QtWidgets.QComboBox(self.frame_home_main_2)
        self.combo_project.setObjectName("combo_project")
        self.combo_project.addItem("")
        self.combo_project.addItem("")
        self.combo_project.addItem("")
        self.verticalLayout_15.addWidget(self.combo_project)
        self.label_15 = QtWidgets.QLabel(self.frame_home_main_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_15.addWidget(self.label_15)
        self.combo_area = QtWidgets.QComboBox(self.frame_home_main_2)
        self.combo_area.setObjectName("combo_area")
        self.combo_area.addItem("")
        self.combo_area.addItem("")
        self.combo_area.addItem("")
        self.combo_area.addItem("")
        self.verticalLayout_15.addWidget(self.combo_area)
        self.label_16 = QtWidgets.QLabel(self.frame_home_main_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_15.addWidget(self.label_16)
        self.combo_city = QtWidgets.QComboBox(self.frame_home_main_2)
        self.combo_city.setObjectName("combo_city")
        self.combo_city.addItem("")
        self.combo_city.addItem("")
        self.combo_city.addItem("")
        self.verticalLayout_15.addWidget(self.combo_city)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_15.addItem(spacerItem)
        self.btn_search = QtWidgets.QPushButton(self.frame_home_main_2)
        self.btn_search.setObjectName("btn_search")
        self.verticalLayout_15.addWidget(self.btn_search)
        self.horizontalLayout_30.addWidget(self.frame_home_main_2, 0, QtCore.Qt.AlignLeft)
        self.frame_5 = QtWidgets.QFrame(self.page_home_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_11 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:rgb(255,255,255);")
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.text_msgbox = QtWidgets.QTextEdit(self.frame_5)
        self.text_msgbox.setObjectName("text_msgbox")
        self.verticalLayout.addWidget(self.text_msgbox)
        self.label_12 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:rgb(255,255,255);")
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.text_files = QtWidgets.QTextEdit(self.frame_5)
        self.text_files.setObjectName("text_files")
        self.verticalLayout.addWidget(self.text_files)
        self.horizontalLayout_30.addWidget(self.frame_5)
        self.stackedWidget_2.addWidget(self.page_home_2)
        self.page_about = QtWidgets.QWidget()
        self.page_about.setStyleSheet("background:rgb(91,90,90);")
        self.page_about.setObjectName("page_about")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.page_about)
        self.verticalLayout_17.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_17.setSpacing(5)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.lab_about_home_2 = QtWidgets.QLabel(self.page_about)
        self.lab_about_home_2.setMinimumSize(QtCore.QSize(0, 55))
        self.lab_about_home_2.setMaximumSize(QtCore.QSize(16777215, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self.lab_about_home_2.setFont(font)
        self.lab_about_home_2.setStyleSheet("color:rgb(255,255,255);")
        self.lab_about_home_2.setObjectName("lab_about_home_2")
        self.verticalLayout_17.addWidget(self.lab_about_home_2)
        self.frame_about = QtWidgets.QFrame(self.page_about)
        self.frame_about.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_about.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_about.setObjectName("frame_about")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.frame_about)
        self.horizontalLayout_31.setContentsMargins(5, 5, 0, 5)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.lab_home_main_disc_2 = QtWidgets.QLabel(self.frame_about)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lab_home_main_disc_2.setFont(font)
        self.lab_home_main_disc_2.setStyleSheet("color:rgb(255,255,255);")
        self.lab_home_main_disc_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lab_home_main_disc_2.setWordWrap(True)
        self.lab_home_main_disc_2.setObjectName("lab_home_main_disc_2")
        self.horizontalLayout_31.addWidget(self.lab_home_main_disc_2)
        self.verticalLayout_17.addWidget(self.frame_about)
        self.stackedWidget_2.addWidget(self.page_about)
        self.horizontalLayout_17.addWidget(self.stackedWidget_2)
        self.verticalLayout_14.addWidget(self.frame_east_top)
        self.gridLayout_7.addWidget(self.frame_east, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        appmainwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(appmainwindow)
        self.statusbar.setObjectName("statusbar")
        appmainwindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(appmainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 733, 21))
        self.menubar.setObjectName("menubar")
        appmainwindow.setMenuBar(self.menubar)

        self.retranslateUi(appmainwindow)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(appmainwindow)

    def retranslateUi(self, appmainwindow):
        _translate = QtCore.QCoreApplication.translate
        appmainwindow.setWindowTitle(_translate("appmainwindow", "MainWindow"))
        self.btn_home.setToolTip(_translate("appmainwindow", "Home"))
        self.btn_about.setToolTip(_translate("appmainwindow", "Bug"))
        self.lab_home_main_hed_2.setText(_translate("appmainwindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Report Search Tool</span></p></body></html>"))
        self.label_13.setText(_translate("appmainwindow", "Select a Client..."))
        self.combo_client.setItemText(0, _translate("appmainwindow", "None selected..."))
        self.combo_client.setItemText(1, _translate("appmainwindow", "Alaska Department of Fish and Game "))
        self.combo_client.setItemText(2, _translate("appmainwindow", "ALASKA RAILROAD CORP"))
        self.label_14.setText(_translate("appmainwindow", "Select a Project Name..."))
        self.combo_project.setItemText(0, _translate("appmainwindow", "None selected..."))
        self.combo_project.setItemText(1, _translate("appmainwindow", "EAST PARK SUBDIVISION"))
        self.combo_project.setItemText(2, _translate("appmainwindow", "PORT INDUSTRIAL AREA"))
        self.label_15.setText(_translate("appmainwindow", "Select a Area..."))
        self.combo_area.setItemText(0, _translate("appmainwindow", "None selected..."))
        self.combo_area.setItemText(1, _translate("appmainwindow", "1"))
        self.combo_area.setItemText(2, _translate("appmainwindow", "2"))
        self.combo_area.setItemText(3, _translate("appmainwindow", "3"))
        self.label_16.setText(_translate("appmainwindow", "Select a City..."))
        self.combo_city.setItemText(0, _translate("appmainwindow", "None selected..."))
        self.combo_city.setItemText(1, _translate("appmainwindow", "Anchorage"))
        self.combo_city.setItemText(2, _translate("appmainwindow", "Adak"))
        self.btn_search.setText(_translate("appmainwindow", "Search"))
        self.label_11.setText(_translate("appmainwindow", "Message Box"))
        self.label_12.setText(_translate("appmainwindow", "Available Files"))
        self.lab_about_home_2.setText(_translate("appmainwindow", "About"))
        self.lab_home_main_disc_2.setText(_translate("appmainwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Name: DOWL Soils Library Search App</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Version: 1.0</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Contact: Sam Klump at sklump@dowl.com</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Description: This app...</span></p></body></html>"))
