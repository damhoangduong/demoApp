# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainftPkqf.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1209, 756)
        MainWindow.setMinimumSize(QSize(1209, 756))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setCursor(QCursor(Qt.PointingHandCursor))
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_lu139 = QPushButton(self.topMenu)
        self.btn_lu139.setObjectName(u"btn_lu139")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_lu139.sizePolicy().hasHeightForWidth())
        self.btn_lu139.setSizePolicy(sizePolicy)
        self.btn_lu139.setMinimumSize(QSize(0, 45))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.btn_lu139.setFont(font1)
        self.btn_lu139.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_lu139.setLayoutDirection(Qt.LeftToRight)
        self.btn_lu139.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-arrow-circle-right.png);\n"
"font: 700 12pt \"Segoe UI\";")

        self.verticalLayout_8.addWidget(self.btn_lu139)

        self.btn_lu205 = QPushButton(self.topMenu)
        self.btn_lu205.setObjectName(u"btn_lu205")
        sizePolicy.setHeightForWidth(self.btn_lu205.sizePolicy().hasHeightForWidth())
        self.btn_lu205.setSizePolicy(sizePolicy)
        self.btn_lu205.setMinimumSize(QSize(0, 45))
        self.btn_lu205.setFont(font1)
        self.btn_lu205.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_lu205.setLayoutDirection(Qt.LeftToRight)
        self.btn_lu205.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-arrow-circle-right.png);\n"
"font: 700 12pt \"Segoe UI\";")

        self.verticalLayout_8.addWidget(self.btn_lu205)

        self.btn_lu132 = QPushButton(self.topMenu)
        self.btn_lu132.setObjectName(u"btn_lu132")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_lu132.sizePolicy().hasHeightForWidth())
        self.btn_lu132.setSizePolicy(sizePolicy1)
        self.btn_lu132.setMinimumSize(QSize(0, 45))
        self.btn_lu132.setFont(font1)
        self.btn_lu132.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_lu132.setLayoutDirection(Qt.LeftToRight)
        self.btn_lu132.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-arrow-circle-right.png);\n"
"font: 700 12pt \"Segoe UI\";")
        self.btn_lu132.setIconSize(QSize(16, 16))

        self.verticalLayout_8.addWidget(self.btn_lu132)

        self.btn_lu596 = QPushButton(self.topMenu)
        self.btn_lu596.setObjectName(u"btn_lu596")
        sizePolicy.setHeightForWidth(self.btn_lu596.sizePolicy().hasHeightForWidth())
        self.btn_lu596.setSizePolicy(sizePolicy)
        self.btn_lu596.setMinimumSize(QSize(0, 45))
        self.btn_lu596.setFont(font1)
        self.btn_lu596.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_lu596.setLayoutDirection(Qt.LeftToRight)
        self.btn_lu596.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-arrow-circle-right.png);\n"
"font: 700 12pt \"Segoe UI\";")

        self.verticalLayout_8.addWidget(self.btn_lu596)

        self.btn_ip = QPushButton(self.topMenu)
        self.btn_ip.setObjectName(u"btn_ip")
        sizePolicy.setHeightForWidth(self.btn_ip.sizePolicy().hasHeightForWidth())
        self.btn_ip.setSizePolicy(sizePolicy)
        self.btn_ip.setMinimumSize(QSize(0, 45))
        self.btn_ip.setFont(font)
        self.btn_ip.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ip.setLayoutDirection(Qt.LeftToRight)
        self.btn_ip.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_ip)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy2)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy3)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setItalic(False)
        self.titleRightInfo.setFont(font2)
        self.titleRightInfo.setStyleSheet(u"font: 700 14pt \"Segoe UI\";")
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;\n"
"background-color: rgb(255, 255, 255);")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.gridLayout = QGridLayout(self.home)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.home)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_19 = QVBoxLayout(self.widget_8)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy)
        self.verticalLayout_22 = QVBoxLayout(self.widget_9)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget_9)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 22pt \"Segoe UI\";")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_6)

        self.label_2 = QLabel(self.widget_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_2)


        self.verticalLayout_19.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.widget_8)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_23 = QVBoxLayout(self.widget_10)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.lisTram_1 = QWidget(self.widget_10)
        self.lisTram_1.setObjectName(u"lisTram_1")
        sizePolicy1.setHeightForWidth(self.lisTram_1.sizePolicy().hasHeightForWidth())
        self.lisTram_1.setSizePolicy(sizePolicy1)
        self.lisTram_1.setStyleSheet(u"border-right-color: rgb(0, 0, 0);")
        self.horizontalLayout_6 = QHBoxLayout(self.lisTram_1)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, -1)
        self.widget_17 = QWidget(self.lisTram_1)
        self.widget_17.setObjectName(u"widget_17")
        self.verticalLayout_41 = QVBoxLayout(self.widget_17)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.widget_46 = QWidget(self.widget_17)
        self.widget_46.setObjectName(u"widget_46")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_46.sizePolicy().hasHeightForWidth())
        self.widget_46.setSizePolicy(sizePolicy4)
        self.widget_46.setStyleSheet(u"font: 700 16pt \"Segoe UI\";")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_46)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.widget_46)
        self.label_16.setObjectName(u"label_16")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy5)
        self.label_16.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_19.addWidget(self.label_16)


        self.verticalLayout_41.addWidget(self.widget_46)

        self.widget_47 = QWidget(self.widget_17)
        self.widget_47.setObjectName(u"widget_47")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_47)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.widget_48 = QWidget(self.widget_47)
        self.widget_48.setObjectName(u"widget_48")
        self.verticalLayout_42 = QVBoxLayout(self.widget_48)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.widget_57 = QWidget(self.widget_48)
        self.widget_57.setObjectName(u"widget_57")
        sizePolicy1.setHeightForWidth(self.widget_57.sizePolicy().hasHeightForWidth())
        self.widget_57.setSizePolicy(sizePolicy1)
        self.widget_57.setStyleSheet(u"")
        self.verticalLayout_29 = QVBoxLayout(self.widget_57)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_57)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"")
        self.label_8.setPixmap(QPixmap(u":/images/images/images/logo-binh-chung-thong-tin-lien-lac.png"))
        self.label_8.setScaledContents(True)

        self.verticalLayout_29.addWidget(self.label_8)

        self.label_18 = QLabel(self.widget_57)
        self.label_18.setObjectName(u"label_18")
        sizePolicy5.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy5)
        self.label_18.setStyleSheet(u"background-position: center;\n"
"background-repeat: no-repeat")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_18)


        self.verticalLayout_42.addWidget(self.widget_57)

        self.widget_58 = QWidget(self.widget_48)
        self.widget_58.setObjectName(u"widget_58")
        sizePolicy4.setHeightForWidth(self.widget_58.sizePolicy().hasHeightForWidth())
        self.widget_58.setSizePolicy(sizePolicy4)
        self.horizontalLayout_16 = QHBoxLayout(self.widget_58)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, -1, 0, 0)
        self.widget_59 = QWidget(self.widget_58)
        self.widget_59.setObjectName(u"widget_59")
        self.verticalLayout_45 = QVBoxLayout(self.widget_59)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.widget_60 = QWidget(self.widget_59)
        self.widget_60.setObjectName(u"widget_60")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_60)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ac1 = QPushButton(self.widget_60)
        self.pushButton_ac1.setObjectName(u"pushButton_ac1")
        sizePolicy5.setHeightForWidth(self.pushButton_ac1.sizePolicy().hasHeightForWidth())
        self.pushButton_ac1.setSizePolicy(sizePolicy5)
        self.pushButton_ac1.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"	background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_23.addWidget(self.pushButton_ac1)


        self.verticalLayout_45.addWidget(self.widget_60)

        self.widget_72 = QWidget(self.widget_59)
        self.widget_72.setObjectName(u"widget_72")
        self.verticalLayout_46 = QVBoxLayout(self.widget_72)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.widget_72)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_46.addWidget(self.label_19)


        self.verticalLayout_45.addWidget(self.widget_72)


        self.horizontalLayout_16.addWidget(self.widget_59)

        self.widget_73 = QWidget(self.widget_58)
        self.widget_73.setObjectName(u"widget_73")
        self.verticalLayout_47 = QVBoxLayout(self.widget_73)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.widget_74 = QWidget(self.widget_73)
        self.widget_74.setObjectName(u"widget_74")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_74)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ac2 = QPushButton(self.widget_74)
        self.pushButton_ac2.setObjectName(u"pushButton_ac2")
        sizePolicy5.setHeightForWidth(self.pushButton_ac2.sizePolicy().hasHeightForWidth())
        self.pushButton_ac2.setSizePolicy(sizePolicy5)
        self.pushButton_ac2.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_25.addWidget(self.pushButton_ac2)


        self.verticalLayout_47.addWidget(self.widget_74)

        self.widget_76 = QWidget(self.widget_73)
        self.widget_76.setObjectName(u"widget_76")
        self.verticalLayout_48 = QVBoxLayout(self.widget_76)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.widget_76)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_48.addWidget(self.label_20)


        self.verticalLayout_47.addWidget(self.widget_76)


        self.horizontalLayout_16.addWidget(self.widget_73)


        self.verticalLayout_42.addWidget(self.widget_58)


        self.horizontalLayout_22.addWidget(self.widget_48)

        self.widget_124 = QWidget(self.widget_47)
        self.widget_124.setObjectName(u"widget_124")
        self.verticalLayout_17 = QVBoxLayout(self.widget_124)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, 0, -1, 0)
        self.widget_125 = QWidget(self.widget_124)
        self.widget_125.setObjectName(u"widget_125")
        self.horizontalLayout_65 = QHBoxLayout(self.widget_125)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.pushButton_nhietdo = QPushButton(self.widget_125)
        self.pushButton_nhietdo.setObjectName(u"pushButton_nhietdo")
        sizePolicy5.setHeightForWidth(self.pushButton_nhietdo.sizePolicy().hasHeightForWidth())
        self.pushButton_nhietdo.setSizePolicy(sizePolicy5)
        self.pushButton_nhietdo.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_nhietdo.setIconSize(QSize(20, 20))

        self.horizontalLayout_65.addWidget(self.pushButton_nhietdo)

        self.label_nhietdo_3 = QLabel(self.widget_125)
        self.label_nhietdo_3.setObjectName(u"label_nhietdo_3")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        self.label_nhietdo_3.setFont(font4)
        self.label_nhietdo_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_65.addWidget(self.label_nhietdo_3)


        self.verticalLayout_17.addWidget(self.widget_125)

        self.widget_126 = QWidget(self.widget_124)
        self.widget_126.setObjectName(u"widget_126")
        self.horizontalLayout_66 = QHBoxLayout(self.widget_126)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.pushButton_doam = QPushButton(self.widget_126)
        self.pushButton_doam.setObjectName(u"pushButton_doam")
        sizePolicy5.setHeightForWidth(self.pushButton_doam.sizePolicy().hasHeightForWidth())
        self.pushButton_doam.setSizePolicy(sizePolicy5)
        self.pushButton_doam.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_66.addWidget(self.pushButton_doam)

        self.label_doam_2 = QLabel(self.widget_126)
        self.label_doam_2.setObjectName(u"label_doam_2")
        self.label_doam_2.setFont(font4)
        self.label_doam_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_66.addWidget(self.label_doam_2)


        self.verticalLayout_17.addWidget(self.widget_126)

        self.widget_127 = QWidget(self.widget_124)
        self.widget_127.setObjectName(u"widget_127")
        self.horizontalLayout_67 = QHBoxLayout(self.widget_127)
        self.horizontalLayout_67.setSpacing(0)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.pushButton_anhsang = QPushButton(self.widget_127)
        self.pushButton_anhsang.setObjectName(u"pushButton_anhsang")
        sizePolicy5.setHeightForWidth(self.pushButton_anhsang.sizePolicy().hasHeightForWidth())
        self.pushButton_anhsang.setSizePolicy(sizePolicy5)
        self.pushButton_anhsang.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_67.addWidget(self.pushButton_anhsang)

        self.label_anhsang = QLabel(self.widget_127)
        self.label_anhsang.setObjectName(u"label_anhsang")
        self.label_anhsang.setFont(font4)
        self.label_anhsang.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_67.addWidget(self.label_anhsang)


        self.verticalLayout_17.addWidget(self.widget_127)

        self.widget_128 = QWidget(self.widget_124)
        self.widget_128.setObjectName(u"widget_128")
        self.horizontalLayout_68 = QHBoxLayout(self.widget_128)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.pushButton_dc1 = QPushButton(self.widget_128)
        self.pushButton_dc1.setObjectName(u"pushButton_dc1")
        sizePolicy5.setHeightForWidth(self.pushButton_dc1.sizePolicy().hasHeightForWidth())
        self.pushButton_dc1.setSizePolicy(sizePolicy5)
        self.pushButton_dc1.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_68.addWidget(self.pushButton_dc1)

        self.label_dc1 = QLabel(self.widget_128)
        self.label_dc1.setObjectName(u"label_dc1")
        self.label_dc1.setFont(font4)
        self.label_dc1.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_68.addWidget(self.label_dc1)


        self.verticalLayout_17.addWidget(self.widget_128)

        self.widget_129 = QWidget(self.widget_124)
        self.widget_129.setObjectName(u"widget_129")
        self.horizontalLayout_69 = QHBoxLayout(self.widget_129)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.pushButton_dc2 = QPushButton(self.widget_129)
        self.pushButton_dc2.setObjectName(u"pushButton_dc2")
        sizePolicy5.setHeightForWidth(self.pushButton_dc2.sizePolicy().hasHeightForWidth())
        self.pushButton_dc2.setSizePolicy(sizePolicy5)
        self.pushButton_dc2.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_69.addWidget(self.pushButton_dc2)

        self.label_dc2 = QLabel(self.widget_129)
        self.label_dc2.setObjectName(u"label_dc2")
        self.label_dc2.setFont(font4)
        self.label_dc2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_69.addWidget(self.label_dc2)


        self.verticalLayout_17.addWidget(self.widget_129)


        self.horizontalLayout_22.addWidget(self.widget_124)


        self.verticalLayout_41.addWidget(self.widget_47)


        self.horizontalLayout_6.addWidget(self.widget_17)

        self.widget_16 = QWidget(self.lisTram_1)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_35 = QVBoxLayout(self.widget_16)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.widget_35 = QWidget(self.widget_16)
        self.widget_35.setObjectName(u"widget_35")
        sizePolicy4.setHeightForWidth(self.widget_35.sizePolicy().hasHeightForWidth())
        self.widget_35.setSizePolicy(sizePolicy4)
        self.widget_35.setStyleSheet(u"font: 700 16pt \"Segoe UI\";")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_35)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.widget_35)
        self.label_12.setObjectName(u"label_12")
        sizePolicy5.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy5)
        self.label_12.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_17.addWidget(self.label_12)


        self.verticalLayout_35.addWidget(self.widget_35)

        self.widget_36 = QWidget(self.widget_16)
        self.widget_36.setObjectName(u"widget_36")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_36)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.widget_37 = QWidget(self.widget_36)
        self.widget_37.setObjectName(u"widget_37")
        self.verticalLayout_36 = QVBoxLayout(self.widget_37)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.widget_38 = QWidget(self.widget_37)
        self.widget_38.setObjectName(u"widget_38")
        sizePolicy1.setHeightForWidth(self.widget_38.sizePolicy().hasHeightForWidth())
        self.widget_38.setSizePolicy(sizePolicy1)
        self.widget_38.setStyleSheet(u"")
        self.verticalLayout_27 = QVBoxLayout(self.widget_38)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget_38)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"")
        self.label_7.setPixmap(QPixmap(u":/images/images/images/logo-binh-chung-thong-tin-lien-lac.png"))
        self.label_7.setScaledContents(True)

        self.verticalLayout_27.addWidget(self.label_7)

        self.label_13 = QLabel(self.widget_38)
        self.label_13.setObjectName(u"label_13")
        sizePolicy5.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy5)
        self.label_13.setStyleSheet(u"background-position: center;\n"
"background-repeat: no-repeat")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_13)


        self.verticalLayout_36.addWidget(self.widget_38)

        self.widget_39 = QWidget(self.widget_37)
        self.widget_39.setObjectName(u"widget_39")
        sizePolicy4.setHeightForWidth(self.widget_39.sizePolicy().hasHeightForWidth())
        self.widget_39.setSizePolicy(sizePolicy4)
        self.horizontalLayout_15 = QHBoxLayout(self.widget_39)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, -1, 0, 0)
        self.widget_40 = QWidget(self.widget_39)
        self.widget_40.setObjectName(u"widget_40")
        self.verticalLayout_37 = QVBoxLayout(self.widget_40)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.widget_41 = QWidget(self.widget_40)
        self.widget_41.setObjectName(u"widget_41")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_41)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ac1_2 = QPushButton(self.widget_41)
        self.pushButton_ac1_2.setObjectName(u"pushButton_ac1_2")
        sizePolicy5.setHeightForWidth(self.pushButton_ac1_2.sizePolicy().hasHeightForWidth())
        self.pushButton_ac1_2.setSizePolicy(sizePolicy5)
        self.pushButton_ac1_2.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"	background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_20.addWidget(self.pushButton_ac1_2)


        self.verticalLayout_37.addWidget(self.widget_41)

        self.widget_42 = QWidget(self.widget_40)
        self.widget_42.setObjectName(u"widget_42")
        self.verticalLayout_38 = QVBoxLayout(self.widget_42)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.widget_42)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_38.addWidget(self.label_14)


        self.verticalLayout_37.addWidget(self.widget_42)


        self.horizontalLayout_15.addWidget(self.widget_40)

        self.widget_43 = QWidget(self.widget_39)
        self.widget_43.setObjectName(u"widget_43")
        self.verticalLayout_39 = QVBoxLayout(self.widget_43)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.widget_44 = QWidget(self.widget_43)
        self.widget_44.setObjectName(u"widget_44")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_44)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.pushButton_dc2_8 = QPushButton(self.widget_44)
        self.pushButton_dc2_8.setObjectName(u"pushButton_dc2_8")
        sizePolicy5.setHeightForWidth(self.pushButton_dc2_8.sizePolicy().hasHeightForWidth())
        self.pushButton_dc2_8.setSizePolicy(sizePolicy5)
        self.pushButton_dc2_8.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_21.addWidget(self.pushButton_dc2_8)


        self.verticalLayout_39.addWidget(self.widget_44)

        self.widget_45 = QWidget(self.widget_43)
        self.widget_45.setObjectName(u"widget_45")
        self.verticalLayout_40 = QVBoxLayout(self.widget_45)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.widget_45)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_40.addWidget(self.label_15)


        self.verticalLayout_39.addWidget(self.widget_45)


        self.horizontalLayout_15.addWidget(self.widget_43)


        self.verticalLayout_36.addWidget(self.widget_39)


        self.horizontalLayout_18.addWidget(self.widget_37)

        self.widget_49 = QWidget(self.widget_36)
        self.widget_49.setObjectName(u"widget_49")
        self.verticalLayout_4 = QVBoxLayout(self.widget_49)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.widget_61 = QWidget(self.widget_49)
        self.widget_61.setObjectName(u"widget_61")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_61)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.pushButton_nhietdo_2 = QPushButton(self.widget_61)
        self.pushButton_nhietdo_2.setObjectName(u"pushButton_nhietdo_2")
        sizePolicy5.setHeightForWidth(self.pushButton_nhietdo_2.sizePolicy().hasHeightForWidth())
        self.pushButton_nhietdo_2.setSizePolicy(sizePolicy5)
        self.pushButton_nhietdo_2.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_nhietdo_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_27.addWidget(self.pushButton_nhietdo_2)

        self.label_nhietdo = QLabel(self.widget_61)
        self.label_nhietdo.setObjectName(u"label_nhietdo")
        self.label_nhietdo.setFont(font4)
        self.label_nhietdo.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_27.addWidget(self.label_nhietdo)


        self.verticalLayout_4.addWidget(self.widget_61)

        self.widget_62 = QWidget(self.widget_49)
        self.widget_62.setObjectName(u"widget_62")
        self.horizontalLayout_28 = QHBoxLayout(self.widget_62)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.pushButton_doam_2 = QPushButton(self.widget_62)
        self.pushButton_doam_2.setObjectName(u"pushButton_doam_2")
        sizePolicy5.setHeightForWidth(self.pushButton_doam_2.sizePolicy().hasHeightForWidth())
        self.pushButton_doam_2.setSizePolicy(sizePolicy5)
        self.pushButton_doam_2.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_28.addWidget(self.pushButton_doam_2)

        self.label_doam_3 = QLabel(self.widget_62)
        self.label_doam_3.setObjectName(u"label_doam_3")
        self.label_doam_3.setFont(font4)
        self.label_doam_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_28.addWidget(self.label_doam_3)


        self.verticalLayout_4.addWidget(self.widget_62)

        self.widget_63 = QWidget(self.widget_49)
        self.widget_63.setObjectName(u"widget_63")
        self.horizontalLayout_29 = QHBoxLayout(self.widget_63)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.pushButton_anhsang_2 = QPushButton(self.widget_63)
        self.pushButton_anhsang_2.setObjectName(u"pushButton_anhsang_2")
        sizePolicy5.setHeightForWidth(self.pushButton_anhsang_2.sizePolicy().hasHeightForWidth())
        self.pushButton_anhsang_2.setSizePolicy(sizePolicy5)
        self.pushButton_anhsang_2.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_29.addWidget(self.pushButton_anhsang_2)

        self.label_anhsang_2 = QLabel(self.widget_63)
        self.label_anhsang_2.setObjectName(u"label_anhsang_2")
        self.label_anhsang_2.setFont(font4)
        self.label_anhsang_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_29.addWidget(self.label_anhsang_2)


        self.verticalLayout_4.addWidget(self.widget_63)

        self.widget_64 = QWidget(self.widget_49)
        self.widget_64.setObjectName(u"widget_64")
        self.horizontalLayout_34 = QHBoxLayout(self.widget_64)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.pushButton_dc1_2 = QPushButton(self.widget_64)
        self.pushButton_dc1_2.setObjectName(u"pushButton_dc1_2")
        sizePolicy5.setHeightForWidth(self.pushButton_dc1_2.sizePolicy().hasHeightForWidth())
        self.pushButton_dc1_2.setSizePolicy(sizePolicy5)
        self.pushButton_dc1_2.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_34.addWidget(self.pushButton_dc1_2)

        self.label_dc1_2 = QLabel(self.widget_64)
        self.label_dc1_2.setObjectName(u"label_dc1_2")
        self.label_dc1_2.setFont(font4)
        self.label_dc1_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_34.addWidget(self.label_dc1_2)


        self.verticalLayout_4.addWidget(self.widget_64)

        self.widget_65 = QWidget(self.widget_49)
        self.widget_65.setObjectName(u"widget_65")
        self.horizontalLayout_35 = QHBoxLayout(self.widget_65)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ac2_2 = QPushButton(self.widget_65)
        self.pushButton_ac2_2.setObjectName(u"pushButton_ac2_2")
        sizePolicy5.setHeightForWidth(self.pushButton_ac2_2.sizePolicy().hasHeightForWidth())
        self.pushButton_ac2_2.setSizePolicy(sizePolicy5)
        self.pushButton_ac2_2.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_35.addWidget(self.pushButton_ac2_2)

        self.label_dc2_2 = QLabel(self.widget_65)
        self.label_dc2_2.setObjectName(u"label_dc2_2")
        self.label_dc2_2.setFont(font4)
        self.label_dc2_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_35.addWidget(self.label_dc2_2)


        self.verticalLayout_4.addWidget(self.widget_65)


        self.horizontalLayout_18.addWidget(self.widget_49)


        self.verticalLayout_35.addWidget(self.widget_36)


        self.horizontalLayout_6.addWidget(self.widget_16)

        self.widget_50 = QWidget(self.lisTram_1)
        self.widget_50.setObjectName(u"widget_50")
        self.verticalLayout_43 = QVBoxLayout(self.widget_50)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.widget_51 = QWidget(self.widget_50)
        self.widget_51.setObjectName(u"widget_51")
        sizePolicy4.setHeightForWidth(self.widget_51.sizePolicy().hasHeightForWidth())
        self.widget_51.setSizePolicy(sizePolicy4)
        self.horizontalLayout_30 = QHBoxLayout(self.widget_51)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.widget_51)
        self.label_17.setObjectName(u"label_17")
        sizePolicy5.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy5)
        self.label_17.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_30.addWidget(self.label_17)


        self.verticalLayout_43.addWidget(self.widget_51)

        self.widget_52 = QWidget(self.widget_50)
        self.widget_52.setObjectName(u"widget_52")
        self.horizontalLayout_31 = QHBoxLayout(self.widget_52)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.widget_53 = QWidget(self.widget_52)
        self.widget_53.setObjectName(u"widget_53")
        self.verticalLayout_44 = QVBoxLayout(self.widget_53)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.widget_55 = QWidget(self.widget_53)
        self.widget_55.setObjectName(u"widget_55")
        self.horizontalLayout_32 = QHBoxLayout(self.widget_55)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.widget_56 = QWidget(self.widget_55)
        self.widget_56.setObjectName(u"widget_56")
        self.verticalLayout_28 = QVBoxLayout(self.widget_56)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.widget_116 = QWidget(self.widget_56)
        self.widget_116.setObjectName(u"widget_116")
        sizePolicy1.setHeightForWidth(self.widget_116.sizePolicy().hasHeightForWidth())
        self.widget_116.setSizePolicy(sizePolicy1)
        self.widget_116.setStyleSheet(u"")
        self.verticalLayout_71 = QVBoxLayout(self.widget_116)
        self.verticalLayout_71.setSpacing(0)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.widget_116)
        self.label_38.setObjectName(u"label_38")
        sizePolicy1.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy1)
        self.label_38.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_38.setPixmap(QPixmap(u":/images/images/images/logo-binh-chung-thong-tin-lien-lac.png"))
        self.label_38.setScaledContents(True)
        self.label_38.setWordWrap(False)
        self.label_38.setMargin(0)
        self.label_38.setOpenExternalLinks(False)

        self.verticalLayout_71.addWidget(self.label_38)

        self.label_46 = QLabel(self.widget_116)
        self.label_46.setObjectName(u"label_46")
        sizePolicy5.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy5)
        self.label_46.setStyleSheet(u"background-position: center;\n"
"background-repeat: no-repeat")
        self.label_46.setAlignment(Qt.AlignCenter)

        self.verticalLayout_71.addWidget(self.label_46)


        self.verticalLayout_28.addWidget(self.widget_116)

        self.widget_117 = QWidget(self.widget_56)
        self.widget_117.setObjectName(u"widget_117")
        sizePolicy4.setHeightForWidth(self.widget_117.sizePolicy().hasHeightForWidth())
        self.widget_117.setSizePolicy(sizePolicy4)
        self.horizontalLayout_62 = QHBoxLayout(self.widget_117)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.widget_118 = QWidget(self.widget_117)
        self.widget_118.setObjectName(u"widget_118")
        self.verticalLayout_72 = QVBoxLayout(self.widget_118)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.widget_119 = QWidget(self.widget_118)
        self.widget_119.setObjectName(u"widget_119")
        self.horizontalLayout_63 = QHBoxLayout(self.widget_119)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ac1_3 = QPushButton(self.widget_119)
        self.pushButton_ac1_3.setObjectName(u"pushButton_ac1_3")
        sizePolicy5.setHeightForWidth(self.pushButton_ac1_3.sizePolicy().hasHeightForWidth())
        self.pushButton_ac1_3.setSizePolicy(sizePolicy5)
        self.pushButton_ac1_3.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_63.addWidget(self.pushButton_ac1_3)


        self.verticalLayout_72.addWidget(self.widget_119)

        self.widget_120 = QWidget(self.widget_118)
        self.widget_120.setObjectName(u"widget_120")
        sizePolicy4.setHeightForWidth(self.widget_120.sizePolicy().hasHeightForWidth())
        self.widget_120.setSizePolicy(sizePolicy4)
        self.verticalLayout_73 = QVBoxLayout(self.widget_120)
        self.verticalLayout_73.setSpacing(0)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.label_47 = QLabel(self.widget_120)
        self.label_47.setObjectName(u"label_47")
        sizePolicy4.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy4)
        self.label_47.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.label_47.setAlignment(Qt.AlignCenter)

        self.verticalLayout_73.addWidget(self.label_47)


        self.verticalLayout_72.addWidget(self.widget_120)


        self.horizontalLayout_62.addWidget(self.widget_118)

        self.widget_121 = QWidget(self.widget_117)
        self.widget_121.setObjectName(u"widget_121")
        sizePolicy4.setHeightForWidth(self.widget_121.sizePolicy().hasHeightForWidth())
        self.widget_121.setSizePolicy(sizePolicy4)
        self.verticalLayout_74 = QVBoxLayout(self.widget_121)
        self.verticalLayout_74.setSpacing(0)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.widget_122 = QWidget(self.widget_121)
        self.widget_122.setObjectName(u"widget_122")
        sizePolicy4.setHeightForWidth(self.widget_122.sizePolicy().hasHeightForWidth())
        self.widget_122.setSizePolicy(sizePolicy4)
        self.horizontalLayout_64 = QHBoxLayout(self.widget_122)
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ac2_3 = QPushButton(self.widget_122)
        self.pushButton_ac2_3.setObjectName(u"pushButton_ac2_3")
        sizePolicy5.setHeightForWidth(self.pushButton_ac2_3.sizePolicy().hasHeightForWidth())
        self.pushButton_ac2_3.setSizePolicy(sizePolicy5)
        self.pushButton_ac2_3.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_64.addWidget(self.pushButton_ac2_3)


        self.verticalLayout_74.addWidget(self.widget_122)

        self.widget_123 = QWidget(self.widget_121)
        self.widget_123.setObjectName(u"widget_123")
        sizePolicy4.setHeightForWidth(self.widget_123.sizePolicy().hasHeightForWidth())
        self.widget_123.setSizePolicy(sizePolicy4)
        self.verticalLayout_75 = QVBoxLayout(self.widget_123)
        self.verticalLayout_75.setSpacing(0)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.label_54 = QLabel(self.widget_123)
        self.label_54.setObjectName(u"label_54")
        sizePolicy4.setHeightForWidth(self.label_54.sizePolicy().hasHeightForWidth())
        self.label_54.setSizePolicy(sizePolicy4)
        self.label_54.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.label_54.setAlignment(Qt.AlignCenter)

        self.verticalLayout_75.addWidget(self.label_54)


        self.verticalLayout_74.addWidget(self.widget_123)


        self.horizontalLayout_62.addWidget(self.widget_121)


        self.verticalLayout_28.addWidget(self.widget_117)


        self.horizontalLayout_32.addWidget(self.widget_56)


        self.verticalLayout_44.addWidget(self.widget_55)


        self.horizontalLayout_31.addWidget(self.widget_53)

        self.widget_71 = QWidget(self.widget_52)
        self.widget_71.setObjectName(u"widget_71")
        self.verticalLayout_33 = QVBoxLayout(self.widget_71)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.widget_54 = QWidget(self.widget_71)
        self.widget_54.setObjectName(u"widget_54")
        self.verticalLayout_16 = QVBoxLayout(self.widget_54)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, 0, 0, 0)
        self.widget_66 = QWidget(self.widget_54)
        self.widget_66.setObjectName(u"widget_66")
        self.horizontalLayout_36 = QHBoxLayout(self.widget_66)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.pushButton_nhietdo_3 = QPushButton(self.widget_66)
        self.pushButton_nhietdo_3.setObjectName(u"pushButton_nhietdo_3")
        sizePolicy5.setHeightForWidth(self.pushButton_nhietdo_3.sizePolicy().hasHeightForWidth())
        self.pushButton_nhietdo_3.setSizePolicy(sizePolicy5)
        self.pushButton_nhietdo_3.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_nhietdo_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_36.addWidget(self.pushButton_nhietdo_3)

        self.label_nhietdo_2 = QLabel(self.widget_66)
        self.label_nhietdo_2.setObjectName(u"label_nhietdo_2")
        self.label_nhietdo_2.setFont(font4)
        self.label_nhietdo_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_36.addWidget(self.label_nhietdo_2)


        self.verticalLayout_16.addWidget(self.widget_66)

        self.widget_67 = QWidget(self.widget_54)
        self.widget_67.setObjectName(u"widget_67")
        self.horizontalLayout_37 = QHBoxLayout(self.widget_67)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.pushButton_doam_3 = QPushButton(self.widget_67)
        self.pushButton_doam_3.setObjectName(u"pushButton_doam_3")
        sizePolicy5.setHeightForWidth(self.pushButton_doam_3.sizePolicy().hasHeightForWidth())
        self.pushButton_doam_3.setSizePolicy(sizePolicy5)
        self.pushButton_doam_3.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_37.addWidget(self.pushButton_doam_3)

        self.label_doam_4 = QLabel(self.widget_67)
        self.label_doam_4.setObjectName(u"label_doam_4")
        self.label_doam_4.setFont(font4)
        self.label_doam_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_37.addWidget(self.label_doam_4)


        self.verticalLayout_16.addWidget(self.widget_67)

        self.widget_68 = QWidget(self.widget_54)
        self.widget_68.setObjectName(u"widget_68")
        self.horizontalLayout_38 = QHBoxLayout(self.widget_68)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.pushButton_anhsang_3 = QPushButton(self.widget_68)
        self.pushButton_anhsang_3.setObjectName(u"pushButton_anhsang_3")
        sizePolicy5.setHeightForWidth(self.pushButton_anhsang_3.sizePolicy().hasHeightForWidth())
        self.pushButton_anhsang_3.setSizePolicy(sizePolicy5)
        self.pushButton_anhsang_3.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_38.addWidget(self.pushButton_anhsang_3)

        self.label_anhsang_3 = QLabel(self.widget_68)
        self.label_anhsang_3.setObjectName(u"label_anhsang_3")
        self.label_anhsang_3.setFont(font4)
        self.label_anhsang_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_38.addWidget(self.label_anhsang_3)


        self.verticalLayout_16.addWidget(self.widget_68)

        self.widget_69 = QWidget(self.widget_54)
        self.widget_69.setObjectName(u"widget_69")
        self.horizontalLayout_39 = QHBoxLayout(self.widget_69)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.pushButton_dc1_3 = QPushButton(self.widget_69)
        self.pushButton_dc1_3.setObjectName(u"pushButton_dc1_3")
        sizePolicy5.setHeightForWidth(self.pushButton_dc1_3.sizePolicy().hasHeightForWidth())
        self.pushButton_dc1_3.setSizePolicy(sizePolicy5)
        self.pushButton_dc1_3.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_39.addWidget(self.pushButton_dc1_3)

        self.label_dc1_3 = QLabel(self.widget_69)
        self.label_dc1_3.setObjectName(u"label_dc1_3")
        self.label_dc1_3.setFont(font4)
        self.label_dc1_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_39.addWidget(self.label_dc1_3)


        self.verticalLayout_16.addWidget(self.widget_69)

        self.widget_70 = QWidget(self.widget_54)
        self.widget_70.setObjectName(u"widget_70")
        self.horizontalLayout_59 = QHBoxLayout(self.widget_70)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.pushButton_dc2_3 = QPushButton(self.widget_70)
        self.pushButton_dc2_3.setObjectName(u"pushButton_dc2_3")
        sizePolicy5.setHeightForWidth(self.pushButton_dc2_3.sizePolicy().hasHeightForWidth())
        self.pushButton_dc2_3.setSizePolicy(sizePolicy5)
        self.pushButton_dc2_3.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_59.addWidget(self.pushButton_dc2_3)

        self.label_dc2_3 = QLabel(self.widget_70)
        self.label_dc2_3.setObjectName(u"label_dc2_3")
        self.label_dc2_3.setFont(font4)
        self.label_dc2_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_59.addWidget(self.label_dc2_3)


        self.verticalLayout_16.addWidget(self.widget_70)


        self.verticalLayout_33.addWidget(self.widget_54)


        self.horizontalLayout_31.addWidget(self.widget_71)


        self.verticalLayout_43.addWidget(self.widget_52)


        self.horizontalLayout_6.addWidget(self.widget_50)


        self.verticalLayout_23.addWidget(self.lisTram_1)

        self.widget_12 = QWidget(self.widget_10)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy)
        self.verticalLayout_25 = QVBoxLayout(self.widget_12)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.widget_14 = QWidget(self.widget_12)
        self.widget_14.setObjectName(u"widget_14")
        sizePolicy.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy)
        self.verticalLayout_52 = QVBoxLayout(self.widget_14)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.widget_75 = QWidget(self.widget_14)
        self.widget_75.setObjectName(u"widget_75")
        sizePolicy.setHeightForWidth(self.widget_75.sizePolicy().hasHeightForWidth())
        self.widget_75.setSizePolicy(sizePolicy)
        self.verticalLayout_51 = QVBoxLayout(self.widget_75)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.widget_77 = QWidget(self.widget_75)
        self.widget_77.setObjectName(u"widget_77")
        self.horizontalLayout_40 = QHBoxLayout(self.widget_77)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, -1, 0, 0)

        self.verticalLayout_51.addWidget(self.widget_77)


        self.verticalLayout_52.addWidget(self.widget_75)


        self.verticalLayout_25.addWidget(self.widget_14)


        self.verticalLayout_23.addWidget(self.widget_12)

        self.listTram_2 = QWidget(self.widget_10)
        self.listTram_2.setObjectName(u"listTram_2")
        self.horizontalLayout_7 = QHBoxLayout(self.listTram_2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, 0)
        self.widget_19 = QWidget(self.listTram_2)
        self.widget_19.setObjectName(u"widget_19")
        self.verticalLayout_59 = QVBoxLayout(self.widget_19)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.widget_108 = QWidget(self.widget_19)
        self.widget_108.setObjectName(u"widget_108")
        sizePolicy4.setHeightForWidth(self.widget_108.sizePolicy().hasHeightForWidth())
        self.widget_108.setSizePolicy(sizePolicy4)
        self.widget_108.setStyleSheet(u"font: 700 16pt \"Segoe UI\";")
        self.horizontalLayout_56 = QHBoxLayout(self.widget_108)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.widget_108)
        self.label_26.setObjectName(u"label_26")
        sizePolicy5.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy5)
        self.label_26.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_56.addWidget(self.label_26)


        self.verticalLayout_59.addWidget(self.widget_108)

        self.widget_109 = QWidget(self.widget_19)
        self.widget_109.setObjectName(u"widget_109")
        self.horizontalLayout_57 = QHBoxLayout(self.widget_109)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.widget_110 = QWidget(self.widget_109)
        self.widget_110.setObjectName(u"widget_110")
        self.verticalLayout_60 = QVBoxLayout(self.widget_110)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.widget_111 = QWidget(self.widget_110)
        self.widget_111.setObjectName(u"widget_111")
        sizePolicy1.setHeightForWidth(self.widget_111.sizePolicy().hasHeightForWidth())
        self.widget_111.setSizePolicy(sizePolicy1)
        self.widget_111.setStyleSheet(u"")
        self.verticalLayout_32 = QVBoxLayout(self.widget_111)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_111)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"")
        self.label_10.setPixmap(QPixmap(u":/images/images/images/logo-binh-chung-thong-tin-lien-lac.png"))
        self.label_10.setScaledContents(True)

        self.verticalLayout_32.addWidget(self.label_10)

        self.label_27 = QLabel(self.widget_111)
        self.label_27.setObjectName(u"label_27")
        sizePolicy5.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy5)
        self.label_27.setStyleSheet(u"background-position: center;\n"
"background-repeat: no-repeat")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_27)


        self.verticalLayout_60.addWidget(self.widget_111)

        self.widget_112 = QWidget(self.widget_110)
        self.widget_112.setObjectName(u"widget_112")
        sizePolicy4.setHeightForWidth(self.widget_112.sizePolicy().hasHeightForWidth())
        self.widget_112.setSizePolicy(sizePolicy4)
        self.horizontalLayout_58 = QHBoxLayout(self.widget_112)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, -1, 0, 0)
        self.widget_113 = QWidget(self.widget_112)
        self.widget_113.setObjectName(u"widget_113")
        self.verticalLayout_61 = QVBoxLayout(self.widget_113)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.widget_114 = QWidget(self.widget_113)
        self.widget_114.setObjectName(u"widget_114")
        self.horizontalLayout_61 = QHBoxLayout(self.widget_114)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ac1_4 = QPushButton(self.widget_114)
        self.pushButton_ac1_4.setObjectName(u"pushButton_ac1_4")
        sizePolicy5.setHeightForWidth(self.pushButton_ac1_4.sizePolicy().hasHeightForWidth())
        self.pushButton_ac1_4.setSizePolicy(sizePolicy5)
        self.pushButton_ac1_4.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"	background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_61.addWidget(self.pushButton_ac1_4)


        self.verticalLayout_61.addWidget(self.widget_114)

        self.widget_115 = QWidget(self.widget_113)
        self.widget_115.setObjectName(u"widget_115")
        self.verticalLayout_62 = QVBoxLayout(self.widget_115)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.widget_115)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_62.addWidget(self.label_28)


        self.verticalLayout_61.addWidget(self.widget_115)


        self.horizontalLayout_58.addWidget(self.widget_113)

        self.widget_138 = QWidget(self.widget_112)
        self.widget_138.setObjectName(u"widget_138")
        self.verticalLayout_63 = QVBoxLayout(self.widget_138)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.widget_139 = QWidget(self.widget_138)
        self.widget_139.setObjectName(u"widget_139")
        self.horizontalLayout_73 = QHBoxLayout(self.widget_139)
        self.horizontalLayout_73.setSpacing(0)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ac2_4 = QPushButton(self.widget_139)
        self.pushButton_ac2_4.setObjectName(u"pushButton_ac2_4")
        sizePolicy5.setHeightForWidth(self.pushButton_ac2_4.sizePolicy().hasHeightForWidth())
        self.pushButton_ac2_4.setSizePolicy(sizePolicy5)
        self.pushButton_ac2_4.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_73.addWidget(self.pushButton_ac2_4)


        self.verticalLayout_63.addWidget(self.widget_139)

        self.widget_140 = QWidget(self.widget_138)
        self.widget_140.setObjectName(u"widget_140")
        self.verticalLayout_64 = QVBoxLayout(self.widget_140)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.widget_140)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_64.addWidget(self.label_29)


        self.verticalLayout_63.addWidget(self.widget_140)


        self.horizontalLayout_58.addWidget(self.widget_138)


        self.verticalLayout_60.addWidget(self.widget_112)


        self.horizontalLayout_57.addWidget(self.widget_110)

        self.widget_141 = QWidget(self.widget_109)
        self.widget_141.setObjectName(u"widget_141")
        self.verticalLayout_24 = QVBoxLayout(self.widget_141)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(-1, 0, -1, 0)
        self.widget_142 = QWidget(self.widget_141)
        self.widget_142.setObjectName(u"widget_142")
        self.horizontalLayout_74 = QHBoxLayout(self.widget_142)
        self.horizontalLayout_74.setSpacing(0)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.pushButton_nhietdo_4 = QPushButton(self.widget_142)
        self.pushButton_nhietdo_4.setObjectName(u"pushButton_nhietdo_4")
        sizePolicy5.setHeightForWidth(self.pushButton_nhietdo_4.sizePolicy().hasHeightForWidth())
        self.pushButton_nhietdo_4.setSizePolicy(sizePolicy5)
        self.pushButton_nhietdo_4.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_nhietdo_4.setIconSize(QSize(20, 20))

        self.horizontalLayout_74.addWidget(self.pushButton_nhietdo_4)

        self.label_nhietdo_6 = QLabel(self.widget_142)
        self.label_nhietdo_6.setObjectName(u"label_nhietdo_6")
        self.label_nhietdo_6.setFont(font4)
        self.label_nhietdo_6.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_74.addWidget(self.label_nhietdo_6)


        self.verticalLayout_24.addWidget(self.widget_142)

        self.widget_143 = QWidget(self.widget_141)
        self.widget_143.setObjectName(u"widget_143")
        self.horizontalLayout_75 = QHBoxLayout(self.widget_143)
        self.horizontalLayout_75.setSpacing(0)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.pushButton_doam_4 = QPushButton(self.widget_143)
        self.pushButton_doam_4.setObjectName(u"pushButton_doam_4")
        sizePolicy5.setHeightForWidth(self.pushButton_doam_4.sizePolicy().hasHeightForWidth())
        self.pushButton_doam_4.setSizePolicy(sizePolicy5)
        self.pushButton_doam_4.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_75.addWidget(self.pushButton_doam_4)

        self.label_doam_5 = QLabel(self.widget_143)
        self.label_doam_5.setObjectName(u"label_doam_5")
        self.label_doam_5.setFont(font4)
        self.label_doam_5.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_75.addWidget(self.label_doam_5)


        self.verticalLayout_24.addWidget(self.widget_143)

        self.widget_144 = QWidget(self.widget_141)
        self.widget_144.setObjectName(u"widget_144")
        self.horizontalLayout_76 = QHBoxLayout(self.widget_144)
        self.horizontalLayout_76.setSpacing(0)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.pushButton_anhsang_4 = QPushButton(self.widget_144)
        self.pushButton_anhsang_4.setObjectName(u"pushButton_anhsang_4")
        sizePolicy5.setHeightForWidth(self.pushButton_anhsang_4.sizePolicy().hasHeightForWidth())
        self.pushButton_anhsang_4.setSizePolicy(sizePolicy5)
        self.pushButton_anhsang_4.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_76.addWidget(self.pushButton_anhsang_4)

        self.label_anhsang_4 = QLabel(self.widget_144)
        self.label_anhsang_4.setObjectName(u"label_anhsang_4")
        self.label_anhsang_4.setFont(font4)
        self.label_anhsang_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_76.addWidget(self.label_anhsang_4)


        self.verticalLayout_24.addWidget(self.widget_144)

        self.widget_145 = QWidget(self.widget_141)
        self.widget_145.setObjectName(u"widget_145")
        self.horizontalLayout_77 = QHBoxLayout(self.widget_145)
        self.horizontalLayout_77.setSpacing(0)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.pushButton_dc1_4 = QPushButton(self.widget_145)
        self.pushButton_dc1_4.setObjectName(u"pushButton_dc1_4")
        sizePolicy5.setHeightForWidth(self.pushButton_dc1_4.sizePolicy().hasHeightForWidth())
        self.pushButton_dc1_4.setSizePolicy(sizePolicy5)
        self.pushButton_dc1_4.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_77.addWidget(self.pushButton_dc1_4)

        self.label_dc1_4 = QLabel(self.widget_145)
        self.label_dc1_4.setObjectName(u"label_dc1_4")
        self.label_dc1_4.setFont(font4)
        self.label_dc1_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_77.addWidget(self.label_dc1_4)


        self.verticalLayout_24.addWidget(self.widget_145)

        self.widget_146 = QWidget(self.widget_141)
        self.widget_146.setObjectName(u"widget_146")
        self.horizontalLayout_78 = QHBoxLayout(self.widget_146)
        self.horizontalLayout_78.setSpacing(0)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.pushButton_dc2_4 = QPushButton(self.widget_146)
        self.pushButton_dc2_4.setObjectName(u"pushButton_dc2_4")
        sizePolicy5.setHeightForWidth(self.pushButton_dc2_4.sizePolicy().hasHeightForWidth())
        self.pushButton_dc2_4.setSizePolicy(sizePolicy5)
        self.pushButton_dc2_4.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_78.addWidget(self.pushButton_dc2_4)

        self.label_dc2_4 = QLabel(self.widget_146)
        self.label_dc2_4.setObjectName(u"label_dc2_4")
        self.label_dc2_4.setFont(font4)
        self.label_dc2_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_78.addWidget(self.label_dc2_4)


        self.verticalLayout_24.addWidget(self.widget_146)


        self.horizontalLayout_57.addWidget(self.widget_141)


        self.verticalLayout_59.addWidget(self.widget_109)


        self.horizontalLayout_7.addWidget(self.widget_19)

        self.widget_18 = QWidget(self.listTram_2)
        self.widget_18.setObjectName(u"widget_18")
        self.verticalLayout_49 = QVBoxLayout(self.widget_18)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.widget_78 = QWidget(self.widget_18)
        self.widget_78.setObjectName(u"widget_78")
        sizePolicy4.setHeightForWidth(self.widget_78.sizePolicy().hasHeightForWidth())
        self.widget_78.setSizePolicy(sizePolicy4)
        self.widget_78.setStyleSheet(u"font: 700 16pt \"Segoe UI\";")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_78)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.widget_78)
        self.label_21.setObjectName(u"label_21")
        sizePolicy5.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy5)
        self.label_21.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_24.addWidget(self.label_21)


        self.verticalLayout_49.addWidget(self.widget_78)

        self.widget_79 = QWidget(self.widget_18)
        self.widget_79.setObjectName(u"widget_79")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_79)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.widget_80 = QWidget(self.widget_79)
        self.widget_80.setObjectName(u"widget_80")
        self.verticalLayout_50 = QVBoxLayout(self.widget_80)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.widget_81 = QWidget(self.widget_80)
        self.widget_81.setObjectName(u"widget_81")
        sizePolicy1.setHeightForWidth(self.widget_81.sizePolicy().hasHeightForWidth())
        self.widget_81.setSizePolicy(sizePolicy1)
        self.widget_81.setStyleSheet(u"")
        self.verticalLayout_30 = QVBoxLayout(self.widget_81)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget_81)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"")
        self.label_9.setPixmap(QPixmap(u":/images/images/images/logo-binh-chung-thong-tin-lien-lac.png"))
        self.label_9.setScaledContents(True)

        self.verticalLayout_30.addWidget(self.label_9)

        self.label_22 = QLabel(self.widget_81)
        self.label_22.setObjectName(u"label_22")
        sizePolicy5.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy5)
        self.label_22.setStyleSheet(u"background-position: center;\n"
"background-repeat: no-repeat")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_22)


        self.verticalLayout_50.addWidget(self.widget_81)

        self.widget_82 = QWidget(self.widget_80)
        self.widget_82.setObjectName(u"widget_82")
        sizePolicy4.setHeightForWidth(self.widget_82.sizePolicy().hasHeightForWidth())
        self.widget_82.setSizePolicy(sizePolicy4)
        self.horizontalLayout_41 = QHBoxLayout(self.widget_82)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, -1, 0, 0)
        self.widget_83 = QWidget(self.widget_82)
        self.widget_83.setObjectName(u"widget_83")
        self.verticalLayout_53 = QVBoxLayout(self.widget_83)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.widget_84 = QWidget(self.widget_83)
        self.widget_84.setObjectName(u"widget_84")
        self.horizontalLayout_42 = QHBoxLayout(self.widget_84)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ac1_5 = QPushButton(self.widget_84)
        self.pushButton_ac1_5.setObjectName(u"pushButton_ac1_5")
        sizePolicy5.setHeightForWidth(self.pushButton_ac1_5.sizePolicy().hasHeightForWidth())
        self.pushButton_ac1_5.setSizePolicy(sizePolicy5)
        self.pushButton_ac1_5.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"	background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_42.addWidget(self.pushButton_ac1_5)


        self.verticalLayout_53.addWidget(self.widget_84)

        self.widget_85 = QWidget(self.widget_83)
        self.widget_85.setObjectName(u"widget_85")
        self.verticalLayout_54 = QVBoxLayout(self.widget_85)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.widget_85)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.label_23)


        self.verticalLayout_53.addWidget(self.widget_85)


        self.horizontalLayout_41.addWidget(self.widget_83)

        self.widget_86 = QWidget(self.widget_82)
        self.widget_86.setObjectName(u"widget_86")
        self.verticalLayout_55 = QVBoxLayout(self.widget_86)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.widget_87 = QWidget(self.widget_86)
        self.widget_87.setObjectName(u"widget_87")
        self.horizontalLayout_43 = QHBoxLayout(self.widget_87)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ac2_5 = QPushButton(self.widget_87)
        self.pushButton_ac2_5.setObjectName(u"pushButton_ac2_5")
        sizePolicy5.setHeightForWidth(self.pushButton_ac2_5.sizePolicy().hasHeightForWidth())
        self.pushButton_ac2_5.setSizePolicy(sizePolicy5)
        self.pushButton_ac2_5.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_43.addWidget(self.pushButton_ac2_5)


        self.verticalLayout_55.addWidget(self.widget_87)

        self.widget_88 = QWidget(self.widget_86)
        self.widget_88.setObjectName(u"widget_88")
        self.verticalLayout_56 = QVBoxLayout(self.widget_88)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.widget_88)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_56.addWidget(self.label_24)


        self.verticalLayout_55.addWidget(self.widget_88)


        self.horizontalLayout_41.addWidget(self.widget_86)


        self.verticalLayout_50.addWidget(self.widget_82)


        self.horizontalLayout_26.addWidget(self.widget_80)

        self.widget_89 = QWidget(self.widget_79)
        self.widget_89.setObjectName(u"widget_89")
        self.verticalLayout_18 = QVBoxLayout(self.widget_89)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(-1, 0, -1, 0)
        self.widget_90 = QWidget(self.widget_89)
        self.widget_90.setObjectName(u"widget_90")
        self.horizontalLayout_44 = QHBoxLayout(self.widget_90)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.pushButton_nhietdo_5 = QPushButton(self.widget_90)
        self.pushButton_nhietdo_5.setObjectName(u"pushButton_nhietdo_5")
        sizePolicy5.setHeightForWidth(self.pushButton_nhietdo_5.sizePolicy().hasHeightForWidth())
        self.pushButton_nhietdo_5.setSizePolicy(sizePolicy5)
        self.pushButton_nhietdo_5.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_nhietdo_5.setIconSize(QSize(20, 20))

        self.horizontalLayout_44.addWidget(self.pushButton_nhietdo_5)

        self.label_nhietdo_4 = QLabel(self.widget_90)
        self.label_nhietdo_4.setObjectName(u"label_nhietdo_4")
        self.label_nhietdo_4.setFont(font4)
        self.label_nhietdo_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_44.addWidget(self.label_nhietdo_4)


        self.verticalLayout_18.addWidget(self.widget_90)

        self.widget_91 = QWidget(self.widget_89)
        self.widget_91.setObjectName(u"widget_91")
        self.horizontalLayout_45 = QHBoxLayout(self.widget_91)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.pushButton_doam_5 = QPushButton(self.widget_91)
        self.pushButton_doam_5.setObjectName(u"pushButton_doam_5")
        sizePolicy5.setHeightForWidth(self.pushButton_doam_5.sizePolicy().hasHeightForWidth())
        self.pushButton_doam_5.setSizePolicy(sizePolicy5)
        self.pushButton_doam_5.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_45.addWidget(self.pushButton_doam_5)

        self.label_doam_6 = QLabel(self.widget_91)
        self.label_doam_6.setObjectName(u"label_doam_6")
        self.label_doam_6.setFont(font4)
        self.label_doam_6.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_45.addWidget(self.label_doam_6)


        self.verticalLayout_18.addWidget(self.widget_91)

        self.widget_92 = QWidget(self.widget_89)
        self.widget_92.setObjectName(u"widget_92")
        self.horizontalLayout_46 = QHBoxLayout(self.widget_92)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.pushButton_anhsang_5 = QPushButton(self.widget_92)
        self.pushButton_anhsang_5.setObjectName(u"pushButton_anhsang_5")
        sizePolicy5.setHeightForWidth(self.pushButton_anhsang_5.sizePolicy().hasHeightForWidth())
        self.pushButton_anhsang_5.setSizePolicy(sizePolicy5)
        self.pushButton_anhsang_5.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_46.addWidget(self.pushButton_anhsang_5)

        self.label_anhsang_5 = QLabel(self.widget_92)
        self.label_anhsang_5.setObjectName(u"label_anhsang_5")
        self.label_anhsang_5.setFont(font4)
        self.label_anhsang_5.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_46.addWidget(self.label_anhsang_5)


        self.verticalLayout_18.addWidget(self.widget_92)

        self.widget_93 = QWidget(self.widget_89)
        self.widget_93.setObjectName(u"widget_93")
        self.horizontalLayout_47 = QHBoxLayout(self.widget_93)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.pushButton_dc1_5 = QPushButton(self.widget_93)
        self.pushButton_dc1_5.setObjectName(u"pushButton_dc1_5")
        sizePolicy5.setHeightForWidth(self.pushButton_dc1_5.sizePolicy().hasHeightForWidth())
        self.pushButton_dc1_5.setSizePolicy(sizePolicy5)
        self.pushButton_dc1_5.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_47.addWidget(self.pushButton_dc1_5)

        self.label_dc1_5 = QLabel(self.widget_93)
        self.label_dc1_5.setObjectName(u"label_dc1_5")
        self.label_dc1_5.setFont(font4)
        self.label_dc1_5.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_47.addWidget(self.label_dc1_5)


        self.verticalLayout_18.addWidget(self.widget_93)

        self.widget_94 = QWidget(self.widget_89)
        self.widget_94.setObjectName(u"widget_94")
        self.horizontalLayout_48 = QHBoxLayout(self.widget_94)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.pushButton_dc2_5 = QPushButton(self.widget_94)
        self.pushButton_dc2_5.setObjectName(u"pushButton_dc2_5")
        sizePolicy5.setHeightForWidth(self.pushButton_dc2_5.sizePolicy().hasHeightForWidth())
        self.pushButton_dc2_5.setSizePolicy(sizePolicy5)
        self.pushButton_dc2_5.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_48.addWidget(self.pushButton_dc2_5)

        self.label_dc2_5 = QLabel(self.widget_94)
        self.label_dc2_5.setObjectName(u"label_dc2_5")
        self.label_dc2_5.setFont(font4)
        self.label_dc2_5.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_48.addWidget(self.label_dc2_5)


        self.verticalLayout_18.addWidget(self.widget_94)


        self.horizontalLayout_26.addWidget(self.widget_89)


        self.verticalLayout_49.addWidget(self.widget_79)


        self.horizontalLayout_7.addWidget(self.widget_18)

        self.widget_95 = QWidget(self.listTram_2)
        self.widget_95.setObjectName(u"widget_95")
        self.verticalLayout_57 = QVBoxLayout(self.widget_95)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.widget_96 = QWidget(self.widget_95)
        self.widget_96.setObjectName(u"widget_96")
        sizePolicy4.setHeightForWidth(self.widget_96.sizePolicy().hasHeightForWidth())
        self.widget_96.setSizePolicy(sizePolicy4)
        self.horizontalLayout_49 = QHBoxLayout(self.widget_96)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.widget_96)
        self.label_25.setObjectName(u"label_25")
        sizePolicy5.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy5)
        self.label_25.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_49.addWidget(self.label_25)


        self.verticalLayout_57.addWidget(self.widget_96)

        self.widget_97 = QWidget(self.widget_95)
        self.widget_97.setObjectName(u"widget_97")
        self.horizontalLayout_50 = QHBoxLayout(self.widget_97)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.widget_98 = QWidget(self.widget_97)
        self.widget_98.setObjectName(u"widget_98")
        self.verticalLayout_58 = QVBoxLayout(self.widget_98)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.widget_99 = QWidget(self.widget_98)
        self.widget_99.setObjectName(u"widget_99")
        self.horizontalLayout_51 = QHBoxLayout(self.widget_99)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.widget_100 = QWidget(self.widget_99)
        self.widget_100.setObjectName(u"widget_100")
        self.verticalLayout_31 = QVBoxLayout(self.widget_100)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.widget_130 = QWidget(self.widget_100)
        self.widget_130.setObjectName(u"widget_130")
        sizePolicy1.setHeightForWidth(self.widget_130.sizePolicy().hasHeightForWidth())
        self.widget_130.setSizePolicy(sizePolicy1)
        self.widget_130.setStyleSheet(u"")
        self.verticalLayout_76 = QVBoxLayout(self.widget_130)
        self.verticalLayout_76.setSpacing(0)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.widget_130)
        self.label_39.setObjectName(u"label_39")
        sizePolicy1.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy1)
        self.label_39.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_39.setPixmap(QPixmap(u":/images/images/images/logo-binh-chung-thong-tin-lien-lac.png"))
        self.label_39.setScaledContents(True)
        self.label_39.setWordWrap(False)
        self.label_39.setMargin(0)
        self.label_39.setOpenExternalLinks(False)

        self.verticalLayout_76.addWidget(self.label_39)

        self.label_55 = QLabel(self.widget_130)
        self.label_55.setObjectName(u"label_55")
        sizePolicy5.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy5)
        self.label_55.setStyleSheet(u"background-position: center;\n"
"background-repeat: no-repeat")
        self.label_55.setAlignment(Qt.AlignCenter)

        self.verticalLayout_76.addWidget(self.label_55)


        self.verticalLayout_31.addWidget(self.widget_130)

        self.widget_131 = QWidget(self.widget_100)
        self.widget_131.setObjectName(u"widget_131")
        sizePolicy4.setHeightForWidth(self.widget_131.sizePolicy().hasHeightForWidth())
        self.widget_131.setSizePolicy(sizePolicy4)
        self.horizontalLayout_70 = QHBoxLayout(self.widget_131)
        self.horizontalLayout_70.setSpacing(0)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.widget_132 = QWidget(self.widget_131)
        self.widget_132.setObjectName(u"widget_132")
        self.verticalLayout_77 = QVBoxLayout(self.widget_132)
        self.verticalLayout_77.setSpacing(0)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.widget_133 = QWidget(self.widget_132)
        self.widget_133.setObjectName(u"widget_133")
        self.horizontalLayout_71 = QHBoxLayout(self.widget_133)
        self.horizontalLayout_71.setSpacing(0)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ac1_6 = QPushButton(self.widget_133)
        self.pushButton_ac1_6.setObjectName(u"pushButton_ac1_6")
        sizePolicy5.setHeightForWidth(self.pushButton_ac1_6.sizePolicy().hasHeightForWidth())
        self.pushButton_ac1_6.setSizePolicy(sizePolicy5)
        self.pushButton_ac1_6.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_71.addWidget(self.pushButton_ac1_6)


        self.verticalLayout_77.addWidget(self.widget_133)

        self.widget_134 = QWidget(self.widget_132)
        self.widget_134.setObjectName(u"widget_134")
        sizePolicy4.setHeightForWidth(self.widget_134.sizePolicy().hasHeightForWidth())
        self.widget_134.setSizePolicy(sizePolicy4)
        self.verticalLayout_78 = QVBoxLayout(self.widget_134)
        self.verticalLayout_78.setSpacing(0)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.label_56 = QLabel(self.widget_134)
        self.label_56.setObjectName(u"label_56")
        sizePolicy4.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy4)
        self.label_56.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.label_56.setAlignment(Qt.AlignCenter)

        self.verticalLayout_78.addWidget(self.label_56)


        self.verticalLayout_77.addWidget(self.widget_134)


        self.horizontalLayout_70.addWidget(self.widget_132)

        self.widget_135 = QWidget(self.widget_131)
        self.widget_135.setObjectName(u"widget_135")
        sizePolicy4.setHeightForWidth(self.widget_135.sizePolicy().hasHeightForWidth())
        self.widget_135.setSizePolicy(sizePolicy4)
        self.verticalLayout_79 = QVBoxLayout(self.widget_135)
        self.verticalLayout_79.setSpacing(0)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.widget_136 = QWidget(self.widget_135)
        self.widget_136.setObjectName(u"widget_136")
        sizePolicy4.setHeightForWidth(self.widget_136.sizePolicy().hasHeightForWidth())
        self.widget_136.setSizePolicy(sizePolicy4)
        self.horizontalLayout_72 = QHBoxLayout(self.widget_136)
        self.horizontalLayout_72.setSpacing(0)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.pushButton_ac2_6 = QPushButton(self.widget_136)
        self.pushButton_ac2_6.setObjectName(u"pushButton_ac2_6")
        sizePolicy5.setHeightForWidth(self.pushButton_ac2_6.sizePolicy().hasHeightForWidth())
        self.pushButton_ac2_6.setSizePolicy(sizePolicy5)
        self.pushButton_ac2_6.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_72.addWidget(self.pushButton_ac2_6)


        self.verticalLayout_79.addWidget(self.widget_136)

        self.widget_137 = QWidget(self.widget_135)
        self.widget_137.setObjectName(u"widget_137")
        sizePolicy4.setHeightForWidth(self.widget_137.sizePolicy().hasHeightForWidth())
        self.widget_137.setSizePolicy(sizePolicy4)
        self.verticalLayout_80 = QVBoxLayout(self.widget_137)
        self.verticalLayout_80.setSpacing(0)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.verticalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.label_57 = QLabel(self.widget_137)
        self.label_57.setObjectName(u"label_57")
        sizePolicy4.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy4)
        self.label_57.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.label_57.setAlignment(Qt.AlignCenter)

        self.verticalLayout_80.addWidget(self.label_57)


        self.verticalLayout_79.addWidget(self.widget_137)


        self.horizontalLayout_70.addWidget(self.widget_135)


        self.verticalLayout_31.addWidget(self.widget_131)


        self.horizontalLayout_51.addWidget(self.widget_100)


        self.verticalLayout_58.addWidget(self.widget_99)


        self.horizontalLayout_50.addWidget(self.widget_98)

        self.widget_101 = QWidget(self.widget_97)
        self.widget_101.setObjectName(u"widget_101")
        self.verticalLayout_26 = QVBoxLayout(self.widget_101)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.widget_102 = QWidget(self.widget_101)
        self.widget_102.setObjectName(u"widget_102")
        self.verticalLayout_21 = QVBoxLayout(self.widget_102)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.widget_103 = QWidget(self.widget_102)
        self.widget_103.setObjectName(u"widget_103")
        self.horizontalLayout_52 = QHBoxLayout(self.widget_103)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.pushButton_nhietdo_6 = QPushButton(self.widget_103)
        self.pushButton_nhietdo_6.setObjectName(u"pushButton_nhietdo_6")
        sizePolicy5.setHeightForWidth(self.pushButton_nhietdo_6.sizePolicy().hasHeightForWidth())
        self.pushButton_nhietdo_6.setSizePolicy(sizePolicy5)
        self.pushButton_nhietdo_6.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_nhietdo_6.setIconSize(QSize(20, 20))

        self.horizontalLayout_52.addWidget(self.pushButton_nhietdo_6)

        self.label_nhietdo_5 = QLabel(self.widget_103)
        self.label_nhietdo_5.setObjectName(u"label_nhietdo_5")
        self.label_nhietdo_5.setFont(font4)
        self.label_nhietdo_5.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_52.addWidget(self.label_nhietdo_5)


        self.verticalLayout_21.addWidget(self.widget_103)

        self.widget_104 = QWidget(self.widget_102)
        self.widget_104.setObjectName(u"widget_104")
        self.horizontalLayout_53 = QHBoxLayout(self.widget_104)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.pushButton_doam_6 = QPushButton(self.widget_104)
        self.pushButton_doam_6.setObjectName(u"pushButton_doam_6")
        sizePolicy5.setHeightForWidth(self.pushButton_doam_6.sizePolicy().hasHeightForWidth())
        self.pushButton_doam_6.setSizePolicy(sizePolicy5)
        self.pushButton_doam_6.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_53.addWidget(self.pushButton_doam_6)

        self.label_doam_7 = QLabel(self.widget_104)
        self.label_doam_7.setObjectName(u"label_doam_7")
        self.label_doam_7.setFont(font4)
        self.label_doam_7.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_53.addWidget(self.label_doam_7)


        self.verticalLayout_21.addWidget(self.widget_104)

        self.widget_105 = QWidget(self.widget_102)
        self.widget_105.setObjectName(u"widget_105")
        self.horizontalLayout_54 = QHBoxLayout(self.widget_105)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.pushButton_anhsang_6 = QPushButton(self.widget_105)
        self.pushButton_anhsang_6.setObjectName(u"pushButton_anhsang_6")
        sizePolicy5.setHeightForWidth(self.pushButton_anhsang_6.sizePolicy().hasHeightForWidth())
        self.pushButton_anhsang_6.setSizePolicy(sizePolicy5)
        self.pushButton_anhsang_6.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_54.addWidget(self.pushButton_anhsang_6)

        self.label_anhsang_6 = QLabel(self.widget_105)
        self.label_anhsang_6.setObjectName(u"label_anhsang_6")
        self.label_anhsang_6.setFont(font4)
        self.label_anhsang_6.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_54.addWidget(self.label_anhsang_6)


        self.verticalLayout_21.addWidget(self.widget_105)

        self.widget_106 = QWidget(self.widget_102)
        self.widget_106.setObjectName(u"widget_106")
        self.horizontalLayout_55 = QHBoxLayout(self.widget_106)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.pushButton_dc1_6 = QPushButton(self.widget_106)
        self.pushButton_dc1_6.setObjectName(u"pushButton_dc1_6")
        sizePolicy5.setHeightForWidth(self.pushButton_dc1_6.sizePolicy().hasHeightForWidth())
        self.pushButton_dc1_6.setSizePolicy(sizePolicy5)
        self.pushButton_dc1_6.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_55.addWidget(self.pushButton_dc1_6)

        self.label_dc1_6 = QLabel(self.widget_106)
        self.label_dc1_6.setObjectName(u"label_dc1_6")
        self.label_dc1_6.setFont(font4)
        self.label_dc1_6.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_55.addWidget(self.label_dc1_6)


        self.verticalLayout_21.addWidget(self.widget_106)

        self.widget_107 = QWidget(self.widget_102)
        self.widget_107.setObjectName(u"widget_107")
        self.horizontalLayout_60 = QHBoxLayout(self.widget_107)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.pushButton_dc2_6 = QPushButton(self.widget_107)
        self.pushButton_dc2_6.setObjectName(u"pushButton_dc2_6")
        sizePolicy5.setHeightForWidth(self.pushButton_dc2_6.sizePolicy().hasHeightForWidth())
        self.pushButton_dc2_6.setSizePolicy(sizePolicy5)
        self.pushButton_dc2_6.setStyleSheet(u"\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_60.addWidget(self.pushButton_dc2_6)

        self.label_dc2_6 = QLabel(self.widget_107)
        self.label_dc2_6.setObjectName(u"label_dc2_6")
        self.label_dc2_6.setFont(font4)
        self.label_dc2_6.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_60.addWidget(self.label_dc2_6)


        self.verticalLayout_21.addWidget(self.widget_107)


        self.verticalLayout_26.addWidget(self.widget_102)


        self.horizontalLayout_50.addWidget(self.widget_101)


        self.verticalLayout_57.addWidget(self.widget_97)


        self.horizontalLayout_7.addWidget(self.widget_95)


        self.verticalLayout_23.addWidget(self.listTram_2)


        self.verticalLayout_19.addWidget(self.widget_10)


        self.gridLayout.addWidget(self.widget_8, 0, 0, 1, 1)

        self.label_3 = QLabel(self.home)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"Segoe UI\";")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.widget = QWidget(self.widgets)
        self.widget.setObjectName(u"widget")

        self.verticalLayout.addWidget(self.widget)

        self.stackedWidget.addWidget(self.widgets)
        self.Nhietdo = QWidget()
        self.Nhietdo.setObjectName(u"Nhietdo")
        self.verticalLayout_34 = QVBoxLayout(self.Nhietdo)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.Nhietdo_widget = QWidget(self.Nhietdo)
        self.Nhietdo_widget.setObjectName(u"Nhietdo_widget")
        self.Nhietdo_widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_65 = QVBoxLayout(self.Nhietdo_widget)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.title_nhietdo = QLabel(self.Nhietdo_widget)
        self.title_nhietdo.setObjectName(u"title_nhietdo")
        sizePolicy4.setHeightForWidth(self.title_nhietdo.sizePolicy().hasHeightForWidth())
        self.title_nhietdo.setSizePolicy(sizePolicy4)
        self.title_nhietdo.setStyleSheet(u"\n"
"font: 700 20pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.title_nhietdo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_65.addWidget(self.title_nhietdo)

        self.thoigian_nhietdo = QLabel(self.Nhietdo_widget)
        self.thoigian_nhietdo.setObjectName(u"thoigian_nhietdo")
        sizePolicy4.setHeightForWidth(self.thoigian_nhietdo.sizePolicy().hasHeightForWidth())
        self.thoigian_nhietdo.setSizePolicy(sizePolicy4)
        self.thoigian_nhietdo.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.thoigian_nhietdo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_65.addWidget(self.thoigian_nhietdo)

        self.screen_nhietdo = QVBoxLayout()
        self.screen_nhietdo.setSpacing(0)
        self.screen_nhietdo.setObjectName(u"screen_nhietdo")
        self.screen_nhietdo.setSizeConstraint(QLayout.SetMaximumSize)
        self.screen_nhietdo.setContentsMargins(-1, -1, -1, 0)

        self.verticalLayout_65.addLayout(self.screen_nhietdo)


        self.verticalLayout_34.addWidget(self.Nhietdo_widget)

        self.stackedWidget.addWidget(self.Nhietdo)
        self.Doam = QWidget()
        self.Doam.setObjectName(u"Doam")
        self.Doam.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_68 = QVBoxLayout(self.Doam)
        self.verticalLayout_68.setSpacing(0)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.widget_Doam = QWidget(self.Doam)
        self.widget_Doam.setObjectName(u"widget_Doam")
        self.widget_Doam.setStyleSheet(u"")
        self.verticalLayout_66 = QVBoxLayout(self.widget_Doam)
        self.verticalLayout_66.setSpacing(0)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.widget_label_doam = QWidget(self.widget_Doam)
        self.widget_label_doam.setObjectName(u"widget_label_doam")
        sizePolicy1.setHeightForWidth(self.widget_label_doam.sizePolicy().hasHeightForWidth())
        self.widget_label_doam.setSizePolicy(sizePolicy1)
        self.widget_label_doam.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.widget_label_doam.setStyleSheet(u"border-color: rgb(0, 170, 255);")
        self.verticalLayout_67 = QVBoxLayout(self.widget_label_doam)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.label_doam = QLabel(self.widget_label_doam)
        self.label_doam.setObjectName(u"label_doam")
        sizePolicy4.setHeightForWidth(self.label_doam.sizePolicy().hasHeightForWidth())
        self.label_doam.setSizePolicy(sizePolicy4)
        self.label_doam.setStyleSheet(u"\n"
"font: 700 20pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_doam.setAlignment(Qt.AlignCenter)

        self.verticalLayout_67.addWidget(self.label_doam)

        self.label_thoigian_doam = QLabel(self.widget_label_doam)
        self.label_thoigian_doam.setObjectName(u"label_thoigian_doam")
        sizePolicy4.setHeightForWidth(self.label_thoigian_doam.sizePolicy().hasHeightForWidth())
        self.label_thoigian_doam.setSizePolicy(sizePolicy4)
        self.label_thoigian_doam.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_thoigian_doam.setAlignment(Qt.AlignCenter)

        self.verticalLayout_67.addWidget(self.label_thoigian_doam)

        self.screen_doam = QVBoxLayout()
        self.screen_doam.setSpacing(0)
        self.screen_doam.setObjectName(u"screen_doam")
        self.screen_doam.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout_67.addLayout(self.screen_doam)


        self.verticalLayout_66.addWidget(self.widget_label_doam)


        self.verticalLayout_68.addWidget(self.widget_Doam)

        self.stackedWidget.addWidget(self.Doam)
        self.Ludoan_506 = QWidget()
        self.Ludoan_506.setObjectName(u"Ludoan_506")
        self.verticalLayout_20 = QVBoxLayout(self.Ludoan_506)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label = QLabel(self.Ludoan_506)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label)

        self.stackedWidget.addWidget(self.Ludoan_506)
        self.Dienap = QWidget()
        self.Dienap.setObjectName(u"Dienap")
        self.verticalLayout_81 = QVBoxLayout(self.Dienap)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.widget_Dienap = QWidget(self.Dienap)
        self.widget_Dienap.setObjectName(u"widget_Dienap")
        self.widget_Dienap.setStyleSheet(u"")
        self.verticalLayout_69 = QVBoxLayout(self.widget_Dienap)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.widget_label_dienap = QWidget(self.widget_Dienap)
        self.widget_label_dienap.setObjectName(u"widget_label_dienap")
        sizePolicy1.setHeightForWidth(self.widget_label_dienap.sizePolicy().hasHeightForWidth())
        self.widget_label_dienap.setSizePolicy(sizePolicy1)
        self.widget_label_dienap.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.widget_label_dienap.setStyleSheet(u"border-color: rgb(0, 170, 255);")
        self.verticalLayout_70 = QVBoxLayout(self.widget_label_dienap)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.label_diepap = QLabel(self.widget_label_dienap)
        self.label_diepap.setObjectName(u"label_diepap")
        sizePolicy4.setHeightForWidth(self.label_diepap.sizePolicy().hasHeightForWidth())
        self.label_diepap.setSizePolicy(sizePolicy4)
        self.label_diepap.setStyleSheet(u"\n"
"font: 700 20pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_diepap.setAlignment(Qt.AlignCenter)

        self.verticalLayout_70.addWidget(self.label_diepap)

        self.label_thoigian_dienap = QLabel(self.widget_label_dienap)
        self.label_thoigian_dienap.setObjectName(u"label_thoigian_dienap")
        sizePolicy4.setHeightForWidth(self.label_thoigian_dienap.sizePolicy().hasHeightForWidth())
        self.label_thoigian_dienap.setSizePolicy(sizePolicy4)
        self.label_thoigian_dienap.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_thoigian_dienap.setAlignment(Qt.AlignCenter)

        self.verticalLayout_70.addWidget(self.label_thoigian_dienap)

        self.screen_dienap = QVBoxLayout()
        self.screen_dienap.setSpacing(0)
        self.screen_dienap.setObjectName(u"screen_dienap")
        self.screen_dienap.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout_70.addLayout(self.screen_dienap)


        self.verticalLayout_69.addWidget(self.widget_label_dienap)


        self.verticalLayout_81.addWidget(self.widget_Dienap)

        self.stackedWidget.addWidget(self.Dienap)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_lu139.setText(QCoreApplication.translate("MainWindow", u"L\u1eef \u0111o\u00e0n 139", None))
        self.btn_lu205.setText(QCoreApplication.translate("MainWindow", u"L\u1eef \u0111o\u00e0n 205", None))
        self.btn_lu132.setText(QCoreApplication.translate("MainWindow", u"L\u1eef \u0111o\u00e0n 132", None))
        self.btn_lu596.setText(QCoreApplication.translate("MainWindow", u"L\u1eef \u0111o\u00e0n 596", None))
        self.btn_ip.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-inde"
                        "nt:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" "
                        "style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"H\u1eccC VI\u1ec6N K\u1ef8 THU\u1eacT QU\u00c2N S\u1ef0", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"H\u1ec6 TH\u1ed0NG QU\u1ea2N L\u00dd TR\u1ea0M TH\u00d4NG TIN", None))
        self.label_2.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"TR\u1ea0M A01", None))
        self.label_8.setText("")
        self.label_18.setText("")
        self.pushButton_ac1.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Ngu\u1ed3n AC1", None))
        self.pushButton_ac2.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Ngu\u1ed3n AC2", None))
        self.pushButton_nhietdo.setText("")
        self.label_nhietdo_3.setText(QCoreApplication.translate("MainWindow", u"Nhi\u1ec7t \u0111\u1ed9 : ", None))
        self.pushButton_doam.setText("")
        self.label_doam_2.setText(QCoreApplication.translate("MainWindow", u" \u0110\u1ed9 \u1ea9m :", None))
        self.pushButton_anhsang.setText("")
        self.label_anhsang.setText(QCoreApplication.translate("MainWindow", u" \u00c1nh s\u00e1ng :", None))
        self.pushButton_dc1.setText("")
        self.label_dc1.setText(QCoreApplication.translate("MainWindow", u" Ngu\u1ed3n DC1 :", None))
        self.pushButton_dc2.setText("")
        self.label_dc2.setText(QCoreApplication.translate("MainWindow", u" Ngu\u1ed3n DC2 :", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"TR\u1ea0M A70", None))
        self.label_7.setText("")
        self.label_13.setText("")
        self.pushButton_ac1_2.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Ngu\u1ed3n AC1", None))
        self.pushButton_dc2_8.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Ngu\u1ed3n AC2", None))
        self.pushButton_nhietdo_2.setText("")
        self.label_nhietdo.setText(QCoreApplication.translate("MainWindow", u"Nhi\u1ec7t \u0111\u1ed9 : ", None))
        self.pushButton_doam_2.setText("")
        self.label_doam_3.setText(QCoreApplication.translate("MainWindow", u" \u0110\u1ed9 \u1ea9m :", None))
        self.pushButton_anhsang_2.setText("")
        self.label_anhsang_2.setText(QCoreApplication.translate("MainWindow", u" \u00c1nh s\u00e1ng :", None))
        self.pushButton_dc1_2.setText("")
        self.label_dc1_2.setText(QCoreApplication.translate("MainWindow", u" Ngu\u1ed3n DC1 :", None))
        self.pushButton_ac2_2.setText("")
        self.label_dc2_2.setText(QCoreApplication.translate("MainWindow", u" Ngu\u1ed3n DC2 :", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"TR\u1ea0M A45", None))
        self.label_38.setText("")
        self.label_46.setText("")
        self.pushButton_ac1_3.setText("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Ngu\u1ed3n AC1", None))
        self.pushButton_ac2_3.setText("")
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Ngu\u1ed3n AC2", None))
        self.pushButton_nhietdo_3.setText("")
        self.label_nhietdo_2.setText(QCoreApplication.translate("MainWindow", u"Nhi\u1ec7t \u0111\u1ed9 : ", None))
        self.pushButton_doam_3.setText("")
        self.label_doam_4.setText(QCoreApplication.translate("MainWindow", u" \u0110\u1ed9 \u1ea9m :", None))
        self.pushButton_anhsang_3.setText("")
        self.label_anhsang_3.setText(QCoreApplication.translate("MainWindow", u" \u00c1nh s\u00e1ng :", None))
        self.pushButton_dc1_3.setText("")
        self.label_dc1_3.setText(QCoreApplication.translate("MainWindow", u" Ngu\u1ed3n DC1 :", None))
        self.pushButton_dc2_3.setText("")
        self.label_dc2_3.setText(QCoreApplication.translate("MainWindow", u" Ngu\u1ed3n DC2 :", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"TR\u1ea0M A48", None))
        self.label_10.setText("")
        self.label_27.setText("")
        self.pushButton_ac1_4.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Ngu\u1ed3n AC1", None))
        self.pushButton_ac2_4.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Ngu\u1ed3n AC2", None))
        self.pushButton_nhietdo_4.setText("")
        self.label_nhietdo_6.setText(QCoreApplication.translate("MainWindow", u"Nhi\u1ec7t \u0111\u1ed9 : ", None))
        self.pushButton_doam_4.setText("")
        self.label_doam_5.setText(QCoreApplication.translate("MainWindow", u" \u0110\u1ed9 \u1ea9m :", None))
        self.pushButton_anhsang_4.setText("")
        self.label_anhsang_4.setText(QCoreApplication.translate("MainWindow", u" \u00c1nh s\u00e1ng :", None))
        self.pushButton_dc1_4.setText("")
        self.label_dc1_4.setText(QCoreApplication.translate("MainWindow", u" Ngu\u1ed3n DC1 :", None))
        self.pushButton_dc2_4.setText("")
        self.label_dc2_4.setText(QCoreApplication.translate("MainWindow", u" Ngu\u1ed3n DC2 :", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u" TR\u1ea0M A171", None))
        self.label_9.setText("")
        self.label_22.setText("")
        self.pushButton_ac1_5.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Ngu\u1ed3n AC1", None))
        self.pushButton_ac2_5.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Ngu\u1ed3n AC2", None))
        self.pushButton_nhietdo_5.setText("")
        self.label_nhietdo_4.setText(QCoreApplication.translate("MainWindow", u"Nhi\u1ec7t \u0111\u1ed9 : ", None))
        self.pushButton_doam_5.setText("")
        self.label_doam_6.setText(QCoreApplication.translate("MainWindow", u" \u0110\u1ed9 \u1ea9m :", None))
        self.pushButton_anhsang_5.setText("")
        self.label_anhsang_5.setText(QCoreApplication.translate("MainWindow", u" \u00c1nh s\u00e1ng :", None))
        self.pushButton_dc1_5.setText("")
        self.label_dc1_5.setText(QCoreApplication.translate("MainWindow", u" Ngu\u1ed3n DC1 :", None))
        self.pushButton_dc2_5.setText("")
        self.label_dc2_5.setText(QCoreApplication.translate("MainWindow", u" Ngu\u1ed3n DC2 :", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"TR\u1ea0M A78", None))
        self.label_39.setText("")
        self.label_55.setText("")
        self.pushButton_ac1_6.setText("")
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Ngu\u1ed3n AC1", None))
        self.pushButton_ac2_6.setText("")
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Ngu\u1ed3n AC2", None))
        self.pushButton_nhietdo_6.setText("")
        self.label_nhietdo_5.setText(QCoreApplication.translate("MainWindow", u"Nhi\u1ec7t \u0111\u1ed9 : ", None))
        self.pushButton_doam_6.setText("")
        self.label_doam_7.setText(QCoreApplication.translate("MainWindow", u" \u0110\u1ed9 \u1ea9m :", None))
        self.pushButton_anhsang_6.setText("")
        self.label_anhsang_6.setText(QCoreApplication.translate("MainWindow", u" \u00c1nh s\u00e1ng :", None))
        self.pushButton_dc1_6.setText("")
        self.label_dc1_6.setText(QCoreApplication.translate("MainWindow", u" Ngu\u1ed3n DC1 :", None))
        self.pushButton_dc2_6.setText("")
        self.label_dc2_6.setText(QCoreApplication.translate("MainWindow", u" Ngu\u1ed3n DC2 :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"L\u1eef \u0111o\u00e0n 139", None))
        self.title_nhietdo.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3u \u0111\u1ed3 nhi\u1ec7t \u0111\u1ed9", None))
        self.thoigian_nhietdo.setText("")
        self.label_doam.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3u \u0111\u1ed3 \u0111\u1ed9 \u1ea9m", None))
        self.label_thoigian_doam.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"NEW PAGE TEST", None))
        self.label_diepap.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3u \u0111\u1ed3 \u0110i\u1ec7n \u00e1p", None))
        self.label_thoigian_dienap.setText("")
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Wanderson M. Pimenta", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi

