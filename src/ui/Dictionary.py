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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_Chart(object):
    def setupUi(self, Chart):
        if not Chart.objectName():
            Chart.setObjectName(u"Chart")
        Chart.resize(872, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Chart.sizePolicy().hasHeightForWidth())
        Chart.setSizePolicy(sizePolicy)
        Chart.setMinimumSize(QSize(600, 600))
        Chart.setMaximumSize(QSize(16777215, 16777215))
        Chart.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(Chart)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QGroupBox(Chart)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setMinimumSize(QSize(300, 0))
        self.sidebar.setMaximumSize(QSize(300, 16777215))
        self.option = QVBoxLayout(self.sidebar)
        self.option.setSpacing(0)
        self.option.setObjectName(u"option")
        self.option.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.tabWidget = QTabWidget(self.sidebar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(300, 0))
        self.tabWidget.setMaximumSize(QSize(300, 16777215))
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidgetPage1 = QWidget()
        self.tabWidgetPage1.setObjectName(u"tabWidgetPage1")
        self.verticalLayout_4 = QVBoxLayout(self.tabWidgetPage1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.groupBox_2 = QGroupBox(self.tabWidgetPage1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 3, -1, -1)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.Label = QLabel(self.groupBox_2)
        self.Label.setObjectName(u"Label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.Label)

        self.LineEdit = QLineEdit(self.groupBox_2)
        self.LineEdit.setObjectName(u"LineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.LineEdit)

        self.Label_2 = QLabel(self.groupBox_2)
        self.Label_2.setObjectName(u"Label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.Label_2)

        self.DateEdit = QDateEdit(self.groupBox_2)
        self.DateEdit.setObjectName(u"DateEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.DateEdit)


        self.verticalLayout_7.addLayout(self.formLayout)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.tabWidgetPage1)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 0))
        self.groupBox_3.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 3, -1, -1)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.Label_3 = QLabel(self.groupBox_3)
        self.Label_3.setObjectName(u"Label_3")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.Label_3)

        self.LineEdit_2 = QLineEdit(self.groupBox_3)
        self.LineEdit_2.setObjectName(u"LineEdit_2")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.LineEdit_2)

        self.Label_6 = QLabel(self.groupBox_3)
        self.Label_6.setObjectName(u"Label_6")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.Label_6)

        self.LineEdit_4 = QLineEdit(self.groupBox_3)
        self.LineEdit_4.setObjectName(u"LineEdit_4")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.LineEdit_4)


        self.verticalLayout_6.addLayout(self.formLayout_2)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.groupBox_5 = QGroupBox(self.tabWidgetPage1)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(0, 0))
        self.groupBox_5.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 3, -1, -1)
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.Label_4 = QLabel(self.groupBox_5)
        self.Label_4.setObjectName(u"Label_4")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.Label_4)

        self.ComboBox = QComboBox(self.groupBox_5)
        self.ComboBox.setObjectName(u"ComboBox")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.ComboBox)

        self.Label_5 = QLabel(self.groupBox_5)
        self.Label_5.setObjectName(u"Label_5")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.Label_5)

        self.ComboBox_2 = QComboBox(self.groupBox_5)
        self.ComboBox_2.setObjectName(u"ComboBox_2")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.ComboBox_2)

        self.Label_7 = QLabel(self.groupBox_5)
        self.Label_7.setObjectName(u"Label_7")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.Label_7)

        self.ComboBox_3 = QComboBox(self.groupBox_5)
        self.ComboBox_3.setObjectName(u"ComboBox_3")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.ComboBox_3)


        self.verticalLayout_5.addLayout(self.formLayout_3)


        self.verticalLayout_4.addWidget(self.groupBox_5)

        self.pushButton_2 = QPushButton(self.tabWidgetPage1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 14, 14);")

        self.verticalLayout_4.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.tabWidgetPage1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: rgb(0, 111, 255);")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)

        self.verticalLayout_4.addWidget(self.pushButton)

        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QWidget()
        self.tabWidgetPage2.setObjectName(u"tabWidgetPage2")
        self.verticalLayout_3 = QVBoxLayout(self.tabWidgetPage2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")

        self.verticalLayout_3.addLayout(self.formLayout_4)

        self.RefreshChart = QPushButton(self.tabWidgetPage2)
        self.RefreshChart.setObjectName(u"RefreshChart")

        self.verticalLayout_3.addWidget(self.RefreshChart)

        self.tabWidget.addTab(self.tabWidgetPage2, "")

        self.option.addWidget(self.tabWidget)


        self.horizontalLayout.addWidget(self.sidebar)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.tabWidget1 = QTabWidget(Chart)
        self.tabWidget1.setObjectName(u"tabWidget1")
        self.tabWidget1.setMinimumSize(QSize(600, 0))
        self.tabWidget1.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget1.setUsesScrollButtons(False)
        self.tabWidget1.setDocumentMode(True)
        self.tabWidget1.setTabsClosable(False)
        self.tabWidget1.setTabBarAutoHide(False)
        self.tab_time = QWidget()
        self.tab_time.setObjectName(u"tab_time")
        self.tab_time.setMinimumSize(QSize(300, 0))
        self.verticalLayout_2 = QVBoxLayout(self.tab_time)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Linechart = QWebEngineView(self.tab_time)
        self.Linechart.setObjectName(u"Linechart")
        self.Linechart.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_2.addWidget(self.Linechart)

        self.tabWidget1.addTab(self.tab_time, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setMinimumSize(QSize(300, 0))
        self.tabWidget1.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setMinimumSize(QSize(300, 0))
        self.tabWidget1.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setMinimumSize(QSize(300, 0))
        self.tabWidget1.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget1)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Chart)

        self.tabWidget.setCurrentIndex(0)
        self.pushButton.setDefault(False)
        self.tabWidget1.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Chart)
    # setupUi

    def retranslateUi(self, Chart):
        Chart.setWindowTitle(QCoreApplication.translate("Chart", u"Form", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Chart", u"\uae30\uac04 \ud544\ud130", None))
        self.Label.setText(QCoreApplication.translate("Chart", u"\uae30\uac04 \uc870\uc815", None))
        self.Label_2.setText(QCoreApplication.translate("Chart", u"\ub0a0\uc9dc \uc870\uc815", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Chart", u"\ud14d\uc2a4\ud2b8 \ud544\ud130", None))
        self.Label_3.setText(QCoreApplication.translate("Chart", u"\ud3ec\ud568\ud560 \ub2e8\uc5b4", None))
        self.Label_6.setText(QCoreApplication.translate("Chart", u"\uc81c\uc678\ud560 \ub2e8\uc5b4", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Chart", u"\ubd84\ub958 \ud544\ud130", None))
        self.Label_4.setText(QCoreApplication.translate("Chart", u"\ub300\ubd84\ub958 :", None))
        self.Label_5.setText(QCoreApplication.translate("Chart", u"\uc911\ubd84\ub958 :", None))
        self.Label_7.setText(QCoreApplication.translate("Chart", u"\uc18c\ubd84\ub958 :", None))
        self.pushButton_2.setText(QCoreApplication.translate("Chart", u"\ud544\ud130 \ucd08\uae30\ud654", None))
        self.pushButton.setText(QCoreApplication.translate("Chart", u"\ud544\ud130 \uc801\uc6a9\ud558\uae30", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), QCoreApplication.translate("Chart", u"\ub370\uc774\ud130 \ud544\ud130", None))
        self.RefreshChart.setText(QCoreApplication.translate("Chart", u"\ucc28\ud2b8 \uc0c8\ub85c\uace0\uce68", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), QCoreApplication.translate("Chart", u"\ucc28\ud2b8 \uc635\uc158", None))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.tab_time), QCoreApplication.translate("Chart", u"\uc2dc\uacc4\uc5f4", None))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.tab_2), QCoreApplication.translate("Chart", u"\ubd84\ud3ec", None))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.tab), QCoreApplication.translate("Chart", u"\ubc14", None))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.tab_3), QCoreApplication.translate("Chart", u"\uc774\ub7f0 \uc800\ub7f0 \ucc28\ud2b8 ", None))
    # retranslateUi

