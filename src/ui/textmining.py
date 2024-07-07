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
    QFontComboBox, QFormLayout, QGraphicsView, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QTabWidget, QVBoxLayout, QWidget)

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
        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)

        self.formLayout_4.setWidget(0, QFormLayout.SpanningRole, self.label)

        self.Label_8 = QLabel(self.groupBox_4)
        self.Label_8.setObjectName(u"Label_8")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.Label_8)

        self.startDate = QDateEdit(self.groupBox_4)
        self.startDate.setObjectName(u"startDate")
        self.startDate.setDateTime(QDateTime(QDate(2001, 1, 1), QTime(9, 0, 0)))
        self.startDate.setMaximumDate(QDate(9994, 1, 2))
        self.startDate.setCalendarPopup(True)
        self.startDate.setTimeSpec(Qt.TimeSpec.LocalTime)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.startDate)

        self.Label = QLabel(self.groupBox_4)
        self.Label.setObjectName(u"Label")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.Label)

        self.endDate = QDateEdit(self.groupBox_4)
        self.endDate.setObjectName(u"endDate")
        self.endDate.setCalendarPopup(True)
        self.endDate.setTimeSpec(Qt.TimeSpec.LocalTime)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.endDate)


        self.verticalLayout_10.addLayout(self.formLayout_4)


        self.verticalLayout_3.addWidget(self.groupBox_4)

        self.groupBox_6 = QGroupBox(self.tabWidgetPage1)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(0, 0))
        self.groupBox_6.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 3, -1, -1)
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.Label_9 = QLabel(self.groupBox_6)
        self.Label_9.setObjectName(u"Label_9")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.Label_9)

        self.inText = QLineEdit(self.groupBox_6)
        self.inText.setObjectName(u"inText")
        self.inText.setMinimumSize(QSize(0, 60))
        self.inText.setDragEnabled(True)
        self.inText.setClearButtonEnabled(True)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.inText)

        self.Label_10 = QLabel(self.groupBox_6)
        self.Label_10.setObjectName(u"Label_10")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.Label_10)

        self.exText = QLineEdit(self.groupBox_6)
        self.exText.setObjectName(u"exText")
        self.exText.setMinimumSize(QSize(0, 60))
        self.exText.setDragEnabled(True)
        self.exText.setClearButtonEnabled(True)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.exText)


        self.verticalLayout_11.addLayout(self.formLayout_5)


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
"color: #FFDFB9;")

        self.verticalLayout_3.addWidget(self.resetFilter)

        self.applyFilter = QPushButton(self.tabWidgetPage1)
        self.applyFilter.setObjectName(u"applyFilter")
        self.applyFilter.setStyleSheet(u"background-color: #00539C;\n"
"color: #EEA47F;")
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
        self.groupBox.setMinimumSize(QSize(0, 150))
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.formLayout_7 = QFormLayout(self.groupBox)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.Label_3 = QLabel(self.groupBox)
        self.Label_3.setObjectName(u"Label_3")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.Label_3)

        self.topnCount = QSpinBox(self.groupBox)
        self.topnCount.setObjectName(u"topnCount")
        self.topnCount.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.topnCount.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.topnCount.setMinimum(10)
        self.topnCount.setMaximum(100)
        self.topnCount.setSingleStep(5)
        self.topnCount.setValue(40)

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.topnCount)

        self.Label_2 = QLabel(self.groupBox)
        self.Label_2.setObjectName(u"Label_2")
        self.Label_2.setScaledContents(False)
        self.Label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_7.setWidget(3, QFormLayout.LabelRole, self.Label_2)

        self.stopwordEdit = QLineEdit(self.groupBox)
        self.stopwordEdit.setObjectName(u"stopwordEdit")

        self.formLayout_7.setWidget(3, QFormLayout.FieldRole, self.stopwordEdit)

        self.Label_4 = QLabel(self.groupBox)
        self.Label_4.setObjectName(u"Label_4")

        self.formLayout_7.setWidget(2, QFormLayout.LabelRole, self.Label_4)

        self.nnCount = QSpinBox(self.groupBox)
        self.nnCount.setObjectName(u"nnCount")
        self.nnCount.setAutoFillBackground(False)
        self.nnCount.setWrapping(False)
        self.nnCount.setFrame(True)
        self.nnCount.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.nnCount.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.nnCount.setMinimum(1)
        self.nnCount.setMaximum(5)
        self.nnCount.setValue(2)

        self.formLayout_7.setWidget(2, QFormLayout.FieldRole, self.nnCount)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 60))
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.formLayout_7.setWidget(1, QFormLayout.SpanningRole, self.label_4)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tabWidgetPage2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout_3 = QFormLayout(self.groupBox_2)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(16777215, 300))

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.fontComboBox = QFontComboBox(self.groupBox_2)
        self.fontComboBox.setObjectName(u"fontComboBox")
        self.fontComboBox.setMaximumSize(QSize(150, 16777215))

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.fontComboBox)

        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.comboBox)

        self.bg = QLabel(self.groupBox_2)
        self.bg.setObjectName(u"bg")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.bg)

        self.bgColor = QComboBox(self.groupBox_2)
        self.bgColor.setObjectName(u"bgColor")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.bgColor)


        self.verticalLayout_4.addWidget(self.groupBox_2)

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
        self.tabWidget1 = QTabWidget(TextMining)
        self.tabWidget1.setObjectName(u"tabWidget1")
        self.tableTab = QWidget()
        self.tableTab.setObjectName(u"tableTab")
        self.verticalLayout = QVBoxLayout(self.tableTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tablePlot = QWebEngineView(self.tableTab)
        self.tablePlot.setObjectName(u"tablePlot")
        self.tablePlot.setUrl(QUrl(u"about:blank"))

        self.verticalLayout.addWidget(self.tablePlot)

        self.tabWidget1.addTab(self.tableTab, "")
        self.TFTab = QWidget()
        self.TFTab.setObjectName(u"TFTab")
        self.verticalLayout_7 = QVBoxLayout(self.TFTab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.TFplot = QWebEngineView(self.TFTab)
        self.TFplot.setObjectName(u"TFplot")
        self.TFplot.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_7.addWidget(self.TFplot)

        self.saveTF = QPushButton(self.TFTab)
        self.saveTF.setObjectName(u"saveTF")

        self.verticalLayout_7.addWidget(self.saveTF)

        self.tabWidget1.addTab(self.TFTab, "")
        self.wcTab = QWidget()
        self.wcTab.setObjectName(u"wcTab")
        self.verticalLayout_8 = QVBoxLayout(self.wcTab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.graphicsView = QGraphicsView(self.wcTab)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_8.addWidget(self.graphicsView)

        self.tabWidget1.addTab(self.wcTab, "")
        self.networkTab = QWidget()
        self.networkTab.setObjectName(u"networkTab")
        self.verticalLayout_9 = QVBoxLayout(self.networkTab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.networkPlot = QWebEngineView(self.networkTab)
        self.networkPlot.setObjectName(u"networkPlot")
        self.networkPlot.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_9.addWidget(self.networkPlot)

        self.tabWidget1.addTab(self.networkTab, "")

        self.verticalLayout_2.addWidget(self.tabWidget1)

        self.initTable = QPushButton(TextMining)
        self.initTable.setObjectName(u"initTable")

        self.verticalLayout_2.addWidget(self.initTable)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.verticalLayout_2)


        self.retranslateUi(TextMining)

        self.tabWidget.setCurrentIndex(0)
        self.applyFilter.setDefault(False)
        self.tabWidget1.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TextMining)
    # setupUi

    def retranslateUi(self, TextMining):
        TextMining.setWindowTitle(QCoreApplication.translate("TextMining", u"Form", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("TextMining", u"\uae30\uac04 \ud544\ud130", None))
        self.label.setText(QCoreApplication.translate("TextMining", u"\ub370\uc774\ud130 \ubc94\uc704 \uc124\uc815", None))
        self.Label_8.setText(QCoreApplication.translate("TextMining", u"\uc2dc\uc791\uc77c :", None))
        self.Label.setText(QCoreApplication.translate("TextMining", u"\uc885\ub8cc\uc77c :", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("TextMining", u"\ud14d\uc2a4\ud2b8 \ud544\ud130", None))
        self.Label_9.setText(QCoreApplication.translate("TextMining", u"\ud3ec\ud568\ud560 \ub2e8\uc5b4 :", None))
        self.inText.setPlaceholderText(QCoreApplication.translate("TextMining", u"ex) \ud734\uac8c\uc18c, \ub098\ubb34, \uac10\uc790", None))
        self.Label_10.setText(QCoreApplication.translate("TextMining", u"\uc81c\uc678\ud560 \ub2e8\uc5b4 :", None))
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
        self.Label_3.setText(QCoreApplication.translate("TextMining", u"\ub178\ub4dc\uac1c\uc218", None))
        self.Label_2.setText(QCoreApplication.translate("TextMining", u"\ubd88\uc6a9\uc5b4 :", None))
        self.Label_4.setText(QCoreApplication.translate("TextMining", u"n-gram \ubc94\uc704 :", None))
        self.label_4.setText(QCoreApplication.translate("TextMining", u"\u203b \ub178\ub4dc \uac1c\uc218\ub294 \ub2e8\uc5b4\uc758 \uac1c\uc218\uc785\ub2c8\ub2e4. \n"
" \ub178\ub4dc\uc758 \uac1c\uc218\uac00 \ub9ce\uc744\uc218\ub85d \uc2dc\uc778\uc131\uc740 \ub5a8\uc5b4\uc9d1\ub2c8\ub2e4.", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TextMining", u"\ub514\uc790\uc778", None))
        self.label_3.setText(QCoreApplication.translate("TextMining", u"\ud3f0\ud2b8 \uc124\uc815 :", None))
        self.label_2.setText(QCoreApplication.translate("TextMining", u"\uae00\uc790 \uc0c9\uc0c1 :", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("TextMining", u"\ud654\uc774\ud2b8", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("TextMining", u"\ub2e4\ud06c", None))

        self.bg.setText(QCoreApplication.translate("TextMining", u"\ubc30\uacbd\uc0c9\uc0c1 :", None))
        self.pushButton_2.setText(QCoreApplication.translate("TextMining", u"\uc635\uc158 \ucd08\uae30\ud654", None))
        self.pushButton_3.setText(QCoreApplication.translate("TextMining", u"\uc635\uc158 \uc801\uc6a9", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), QCoreApplication.translate("TextMining", u"\ucc28\ud2b8 \uc635\uc158", None))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.tableTab), QCoreApplication.translate("TextMining", u"\uadf8\ub0e5 \ud45c", None))
        self.saveTF.setText(QCoreApplication.translate("TextMining", u"\ud45c\ub85c \uc800\uc7a5\ud558\uae30", None))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.TFTab), QCoreApplication.translate("TextMining", u"\u25a6 \ub2e8\uc5b4 \ube48\ub3c4\ud45c", None))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.wcTab), QCoreApplication.translate("TextMining", u"\u2601 \uc6cc\ub4dc\ud074\ub77c\uc6b0\ub4dc", None))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.networkTab), QCoreApplication.translate("TextMining", u"\u2668 \ub124\ud2b8\uc6cc\ud06c", None))
        self.initTable.setText(QCoreApplication.translate("TextMining", u"\uc0c8\ub85c\uace0\uce68", None))
    # retranslateUi

