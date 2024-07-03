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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QGraphicsView, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTabWidget, QTableView, QVBoxLayout, QWidget)

class Ui_TextMining(object):
    def setupUi(self, TextMining):
        if not TextMining.objectName():
            TextMining.setObjectName(u"TextMining")
        TextMining.resize(848, 579)
        self.horizontalLayout = QHBoxLayout(TextMining)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(TextMining)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(300, 0))
        self.tabWidgetPage1 = QWidget()
        self.tabWidgetPage1.setObjectName(u"tabWidgetPage1")
        self.verticalLayout_3 = QVBoxLayout(self.tabWidgetPage1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_4 = QGroupBox(self.tabWidgetPage1)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 3, -1, -1)
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.Label_7 = QLabel(self.groupBox_4)
        self.Label_7.setObjectName(u"Label_7")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.Label_7)

        self.LineEdit_5 = QLineEdit(self.groupBox_4)
        self.LineEdit_5.setObjectName(u"LineEdit_5")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.LineEdit_5)

        self.Label_8 = QLabel(self.groupBox_4)
        self.Label_8.setObjectName(u"Label_8")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.Label_8)

        self.DateEdit_2 = QDateEdit(self.groupBox_4)
        self.DateEdit_2.setObjectName(u"DateEdit_2")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.DateEdit_2)


        self.verticalLayout_10.addLayout(self.formLayout_4)


        self.verticalLayout_3.addWidget(self.groupBox_4)

        self.groupBox_6 = QGroupBox(self.tabWidgetPage1)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(0, 0))
        self.groupBox_6.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 3, -1, -1)
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.Label_9 = QLabel(self.groupBox_6)
        self.Label_9.setObjectName(u"Label_9")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.Label_9)

        self.LineEdit_6 = QLineEdit(self.groupBox_6)
        self.LineEdit_6.setObjectName(u"LineEdit_6")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.LineEdit_6)

        self.Label_10 = QLabel(self.groupBox_6)
        self.Label_10.setObjectName(u"Label_10")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.Label_10)

        self.LineEdit_7 = QLineEdit(self.groupBox_6)
        self.LineEdit_7.setObjectName(u"LineEdit_7")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.LineEdit_7)


        self.verticalLayout_11.addLayout(self.formLayout_5)


        self.verticalLayout_3.addWidget(self.groupBox_6)

        self.groupBox_5 = QGroupBox(self.tabWidgetPage1)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(0, 0))
        self.groupBox_5.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 3, -1, -1)
        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.Label_6 = QLabel(self.groupBox_5)
        self.Label_6.setObjectName(u"Label_6")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.Label_6)

        self.ComboBox_4 = QComboBox(self.groupBox_5)
        self.ComboBox_4.setObjectName(u"ComboBox_4")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.ComboBox_4)

        self.Label_12 = QLabel(self.groupBox_5)
        self.Label_12.setObjectName(u"Label_12")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.Label_12)

        self.ComboBox_5 = QComboBox(self.groupBox_5)
        self.ComboBox_5.setObjectName(u"ComboBox_5")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.ComboBox_5)

        self.Label_13 = QLabel(self.groupBox_5)
        self.Label_13.setObjectName(u"Label_13")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.Label_13)

        self.ComboBox_6 = QComboBox(self.groupBox_5)
        self.ComboBox_6.setObjectName(u"ComboBox_6")

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.ComboBox_6)


        self.verticalLayout_6.addLayout(self.formLayout_6)


        self.verticalLayout_3.addWidget(self.groupBox_5)

        self.pushButton_4 = QPushButton(self.tabWidgetPage1)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"background-color: rgb(255, 14, 14);")

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.tabWidgetPage1)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"background-color: rgb(0, 111, 255);")
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setFlat(False)

        self.verticalLayout_3.addWidget(self.pushButton_5)

        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QWidget()
        self.tabWidgetPage2.setObjectName(u"tabWidgetPage2")
        self.tabWidget.addTab(self.tabWidgetPage2, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget1 = QTabWidget(TextMining)
        self.tabWidget1.setObjectName(u"tabWidget1")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_7 = QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tableView = QTableView(self.tab)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_7.addWidget(self.tableView)

        self.tabWidget1.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_8 = QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.graphicsView = QGraphicsView(self.tab_2)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_8.addWidget(self.graphicsView)

        self.tabWidget1.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_9 = QVBoxLayout(self.tab_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.webEngineView = QWebEngineView(self.tab_3)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_9.addWidget(self.webEngineView)

        self.tabWidget1.addTab(self.tab_3, "")

        self.verticalLayout_2.addWidget(self.tabWidget1)

        self.pushButton = QPushButton(TextMining)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(TextMining)

        self.tabWidget.setCurrentIndex(0)
        self.pushButton_5.setDefault(False)
        self.tabWidget1.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TextMining)
    # setupUi

    def retranslateUi(self, TextMining):
        TextMining.setWindowTitle(QCoreApplication.translate("TextMining", u"Form", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("TextMining", u"\uae30\uac04 \ud544\ud130", None))
        self.Label_7.setText(QCoreApplication.translate("TextMining", u"\uae30\uac04 \uc870\uc815", None))
        self.Label_8.setText(QCoreApplication.translate("TextMining", u"\ub0a0\uc9dc \uc870\uc815", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("TextMining", u"\ud14d\uc2a4\ud2b8 \ud544\ud130", None))
        self.Label_9.setText(QCoreApplication.translate("TextMining", u"\ud3ec\ud568\ud560 \ub2e8\uc5b4", None))
        self.Label_10.setText(QCoreApplication.translate("TextMining", u"\uc81c\uc678\ud560 \ub2e8\uc5b4", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("TextMining", u"\ubd84\ub958 \ud544\ud130", None))
        self.Label_6.setText(QCoreApplication.translate("TextMining", u"\ub300\ubd84\ub958 :", None))
        self.Label_12.setText(QCoreApplication.translate("TextMining", u"\uc911\ubd84\ub958 :", None))
        self.Label_13.setText(QCoreApplication.translate("TextMining", u"\uc18c\ubd84\ub958 :", None))
        self.pushButton_4.setText(QCoreApplication.translate("TextMining", u"\ud544\ud130 \ucd08\uae30\ud654", None))
        self.pushButton_5.setText(QCoreApplication.translate("TextMining", u"\ud544\ud130 \uc801\uc6a9\ud558\uae30", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), QCoreApplication.translate("TextMining", u"\ub370\uc774\ud130 \ud544\ud130", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), QCoreApplication.translate("TextMining", u"\ucc28\ud2b8 \uc635\uc158", None))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.tab), QCoreApplication.translate("TextMining", u"\u25a6 \ub2e8\uc5b4 \ube48\ub3c4\ud45c", None))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.tab_2), QCoreApplication.translate("TextMining", u"\u2601 \uc6cc\ub4dc\ud074\ub77c\uc6b0\ub4dc", None))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.tab_3), QCoreApplication.translate("TextMining", u"\u2668 \ub124\ud2b8\uc6cc\ud06c", None))
        self.pushButton.setText(QCoreApplication.translate("TextMining", u"\ubc84\ud2bc", None))
    # retranslateUi

