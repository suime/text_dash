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
    QTabWidget, QTableView, QToolBox, QVBoxLayout,
    QWidget)

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
        self.toolBox = QToolBox(TextMining)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBoxPage1 = QWidget()
        self.toolBoxPage1.setObjectName(u"toolBoxPage1")
        self.verticalLayout_3 = QVBoxLayout(self.toolBoxPage1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_2 = QGroupBox(self.toolBoxPage1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
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


        self.verticalLayout_5.addLayout(self.formLayout)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.toolBoxPage1)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
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


        self.verticalLayout_4.addLayout(self.formLayout_2)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.groupBox_5 = QGroupBox(self.toolBoxPage1)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.Label_4 = QLabel(self.groupBox_5)
        self.Label_4.setObjectName(u"Label_4")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.Label_4)

        self.LineEdit_3 = QLineEdit(self.groupBox_5)
        self.LineEdit_3.setObjectName(u"LineEdit_3")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.LineEdit_3)

        self.sub = QLabel(self.groupBox_5)
        self.sub.setObjectName(u"sub")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.sub)

        self.ComboBox = QComboBox(self.groupBox_5)
        self.ComboBox.setObjectName(u"ComboBox")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.ComboBox)

        self.Label_5 = QLabel(self.groupBox_5)
        self.Label_5.setObjectName(u"Label_5")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.Label_5)

        self.ComboBox_2 = QComboBox(self.groupBox_5)
        self.ComboBox_2.setObjectName(u"ComboBox_2")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.ComboBox_2)


        self.verticalLayout_6.addLayout(self.formLayout_3)


        self.verticalLayout_3.addWidget(self.groupBox_5)

        self.pushButton_3 = QPushButton(self.toolBoxPage1)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setFlat(False)

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.toolBox.addItem(self.toolBoxPage1, u"")
        self.toolBoxPage2 = QWidget()
        self.toolBoxPage2.setObjectName(u"toolBoxPage2")
        self.toolBox.addItem(self.toolBoxPage2, u"")

        self.verticalLayout.addWidget(self.toolBox)

        self.pushButton_2 = QPushButton(TextMining)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(TextMining)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_7 = QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tableView = QTableView(self.tab)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_7.addWidget(self.tableView)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_8 = QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.graphicsView = QGraphicsView(self.tab_2)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_8.addWidget(self.graphicsView)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_9 = QVBoxLayout(self.tab_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.webEngineView = QWebEngineView(self.tab_3)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_9.addWidget(self.webEngineView)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.pushButton = QPushButton(TextMining)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(TextMining)

        self.pushButton_3.setDefault(False)
        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(TextMining)
    # setupUi

    def retranslateUi(self, TextMining):
        TextMining.setWindowTitle(QCoreApplication.translate("TextMining", u"Form", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TextMining", u"\uae30\uac04 \ud544\ud130", None))
        self.Label.setText(QCoreApplication.translate("TextMining", u"\uae30\uac04 \uc870\uc815", None))
        self.Label_2.setText(QCoreApplication.translate("TextMining", u"\ub0a0\uc9dc \uc870\uc815", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("TextMining", u"\ud14d\uc2a4\ud2b8 \ud544\ud130", None))
        self.Label_3.setText(QCoreApplication.translate("TextMining", u"\ud3ec\ud568\ud560 \ub2e8\uc5b4", None))
        self.Label_6.setText(QCoreApplication.translate("TextMining", u"\uc81c\uc678\ud560 \ub2e8\uc5b4", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("TextMining", u"\ubd84\ub958 \ud544\ud130", None))
        self.Label_4.setText(QCoreApplication.translate("TextMining", u"\uce74\ud14c\uace0\ub9ac \uc120\ud0dd", None))
        self.sub.setText(QCoreApplication.translate("TextMining", u"\uc911\uce74\ud14c\uace0\ub9ac \uc120\ud0dd", None))
        self.Label_5.setText(QCoreApplication.translate("TextMining", u"\uc18c\ubd84\ub958 \uc120\ud0dd", None))
        self.pushButton_3.setText(QCoreApplication.translate("TextMining", u"\uc801\uc6a9\ud558\uae30", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.toolBoxPage1), "")
        self.toolBox.setItemText(self.toolBox.indexOf(self.toolBoxPage2), "")
        self.pushButton_2.setText(QCoreApplication.translate("TextMining", u"\ucc28\ud2b8 \uc0dd\uc131\ud558\uae30", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("TextMining", u"\ub2e8\uc5b4 \ube48\ub3c4\ud45c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("TextMining", u"\uc6cc\ub4dc\ud074\ub77c\uc6b0\ub4dc", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("TextMining", u"\ub124\ud2b8\uc6cc\ud06c", None))
        self.pushButton.setText(QCoreApplication.translate("TextMining", u"\ubc84\ud2bc", None))
    # retranslateUi

