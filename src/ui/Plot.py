# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Plot.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFontComboBox,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpinBox, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_Plot(object):
    def setupUi(self, Plot):
        if not Plot.objectName():
            Plot.setObjectName(u"Plot")
        Plot.resize(988, 612)
        self.horizontalLayout = QHBoxLayout(Plot)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.tabWidget = QTabWidget(Plot)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(300, 0))
        self.tabWidget.setMaximumSize(QSize(310, 16777215))
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.tabWidgetPage1 = QWidget()
        self.tabWidgetPage1.setObjectName(u"tabWidgetPage1")
        self.verticalLayout_3 = QVBoxLayout(self.tabWidgetPage1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_4 = QGroupBox(self.tabWidgetPage1)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 3, -1, -1)
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setRowWrapPolicy(QFormLayout.RowWrapPolicy.DontWrapRows)
        self.formLayout_4.setHorizontalSpacing(4)
        self.formLayout_4.setVerticalSpacing(4)
        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)

        self.formLayout_4.setWidget(0, QFormLayout.SpanningRole, self.label)

        self.Label_8 = QLabel(self.groupBox_4)
        self.Label_8.setObjectName(u"Label_8")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.Label_8)

        self.startDate = QDateEdit(self.groupBox_4)
        self.startDate.setObjectName(u"startDate")
        self.startDate.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.startDate.setProperty("showGroupSeparator", True)
        self.startDate.setDateTime(QDateTime(QDate(2024, 7, 1), QTime(9, 0, 0)))
        self.startDate.setMaximumDate(QDate(9994, 1, 11))
        self.startDate.setCalendarPopup(True)
        self.startDate.setTimeSpec(Qt.TimeSpec.LocalTime)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.startDate)

        self.Label = QLabel(self.groupBox_4)
        self.Label.setObjectName(u"Label")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.Label)

        self.endDate = QDateEdit(self.groupBox_4)
        self.endDate.setObjectName(u"endDate")
        self.endDate.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.endDate.setDateTime(QDateTime(QDate(2024, 7, 1), QTime(9, 0, 0)))
        self.endDate.setCalendarPopup(True)
        self.endDate.setTimeSpec(Qt.TimeSpec.LocalTime)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.endDate)


        self.verticalLayout_10.addLayout(self.formLayout_4)


        self.verticalLayout_3.addWidget(self.groupBox_4)

        self.groupBox_6 = QGroupBox(self.tabWidgetPage1)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(0, 0))
        self.groupBox_6.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Label_9 = QLabel(self.groupBox_6)
        self.Label_9.setObjectName(u"Label_9")

        self.verticalLayout_5.addWidget(self.Label_9)

        self.inText = QPlainTextEdit(self.groupBox_6)
        self.inText.setObjectName(u"inText")
        self.inText.setFrameShadow(QFrame.Shadow.Sunken)
        self.inText.setTabChangesFocus(True)

        self.verticalLayout_5.addWidget(self.inText)

        self.Label_10 = QLabel(self.groupBox_6)
        self.Label_10.setObjectName(u"Label_10")

        self.verticalLayout_5.addWidget(self.Label_10)

        self.exText = QPlainTextEdit(self.groupBox_6)
        self.exText.setObjectName(u"exText")
        self.exText.setTabChangesFocus(True)

        self.verticalLayout_5.addWidget(self.exText)


        self.verticalLayout_3.addWidget(self.groupBox_6)

        self.groupBox_5 = QGroupBox(self.tabWidgetPage1)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(0, 0))
        self.groupBox_5.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 3, -1, -1)
        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.Label_6 = QLabel(self.groupBox_5)
        self.Label_6.setObjectName(u"Label_6")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.Label_6)

        self.category1 = QComboBox(self.groupBox_5)
        self.category1.addItem("")
        self.category1.setObjectName(u"category1")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.category1)

        self.Label_12 = QLabel(self.groupBox_5)
        self.Label_12.setObjectName(u"Label_12")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.Label_12)

        self.category2 = QComboBox(self.groupBox_5)
        self.category2.addItem("")
        self.category2.setObjectName(u"category2")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.category2)

        self.Label_13 = QLabel(self.groupBox_5)
        self.Label_13.setObjectName(u"Label_13")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.Label_13)

        self.category3 = QComboBox(self.groupBox_5)
        self.category3.addItem("")
        self.category3.setObjectName(u"category3")

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.category3)


        self.verticalLayout_6.addLayout(self.formLayout_6)


        self.verticalLayout_3.addWidget(self.groupBox_5)

        self.resetFilter = QPushButton(self.tabWidgetPage1)
        self.resetFilter.setObjectName(u"resetFilter")
        self.resetFilter.setStyleSheet(u"background-color: #990011;\n"
"color: #FCF6F5;\n"
"font-weight: bold;\n"
"border-radius: 0.3em;\n"
"height: 20px;")

        self.verticalLayout_3.addWidget(self.resetFilter)

        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QWidget()
        self.tabWidgetPage2.setObjectName(u"tabWidgetPage2")
        self.verticalLayout_14 = QVBoxLayout(self.tabWidgetPage2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.groupBox = QGroupBox(self.tabWidgetPage2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 100))
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_2.addWidget(self.label_4)

        self.text_title = QLineEdit(self.groupBox)
        self.text_title.setObjectName(u"text_title")

        self.verticalLayout_2.addWidget(self.text_title)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_2.addWidget(self.label_5)

        self.text_sub = QLineEdit(self.groupBox)
        self.text_sub.setObjectName(u"text_sub")

        self.verticalLayout_2.addWidget(self.text_sub)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_2.addWidget(self.label_7)

        self.text_unit = QLineEdit(self.groupBox)
        self.text_unit.setObjectName(u"text_unit")

        self.verticalLayout_2.addWidget(self.text_unit)


        self.verticalLayout_14.addWidget(self.groupBox)

        self.designBox = QGroupBox(self.tabWidgetPage2)
        self.designBox.setObjectName(u"designBox")
        self.gridLayout_2 = QGridLayout(self.designBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.fontComboBox = QFontComboBox(self.designBox)
        self.fontComboBox.setObjectName(u"fontComboBox")

        self.gridLayout_2.addWidget(self.fontComboBox, 0, 1, 1, 1)

        self.label_3 = QLabel(self.designBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.bg = QLabel(self.designBox)
        self.bg.setObjectName(u"bg")

        self.gridLayout_2.addWidget(self.bg, 4, 0, 1, 1)

        self.bgcolorPicker = QPushButton(self.designBox)
        self.bgcolorPicker.setObjectName(u"bgcolorPicker")
        self.bgcolorPicker.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.bgcolorPicker, 4, 1, 1, 1)

        self.label_2 = QLabel(self.designBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(16777215, 300))

        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)

        self.colorPicker = QPushButton(self.designBox)
        self.colorPicker.setObjectName(u"colorPicker")
        self.colorPicker.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(117, 117, 117);")

        self.gridLayout_2.addWidget(self.colorPicker, 3, 1, 1, 1)

        self.label_6 = QLabel(self.designBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)

        self.minFontSize = QSpinBox(self.designBox)
        self.minFontSize.setObjectName(u"minFontSize")
        self.minFontSize.setMinimum(5)
        self.minFontSize.setMaximum(48)
        self.minFontSize.setValue(12)

        self.gridLayout_2.addWidget(self.minFontSize, 5, 1, 1, 1)


        self.verticalLayout_14.addWidget(self.designBox)

        self.resetOption = QPushButton(self.tabWidgetPage2)
        self.resetOption.setObjectName(u"resetOption")
        self.resetOption.setStyleSheet(u"background-color: #990011;\n"
"color: #FCF6F5;\n"
"font-weight: bold;\n"
"border-radius: 0.3em;\n"
"height: 20px;")

        self.verticalLayout_14.addWidget(self.resetOption)

        self.verticalLayout_14.setStretch(1, 1)
        self.tabWidget.addTab(self.tabWidgetPage2, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget_2 = QTabWidget(Plot)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setDocumentMode(False)
        self.tabWidget_2.setMovable(True)
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.verticalLayout_4 = QVBoxLayout(self.tab1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.qtTreemap = QWebEngineView(self.tab1)
        self.qtTreemap.setObjectName(u"qtTreemap")
        self.qtTreemap.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_4.addWidget(self.qtTreemap)

        self.initTreemap = QPushButton(self.tab1)
        self.initTreemap.setObjectName(u"initTreemap")
        self.initTreemap.setStyleSheet(u"background-color: #1e90ff;\n"
"height: 24px;\n"
"border-radius: 0.5em;\n"
"font-size: 13px;\n"
"font-weight: bold;\n"
"color: #ffffff;")

        self.verticalLayout_4.addWidget(self.initTreemap)

        self.saveWC = QPushButton(self.tab1)
        self.saveWC.setObjectName(u"saveWC")
        self.saveWC.setStyleSheet(u"background-color: rgb(249, 87, 0);\n"
"height: 24px;\n"
"border-radius: 0.5em;\n"
"font-size: 13px;\n"
"font-weight: bold;\n"
"color: #ffffff;")

        self.verticalLayout_4.addWidget(self.saveWC)

        self.tabWidget_2.addTab(self.tab1, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.verticalLayout_7 = QVBoxLayout(self.tab2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.qtPie = QWebEngineView(self.tab2)
        self.qtPie.setObjectName(u"qtPie")
        self.qtPie.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_7.addWidget(self.qtPie)

        self.initPie = QPushButton(self.tab2)
        self.initPie.setObjectName(u"initPie")
        self.initPie.setStyleSheet(u"background-color: #1e90ff;\n"
"height: 24px;\n"
"border-radius: 0.5em;\n"
"font-size: 13px;\n"
"font-weight: bold;\n"
"color: #ffffff;")

        self.verticalLayout_7.addWidget(self.initPie)

        self.saveWC_2 = QPushButton(self.tab2)
        self.saveWC_2.setObjectName(u"saveWC_2")
        self.saveWC_2.setStyleSheet(u"background-color: rgb(249, 87, 0);\n"
"height: 24px;\n"
"border-radius: 0.5em;\n"
"font-size: 13px;\n"
"font-weight: bold;\n"
"color: #ffffff;")

        self.verticalLayout_7.addWidget(self.saveWC_2)

        self.tabWidget_2.addTab(self.tab2, "")
        self.tab3 = QWidget()
        self.tab3.setObjectName(u"tab3")
        self.verticalLayout_8 = QVBoxLayout(self.tab3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.qtHbar = QWebEngineView(self.tab3)
        self.qtHbar.setObjectName(u"qtHbar")
        self.qtHbar.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_8.addWidget(self.qtHbar)

        self.initHbar = QPushButton(self.tab3)
        self.initHbar.setObjectName(u"initHbar")
        self.initHbar.setStyleSheet(u"background-color: #1e90ff;\n"
"height: 24px;\n"
"border-radius: 0.5em;\n"
"font-size: 13px;\n"
"font-weight: bold;\n"
"color: #ffffff;")

        self.verticalLayout_8.addWidget(self.initHbar)

        self.saveWC_3 = QPushButton(self.tab3)
        self.saveWC_3.setObjectName(u"saveWC_3")
        self.saveWC_3.setStyleSheet(u"background-color: rgb(249, 87, 0);\n"
"height: 24px;\n"
"border-radius: 0.5em;\n"
"font-size: 13px;\n"
"font-weight: bold;\n"
"color: #ffffff;")

        self.verticalLayout_8.addWidget(self.saveWC_3)

        self.tabWidget_2.addTab(self.tab3, "")
        self.tab4 = QWidget()
        self.tab4.setObjectName(u"tab4")
        self.verticalLayout_9 = QVBoxLayout(self.tab4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.qtLine = QWebEngineView(self.tab4)
        self.qtLine.setObjectName(u"qtLine")
        self.qtLine.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_9.addWidget(self.qtLine)

        self.initLine = QPushButton(self.tab4)
        self.initLine.setObjectName(u"initLine")
        self.initLine.setStyleSheet(u"background-color: #1e90ff;\n"
"height: 24px;\n"
"border-radius: 0.5em;\n"
"font-size: 13px;\n"
"font-weight: bold;\n"
"color: #ffffff;")

        self.verticalLayout_9.addWidget(self.initLine)

        self.saveWC_4 = QPushButton(self.tab4)
        self.saveWC_4.setObjectName(u"saveWC_4")
        self.saveWC_4.setStyleSheet(u"background-color: rgb(249, 87, 0);\n"
"height: 24px;\n"
"border-radius: 0.5em;\n"
"font-size: 13px;\n"
"font-weight: bold;\n"
"color: #ffffff;")

        self.verticalLayout_9.addWidget(self.saveWC_4)

        self.tabWidget_2.addTab(self.tab4, "")
        self.tab5 = QWidget()
        self.tab5.setObjectName(u"tab5")
        self.verticalLayout_11 = QVBoxLayout(self.tab5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.qtBar = QWebEngineView(self.tab5)
        self.qtBar.setObjectName(u"qtBar")
        self.qtBar.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_11.addWidget(self.qtBar)

        self.initBar = QPushButton(self.tab5)
        self.initBar.setObjectName(u"initBar")
        self.initBar.setStyleSheet(u"background-color: #1e90ff;\n"
"height: 24px;\n"
"border-radius: 0.5em;\n"
"font-size: 13px;\n"
"font-weight: bold;\n"
"color: #ffffff;")

        self.verticalLayout_11.addWidget(self.initBar)

        self.saveWC_5 = QPushButton(self.tab5)
        self.saveWC_5.setObjectName(u"saveWC_5")
        self.saveWC_5.setStyleSheet(u"background-color: rgb(249, 87, 0);\n"
"height: 24px;\n"
"border-radius: 0.5em;\n"
"font-size: 13px;\n"
"font-weight: bold;\n"
"color: #ffffff;")

        self.verticalLayout_11.addWidget(self.saveWC_5)

        self.tabWidget_2.addTab(self.tab5, "")
        self.tab6 = QWidget()
        self.tab6.setObjectName(u"tab6")
        self.verticalLayout_12 = QVBoxLayout(self.tab6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.qtSankey = QWebEngineView(self.tab6)
        self.qtSankey.setObjectName(u"qtSankey")
        self.qtSankey.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_12.addWidget(self.qtSankey)

        self.initSankey = QPushButton(self.tab6)
        self.initSankey.setObjectName(u"initSankey")
        self.initSankey.setStyleSheet(u"background-color: #1e90ff;\n"
"height: 24px;\n"
"border-radius: 0.5em;\n"
"font-size: 13px;\n"
"font-weight: bold;\n"
"color: #ffffff;")

        self.verticalLayout_12.addWidget(self.initSankey)

        self.saveWC_6 = QPushButton(self.tab6)
        self.saveWC_6.setObjectName(u"saveWC_6")
        self.saveWC_6.setStyleSheet(u"background-color: rgb(249, 87, 0);\n"
"height: 24px;\n"
"border-radius: 0.5em;\n"
"font-size: 13px;\n"
"font-weight: bold;\n"
"color: #ffffff;")

        self.verticalLayout_12.addWidget(self.saveWC_6)

        self.tabWidget_2.addTab(self.tab6, "")
        self.tab_stat = QWidget()
        self.tab_stat.setObjectName(u"tab_stat")
        self.verticalLayout_13 = QVBoxLayout(self.tab_stat)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.qtStat = QWebEngineView(self.tab_stat)
        self.qtStat.setObjectName(u"qtStat")
        self.qtStat.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_13.addWidget(self.qtStat)

        self.initStat = QPushButton(self.tab_stat)
        self.initStat.setObjectName(u"initStat")
        self.initStat.setStyleSheet(u"background-color: #1e90ff;\n"
"height: 24px;\n"
"border-radius: 0.5em;\n"
"font-size: 13px;\n"
"font-weight: bold;\n"
"color: #ffffff;")

        self.verticalLayout_13.addWidget(self.initStat)

        self.saveWC_7 = QPushButton(self.tab_stat)
        self.saveWC_7.setObjectName(u"saveWC_7")
        self.saveWC_7.setStyleSheet(u"background-color: rgb(249, 87, 0);\n"
"height: 24px;\n"
"border-radius: 0.5em;\n"
"font-size: 13px;\n"
"font-weight: bold;\n"
"color: #ffffff;")

        self.verticalLayout_13.addWidget(self.saveWC_7)

        self.tabWidget_2.addTab(self.tab_stat, "")

        self.verticalLayout.addWidget(self.tabWidget_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Plot)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Plot)
    # setupUi

    def retranslateUi(self, Plot):
        Plot.setWindowTitle(QCoreApplication.translate("Plot", u"Form", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Plot", u"\uae30\uac04 \ud544\ud130", None))
        self.label.setText(QCoreApplication.translate("Plot", u"\ub370\uc774\ud130 \ubc94\uc704 \uc124\uc815", None))
        self.Label_8.setText(QCoreApplication.translate("Plot", u"\uc2dc\uc791\uc77c :", None))
        self.Label.setText(QCoreApplication.translate("Plot", u"\uc885\ub8cc\uc77c :", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Plot", u"\ud14d\uc2a4\ud2b8 \ud544\ud130", None))
        self.Label_9.setText(QCoreApplication.translate("Plot", u"\ud3ec\ud568\ud560 \ub2e8\uc5b4", None))
        self.inText.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.Label_10.setToolTip(QCoreApplication.translate("Plot", u"<html><head/><body><p>\ud45c\uc5d0\uc11c \uc81c\uc678\ud560 \ud14d\uc2a4\ud2b8\ub97c \uc27c\ud45c\ub098, \uc904\ubc14\uafc8\uc73c\ub85c \uad6c\ubd84\ud574\uc11c \uc791\uc131\ud558\uc138\uc694</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Label_10.setText(QCoreApplication.translate("Plot", u"\uc81c\uc678\ud560 \ub2e8\uc5b4", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Plot", u"\ubd84\ub958 \ud544\ud130", None))
        self.Label_6.setText(QCoreApplication.translate("Plot", u"\ub300\ubd84\ub958 :", None))
        self.category1.setItemText(0, QCoreApplication.translate("Plot", u"\ubbf8\uc124\uc815", None))

        self.category1.setPlaceholderText(QCoreApplication.translate("Plot", u"\ubbf8\uc124\uc815", None))
        self.Label_12.setText(QCoreApplication.translate("Plot", u"\uc911\ubd84\ub958 :", None))
        self.category2.setItemText(0, QCoreApplication.translate("Plot", u"\ubbf8\uc124\uc815", None))

        self.category2.setPlaceholderText(QCoreApplication.translate("Plot", u"\ubbf8\uc124\uc815", None))
        self.Label_13.setText(QCoreApplication.translate("Plot", u"\uc18c\ubd84\ub958 :", None))
        self.category3.setItemText(0, QCoreApplication.translate("Plot", u"\ubbf8\uc124\uc815", None))

        self.category3.setPlaceholderText(QCoreApplication.translate("Plot", u"\ubbf8\uc124\uc815", None))
        self.resetFilter.setText(QCoreApplication.translate("Plot", u"\ud544\ud130 \ucd08\uae30\ud654", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), QCoreApplication.translate("Plot", u"\ub370\uc774\ud130 \ud544\ud130", None))
        self.groupBox.setTitle(QCoreApplication.translate("Plot", u"\ud14d\uc2a4\ud2b8 \uc635\uc158", None))
        self.label_4.setText(QCoreApplication.translate("Plot", u"\ucc28\ud2b8 \uc81c\ubaa9", None))
        self.label_5.setText(QCoreApplication.translate("Plot", u"\ucc28\ud2b8 \uc18c\uc81c\ubaa9", None))
        self.label_7.setText(QCoreApplication.translate("Plot", u"\ub2e8\uc704", None))
        self.designBox.setTitle(QCoreApplication.translate("Plot", u"\ub514\uc790\uc778 \uc635\uc158", None))
        self.label_3.setText(QCoreApplication.translate("Plot", u"\ud3f0\ud2b8 \uc124\uc815 :", None))
        self.bg.setText(QCoreApplication.translate("Plot", u"\ucc28\ud2b8 \ubc30\uacbd \uc0c9\uc0c1 :", None))
        self.bgcolorPicker.setText(QCoreApplication.translate("Plot", u"#ffffff", None))
        self.label_2.setText(QCoreApplication.translate("Plot", u"\uae00\uc790 \uc0c9\uc0c1 :", None))
        self.colorPicker.setText(QCoreApplication.translate("Plot", u"#000000", None))
        self.label_6.setText(QCoreApplication.translate("Plot", u"\ucd5c\uc18c \uae00\uc790\ud06c\uae30", None))
        self.resetOption.setText(QCoreApplication.translate("Plot", u"\uc635\uc158 \ucd08\uae30\ud654", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), QCoreApplication.translate("Plot", u"\ucc28\ud2b8 \uc635\uc158", None))
        self.initTreemap.setText(QCoreApplication.translate("Plot", u"\ucc28\ud2b8 \uc0dd\uc131\ud558\uae30", None))
        self.saveWC.setText(QCoreApplication.translate("Plot", u"\uc774\ubbf8\uc9c0\ub85c \uc800\uc7a5\ud558\uae30", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab1), QCoreApplication.translate("Plot", u"\ubd84\ud3ec_\ud2b8\ub9ac\ub9f5", None))
        self.initPie.setText(QCoreApplication.translate("Plot", u"\ucc28\ud2b8 \uc0dd\uc131\ud558\uae30", None))
        self.saveWC_2.setText(QCoreApplication.translate("Plot", u"\uc774\ubbf8\uc9c0\ub85c \uc800\uc7a5\ud558\uae30", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab2), QCoreApplication.translate("Plot", u"\ubd84\ud3ec_\ud30c\uc774", None))
        self.initHbar.setText(QCoreApplication.translate("Plot", u"\ucc28\ud2b8 \uc0dd\uc131\ud558\uae30", None))
        self.saveWC_3.setText(QCoreApplication.translate("Plot", u"\uc774\ubbf8\uc9c0\ub85c \uc800\uc7a5\ud558\uae30", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab3), QCoreApplication.translate("Plot", u"\ubd84\ud3ec_\ubc14", None))
        self.initLine.setText(QCoreApplication.translate("Plot", u"\ucc28\ud2b8 \uc0dd\uc131\ud558\uae30", None))
        self.saveWC_4.setText(QCoreApplication.translate("Plot", u"\uc774\ubbf8\uc9c0\ub85c \uc800\uc7a5\ud558\uae30", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab4), QCoreApplication.translate("Plot", u"\uc2dc\uacc4\uc5f4_\ub77c\uc778", None))
        self.initBar.setText(QCoreApplication.translate("Plot", u"\ucc28\ud2b8 \uc0dd\uc131\ud558\uae30", None))
        self.saveWC_5.setText(QCoreApplication.translate("Plot", u"\uc774\ubbf8\uc9c0\ub85c \uc800\uc7a5\ud558\uae30", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab5), QCoreApplication.translate("Plot", u"\uc2dc\uacc4\uc5f4_\ubc14", None))
        self.initSankey.setText(QCoreApplication.translate("Plot", u"\ucc28\ud2b8 \uc0dd\uc131\ud558\uae30", None))
        self.saveWC_6.setText(QCoreApplication.translate("Plot", u"\uc774\ubbf8\uc9c0\ub85c \uc800\uc7a5\ud558\uae30", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab6), QCoreApplication.translate("Plot", u"\uc0dd\ud0a4", None))
        self.initStat.setText(QCoreApplication.translate("Plot", u"\ucc28\ud2b8 \uc0dd\uc131\ud558\uae30", None))
        self.saveWC_7.setText(QCoreApplication.translate("Plot", u"\uc774\ubbf8\uc9c0\ub85c \uc800\uc7a5\ud558\uae30", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_stat), QCoreApplication.translate("Plot", u"\ud1b5\uacc4", None))
    # retranslateUi

