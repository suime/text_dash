# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Chart.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLayout,
    QSizePolicy, QTabWidget, QToolBox, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(720, 461)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.option = QVBoxLayout()
        self.option.setObjectName(u"option")
        self.option.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.toolBox = QToolBox(Form)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 341, 367))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_2 = QGroupBox(self.page)
        self.groupBox_2.setObjectName(u"groupBox_2")

        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.page)
        self.groupBox_3.setObjectName(u"groupBox_3")

        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.groupBox_5 = QGroupBox(self.page)
        self.groupBox_5.setObjectName(u"groupBox_5")

        self.verticalLayout_4.addWidget(self.groupBox_5)

        self.toolBox.addItem(self.page, u"\ud544\ud130")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 341, 367))
        self.verticalLayout_3 = QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.page_2)
        self.groupBox.setObjectName(u"groupBox")

        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_4 = QGroupBox(self.page_2)
        self.groupBox_4.setObjectName(u"groupBox_4")

        self.verticalLayout_3.addWidget(self.groupBox_4)

        self.toolBox.addItem(self.page_2, u"\ucc28\ud2b8 \uc635\uc158")

        self.option.addWidget(self.toolBox)


        self.horizontalLayout.addLayout(self.option)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_time = QWidget()
        self.tab_time.setObjectName(u"tab_time")
        self.verticalLayout_2 = QVBoxLayout(self.tab_time)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_6 = QGroupBox(self.tab_time)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.webEngineView = QWebEngineView(self.groupBox_6)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_5.addWidget(self.webEngineView)


        self.verticalLayout_2.addWidget(self.groupBox_6)

        self.tabWidget.addTab(self.tab_time, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.HelpAbout))
        self.tabWidget.addTab(self.tab_2, icon, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        self.toolBox.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\uae30\uac04 \ud544\ud130", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\ud14d\uc2a4\ud2b8 \ud544\ud130", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"\ubd84\ub958 \ud544\ud130", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("Form", u"\ud544\ud130", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("Form", u"\ucc28\ud2b8 \uc635\uc158", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Form", u"\ucc28\ud2b8", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_time), QCoreApplication.translate("Form", u"\uc2dc\uacc4\uc5f4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\ubd84\ud3ec", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\ucabd", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\ucabd", None))
    # retranslateUi

