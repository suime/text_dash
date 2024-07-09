# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TextMining.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QFontComboBox, QFormLayout, QFrame, QGridLayout,
    QGroupBox, QLabel, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpinBox, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_TextMining(object):
    def setupUi(self, TextMining):
        if not TextMining.objectName():
            TextMining.setObjectName(u"TextMining")
        TextMining.resize(912, 591)
        self.formLayout = QFormLayout(TextMining)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.tabWidget = QTabWidget(TextMining)
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
        self.startDate.setMaximumDate(QDate(9994, 1, 4))
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
        self.category1.setObjectName(u"category1")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.category1)

        self.Label_12 = QLabel(self.groupBox_5)
        self.Label_12.setObjectName(u"Label_12")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.Label_12)

        self.category2 = QComboBox(self.groupBox_5)
        self.category2.setObjectName(u"category2")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.category2)

        self.Label_13 = QLabel(self.groupBox_5)
        self.Label_13.setObjectName(u"Label_13")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.Label_13)

        self.category3 = QComboBox(self.groupBox_5)
        self.category3.setObjectName(u"category3")

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.category3)


        self.verticalLayout_6.addLayout(self.formLayout_6)


        self.verticalLayout_3.addWidget(self.groupBox_5)

        self.resetFilter = QPushButton(self.tabWidgetPage1)
        self.resetFilter.setObjectName(u"resetFilter")
        self.resetFilter.setStyleSheet(u"background-color: #A4193D;\n"
"color: #FFF;\n"
"font-weight: bold;")

        self.verticalLayout_3.addWidget(self.resetFilter)

        self.applyFilter = QPushButton(self.tabWidgetPage1)
        self.applyFilter.setObjectName(u"applyFilter")
        self.applyFilter.setStyleSheet(u"background-color: #00539C;\n"
"color: #FFF;\n"
"font-weight: bold;")
        self.applyFilter.setAutoDefault(False)
        self.applyFilter.setFlat(False)

        self.verticalLayout_3.addWidget(self.applyFilter)

        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QWidget()
        self.tabWidgetPage2.setObjectName(u"tabWidgetPage2")
        self.verticalLayout_4 = QVBoxLayout(self.tabWidgetPage2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox = QGroupBox(self.tabWidgetPage2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 100))
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.nnCount = QSpinBox(self.groupBox)
        self.nnCount.setObjectName(u"nnCount")
        self.nnCount.setAutoFillBackground(False)
        self.nnCount.setWrapping(False)
        self.nnCount.setFrame(True)
        self.nnCount.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.nnCount.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.nnCount.setMinimum(1)
        self.nnCount.setMaximum(5)
        self.nnCount.setValue(1)

        self.gridLayout.addWidget(self.nnCount, 1, 1, 1, 1)

        self.Label_4 = QLabel(self.groupBox)
        self.Label_4.setObjectName(u"Label_4")

        self.gridLayout.addWidget(self.Label_4, 1, 0, 1, 1)

        self.Label_2 = QLabel(self.groupBox)
        self.Label_2.setObjectName(u"Label_2")
        self.Label_2.setScaledContents(False)
        self.Label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Label_2, 3, 0, 1, 1)

        self.nnCount_2 = QSpinBox(self.groupBox)
        self.nnCount_2.setObjectName(u"nnCount_2")
        self.nnCount_2.setAutoFillBackground(False)
        self.nnCount_2.setWrapping(False)
        self.nnCount_2.setFrame(True)
        self.nnCount_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.nnCount_2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.nnCount_2.setMinimum(1)
        self.nnCount_2.setMaximum(5)
        self.nnCount_2.setValue(2)

        self.gridLayout.addWidget(self.nnCount_2, 1, 2, 1, 1)

        self.stopwordsEdit = QPlainTextEdit(self.groupBox)
        self.stopwordsEdit.setObjectName(u"stopwordsEdit")
        self.stopwordsEdit.setTabChangesFocus(True)

        self.gridLayout.addWidget(self.stopwordsEdit, 4, 0, 1, 3)

        self.topnCount = QSpinBox(self.groupBox)
        self.topnCount.setObjectName(u"topnCount")
        self.topnCount.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.topnCount.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.topnCount.setMinimum(10)
        self.topnCount.setMaximum(100)
        self.topnCount.setSingleStep(5)
        self.topnCount.setValue(40)

        self.gridLayout.addWidget(self.topnCount, 0, 2, 1, 1)

        self.Label_3 = QLabel(self.groupBox)
        self.Label_3.setObjectName(u"Label_3")

        self.gridLayout.addWidget(self.Label_3, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.designBox = QGroupBox(self.tabWidgetPage2)
        self.designBox.setObjectName(u"designBox")
        self.gridLayout_2 = QGridLayout(self.designBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.designBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.bg = QLabel(self.designBox)
        self.bg.setObjectName(u"bg")

        self.gridLayout_2.addWidget(self.bg, 2, 0, 1, 1)

        self.fontComboBox = QFontComboBox(self.designBox)
        self.fontComboBox.setObjectName(u"fontComboBox")
        self.fontComboBox.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_2.addWidget(self.fontComboBox, 0, 1, 1, 1)

        self.label_2 = QLabel(self.designBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(16777215, 300))

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.comboBox = QComboBox(self.designBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2.addWidget(self.comboBox, 1, 1, 1, 1)

        self.bgcolorPicker = QPushButton(self.designBox)
        self.bgcolorPicker.setObjectName(u"bgcolorPicker")

        self.gridLayout_2.addWidget(self.bgcolorPicker, 2, 2, 1, 1)

        self.sampleText = QLabel(self.designBox)
        self.sampleText.setObjectName(u"sampleText")
        self.sampleText.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.sampleText.setFrameShape(QFrame.Shape.StyledPanel)
        self.sampleText.setFrameShadow(QFrame.Shadow.Plain)
        self.sampleText.setLineWidth(1)

        self.gridLayout_2.addWidget(self.sampleText, 2, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.designBox)

        self.pushButton_2 = QPushButton(self.tabWidgetPage2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_4.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.tabWidgetPage2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_4.addWidget(self.pushButton_3)

        self.tabWidget.addTab(self.tabWidgetPage2, "")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.tabWidget)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.formLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Main = QTabWidget(TextMining)
        self.Main.setObjectName(u"Main")
        self.Main.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.datatab = QWidget()
        self.datatab.setObjectName(u"datatab")
        self.verticalLayout_11 = QVBoxLayout(self.datatab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.dfplot = QWebEngineView(self.datatab)
        self.dfplot.setObjectName(u"dfplot")
        self.dfplot.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_11.addWidget(self.dfplot)

        self.initDf = QPushButton(self.datatab)
        self.initDf.setObjectName(u"initDf")
        self.initDf.setStyleSheet(u"background-color: rgb(64, 64, 64);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_11.addWidget(self.initDf)

        self.saveData = QPushButton(self.datatab)
        self.saveData.setObjectName(u"saveData")
        self.saveData.setStyleSheet(u"background-color: #178047;\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_11.addWidget(self.saveData)

        self.Main.addTab(self.datatab, "")
        self.tableTab = QWidget()
        self.tableTab.setObjectName(u"tableTab")
        self.verticalLayout = QVBoxLayout(self.tableTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tablePlot = QWebEngineView(self.tableTab)
        self.tablePlot.setObjectName(u"tablePlot")
        self.tablePlot.setUrl(QUrl(u"about:blank"))

        self.verticalLayout.addWidget(self.tablePlot)

        self.initTable = QPushButton(self.tableTab)
        self.initTable.setObjectName(u"initTable")
        self.initTable.setStyleSheet(u"background-color: rgb(64, 64, 64);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.initTable)

        self.saveStat = QPushButton(self.tableTab)
        self.saveStat.setObjectName(u"saveStat")

        self.verticalLayout.addWidget(self.saveStat)

        self.Main.addTab(self.tableTab, "")
        self.TFTab = QWidget()
        self.TFTab.setObjectName(u"TFTab")
        self.verticalLayout_7 = QVBoxLayout(self.TFTab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.TFplot = QWebEngineView(self.TFTab)
        self.TFplot.setObjectName(u"TFplot")
        self.TFplot.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_7.addWidget(self.TFplot)

        self.initTF = QPushButton(self.TFTab)
        self.initTF.setObjectName(u"initTF")
        self.initTF.setStyleSheet(u"background-color: rgb(64, 64, 64);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.initTF)

        self.saveTf = QPushButton(self.TFTab)
        self.saveTf.setObjectName(u"saveTf")

        self.verticalLayout_7.addWidget(self.saveTf)

        self.Main.addTab(self.TFTab, "")
        self.wcTab = QWidget()
        self.wcTab.setObjectName(u"wcTab")
        self.verticalLayout_8 = QVBoxLayout(self.wcTab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.WClayout = QVBoxLayout()
        self.WClayout.setObjectName(u"WClayout")

        self.verticalLayout_8.addLayout(self.WClayout)

        self.initWC = QPushButton(self.wcTab)
        self.initWC.setObjectName(u"initWC")
        self.initWC.setStyleSheet(u"background-color: rgb(64, 64, 64);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.initWC)

        self.saveWC = QPushButton(self.wcTab)
        self.saveWC.setObjectName(u"saveWC")

        self.verticalLayout_8.addWidget(self.saveWC)

        self.Main.addTab(self.wcTab, "")
        self.networkTab = QWidget()
        self.networkTab.setObjectName(u"networkTab")
        self.verticalLayout_9 = QVBoxLayout(self.networkTab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.networkPlot = QWebEngineView(self.networkTab)
        self.networkPlot.setObjectName(u"networkPlot")
        self.networkPlot.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_9.addWidget(self.networkPlot)

        self.initNetwork = QPushButton(self.networkTab)
        self.initNetwork.setObjectName(u"initNetwork")
        self.initNetwork.setStyleSheet(u"background-color: rgb(64, 64, 64);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.initNetwork)

        self.saveNetwork = QPushButton(self.networkTab)
        self.saveNetwork.setObjectName(u"saveNetwork")

        self.verticalLayout_9.addWidget(self.saveNetwork)

        self.Main.addTab(self.networkTab, "")

        self.verticalLayout_2.addWidget(self.Main)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.verticalLayout_2)

        QWidget.setTabOrder(self.topnCount, self.nnCount)
        QWidget.setTabOrder(self.nnCount, self.nnCount_2)
        QWidget.setTabOrder(self.nnCount_2, self.stopwordsEdit)
        QWidget.setTabOrder(self.stopwordsEdit, self.fontComboBox)
        QWidget.setTabOrder(self.fontComboBox, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.initTable)
        QWidget.setTabOrder(self.initTable, self.saveStat)
        QWidget.setTabOrder(self.saveStat, self.category3)
        QWidget.setTabOrder(self.category3, self.resetFilter)
        QWidget.setTabOrder(self.resetFilter, self.applyFilter)
        QWidget.setTabOrder(self.applyFilter, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.Main)
        QWidget.setTabOrder(self.Main, self.startDate)
        QWidget.setTabOrder(self.startDate, self.category2)
        QWidget.setTabOrder(self.category2, self.initTF)
        QWidget.setTabOrder(self.initTF, self.initWC)
        QWidget.setTabOrder(self.initWC, self.saveWC)
        QWidget.setTabOrder(self.saveWC, self.initNetwork)
        QWidget.setTabOrder(self.initNetwork, self.saveTf)
        QWidget.setTabOrder(self.saveTf, self.saveNetwork)
        QWidget.setTabOrder(self.saveNetwork, self.endDate)
        QWidget.setTabOrder(self.endDate, self.category1)
        QWidget.setTabOrder(self.category1, self.inText)
        QWidget.setTabOrder(self.inText, self.exText)

        self.retranslateUi(TextMining)

        self.tabWidget.setCurrentIndex(1)
        self.applyFilter.setDefault(False)
        self.Main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TextMining)
    # setupUi

    def retranslateUi(self, TextMining):
        TextMining.setWindowTitle(QCoreApplication.translate("TextMining", u"Form", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("TextMining", u"\uae30\uac04 \ud544\ud130", None))
        self.label.setText(QCoreApplication.translate("TextMining", u"\ub370\uc774\ud130 \ubc94\uc704 \uc124\uc815", None))
        self.Label_8.setText(QCoreApplication.translate("TextMining", u"\uc2dc\uc791\uc77c :", None))
        self.Label.setText(QCoreApplication.translate("TextMining", u"\uc885\ub8cc\uc77c :", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("TextMining", u"\ud14d\uc2a4\ud2b8 \ud544\ud130", None))
        self.Label_9.setText(QCoreApplication.translate("TextMining", u"\ud3ec\ud568\ud560 \ub2e8\uc5b4", None))
        self.inText.setPlaceholderText(QCoreApplication.translate("TextMining", u"\uc27c\ud45c\ub098 \uc5d4\ud130\ud0a4\ub85c \uad6c\ubd84\ud558\uc5ec \uc791\uc131\ud558\uc138\uc694. ex) \ud55c\uad6d, \ub3c4\ub85c, \uacf5\uc0ac", None))
#if QT_CONFIG(tooltip)
        self.Label_10.setToolTip(QCoreApplication.translate("TextMining", u"<html><head/><body><p>\ud45c\uc5d0\uc11c \uc81c\uc678\ud560 \ud14d\uc2a4\ud2b8\ub97c \uc27c\ud45c\ub098, \uc904\ubc14\uafc8\uc73c\ub85c \uad6c\ubd84\ud574\uc11c \uc791\uc131\ud558\uc138\uc694</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Label_10.setText(QCoreApplication.translate("TextMining", u"\uc81c\uc678\ud560 \ub2e8\uc5b4", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("TextMining", u"\ubd84\ub958 \ud544\ud130", None))
        self.Label_6.setText(QCoreApplication.translate("TextMining", u"\ub300\ubd84\ub958 :", None))
        self.category1.setPlaceholderText(QCoreApplication.translate("TextMining", u"\ubbf8\uc124\uc815", None))
        self.Label_12.setText(QCoreApplication.translate("TextMining", u"\uc911\ubd84\ub958 :", None))
        self.category2.setPlaceholderText(QCoreApplication.translate("TextMining", u"\ubbf8\uc124\uc815", None))
        self.Label_13.setText(QCoreApplication.translate("TextMining", u"\uc18c\ubd84\ub958 :", None))
        self.category3.setPlaceholderText(QCoreApplication.translate("TextMining", u"\ubbf8\uc124\uc815", None))
        self.resetFilter.setText(QCoreApplication.translate("TextMining", u"\ud544\ud130 \ucd08\uae30\ud654", None))
        self.applyFilter.setText(QCoreApplication.translate("TextMining", u"\ud544\ud130 \uc801\uc6a9\ud558\uae30", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), QCoreApplication.translate("TextMining", u"\ub370\uc774\ud130 \ud544\ud130", None))
        self.groupBox.setTitle(QCoreApplication.translate("TextMining", u"\ud14d\uc2a4\ud2b8 \uc635\uc158", None))
        self.Label_4.setText(QCoreApplication.translate("TextMining", u"n-gram \ubc94\uc704 :", None))
#if QT_CONFIG(tooltip)
        self.Label_2.setToolTip(QCoreApplication.translate("TextMining", u"<html><head/><body><p>\ubd88\uc6a9\uc5b4\ub294 \ucc28\ud2b8\uc5d0\uc11c\ub9cc \uc228\uae38 \ub2e8\uc5b4\uc785\ub2c8\ub2e4.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Label_2.setText(QCoreApplication.translate("TextMining", u"\ubd88\uc6a9\uc5b4", None))
        self.stopwordsEdit.setDocumentTitle("")
        self.stopwordsEdit.setPlaceholderText(QCoreApplication.translate("TextMining", u"\ucc28\ud2b8\uc5d0\uc11c \uc228\uae38 \ub2e8\uc5b4\ub97c \uc27c\ud45c\uc640 \uc904\ubc14\uafc8\uc73c\ub85c \uad6c\ubd84\ud574\uc11c \uc785\ub825\ud558\uc138\uc694.", None))
#if QT_CONFIG(tooltip)
        self.Label_3.setToolTip(QCoreApplication.translate("TextMining", u"<html><head/><body><p>\ub178\ub4dc\uac1c\uc218\ub294 \ud45c\uc2dc\ud560 \ub2e8\uc5b4\uc758 \uac1c\uc218\uc785\ub2c8\ub2e4.</p><p>\ub9ce\uc744\uc218\ub85d \ucc28\ud2b8\uac00 \ubcf5\uc7a1\ud558\uc5ec \ubcf4\uae30\uac00 \uc5b4\ub824\uc6cc\uc9d1\ub2c8\ub2e4.<br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Label_3.setWhatsThis(QCoreApplication.translate("TextMining", u"<html><head/><body><p>\ub178\ub4dc \uac1c\uc218\ub294 \ud45c\uc2dc\ud560 \ub2e8\uc5b4\uc758 \uac1c\uc218\uc785\ub2c8\ub2e4. </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Label_3.setText(QCoreApplication.translate("TextMining", u"\ub178\ub4dc\uac1c\uc218 :", None))
        self.designBox.setTitle(QCoreApplication.translate("TextMining", u"\ub514\uc790\uc778 \uc635\uc158", None))
        self.label_3.setText(QCoreApplication.translate("TextMining", u"\ud3f0\ud2b8 \uc124\uc815 :", None))
        self.bg.setText(QCoreApplication.translate("TextMining", u"\ucc28\ud2b8 \ubc30\uacbd \uc0c9\uc0c1 :", None))
        self.label_2.setText(QCoreApplication.translate("TextMining", u"\uae00\uc790 \uc0c9\uc0c1 :", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("TextMining", u"\ud654\uc774\ud2b8", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("TextMining", u"\ub2e4\ud06c", None))

        self.bgcolorPicker.setText(QCoreApplication.translate("TextMining", u"\uc0c9\uc0c1 \uc120\ud0dd", None))
        self.sampleText.setText(QCoreApplication.translate("TextMining", u" 0", None))
        self.pushButton_2.setText(QCoreApplication.translate("TextMining", u"\uc635\uc158 \ucd08\uae30\ud654", None))
        self.pushButton_3.setText(QCoreApplication.translate("TextMining", u"\uc635\uc158 \uc801\uc6a9", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), QCoreApplication.translate("TextMining", u"\ucc28\ud2b8 \uc635\uc158", None))
        self.initDf.setText(QCoreApplication.translate("TextMining", u"\uc0dd\uc131\ud558\uae30", None))
        self.saveData.setText(QCoreApplication.translate("TextMining", u"\uc5d1\uc140\ub85c \uc800\uc7a5\ud558\uae30", None))
        self.Main.setTabText(self.Main.indexOf(self.datatab), QCoreApplication.translate("TextMining", u"\ub370\uc774\ud130", None))
        self.initTable.setText(QCoreApplication.translate("TextMining", u"\ud1b5\uacc4\ud45c \uc0dd\uc131\ud558\uae30", None))
        self.saveStat.setText(QCoreApplication.translate("TextMining", u"\uc774\ubbf8\uc9c0\ub85c \uc800\uc7a5\ud558\uae30", None))
        self.Main.setTabText(self.Main.indexOf(self.tableTab), QCoreApplication.translate("TextMining", u"\ud1b5\uacc4\ud45c", None))
        self.initTF.setText(QCoreApplication.translate("TextMining", u"\ub2e8\uc5b4 \ube48\ub3c4\ud45c \uc0dd\uc131\ud558\uae30", None))
        self.saveTf.setText(QCoreApplication.translate("TextMining", u"\uc5d1\uc140\ub85c \uc800\uc7a5\ud558\uae30", None))
        self.Main.setTabText(self.Main.indexOf(self.TFTab), QCoreApplication.translate("TextMining", u"\ub2e8\uc5b4 \ube48\ub3c4\ud45c", None))
        self.initWC.setText(QCoreApplication.translate("TextMining", u"\uc6cc\ub4dc\ud074\ub77c\uc6b0\ub4dc \uc0dd\uc131\ud558\uae30", None))
        self.saveWC.setText(QCoreApplication.translate("TextMining", u"\uc774\ubbf8\uc9c0\ub85c \uc800\uc7a5\ud558\uae30", None))
        self.Main.setTabText(self.Main.indexOf(self.wcTab), QCoreApplication.translate("TextMining", u"\uc6cc\ub4dc\ud074\ub77c\uc6b0\ub4dc", None))
        self.initNetwork.setText(QCoreApplication.translate("TextMining", u"\ub124\ud2b8\uc6cc\ud06c \ucc28\ud2b8 \uc0dd\uc131\ud558\uae30", None))
        self.saveNetwork.setText(QCoreApplication.translate("TextMining", u"\uc774\ubbf8\uc9c0\ub85c \uc800\uc7a5\ud558\uae30", None))
        self.Main.setTabText(self.Main.indexOf(self.networkTab), QCoreApplication.translate("TextMining", u"\ub124\ud2b8\uc6cc\ud06c", None))
    # retranslateUi

