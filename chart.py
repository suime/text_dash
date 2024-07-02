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
    QFrame, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QTabWidget, QToolBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(904, 520)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.option = QVBoxLayout()
        self.option.setObjectName(u"option")
        self.option.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.toolBox = QToolBox(Form)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 439, 450))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.page)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayoutWidget = QWidget(self.groupBox_2)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 20, 191, 101))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.Label = QLabel(self.formLayoutWidget)
        self.Label.setObjectName(u"Label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.Label)

        self.LineEdit = QLineEdit(self.formLayoutWidget)
        self.LineEdit.setObjectName(u"LineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.LineEdit)

        self.Label_2 = QLabel(self.formLayoutWidget)
        self.Label_2.setObjectName(u"Label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.Label_2)

        self.DateEdit = QDateEdit(self.formLayoutWidget)
        self.DateEdit.setObjectName(u"DateEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.DateEdit)

        self.line = QFrame(self.groupBox_2)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(200, 20, 20, 111))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.page)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.formLayoutWidget_2 = QWidget(self.groupBox_3)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(10, 30, 421, 91))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Label_3 = QLabel(self.formLayoutWidget_2)
        self.Label_3.setObjectName(u"Label_3")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.Label_3)

        self.LineEdit_2 = QLineEdit(self.formLayoutWidget_2)
        self.LineEdit_2.setObjectName(u"LineEdit_2")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.LineEdit_2)

        self.Label_6 = QLabel(self.formLayoutWidget_2)
        self.Label_6.setObjectName(u"Label_6")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.Label_6)

        self.LineEdit_4 = QLineEdit(self.formLayoutWidget_2)
        self.LineEdit_4.setObjectName(u"LineEdit_4")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.LineEdit_4)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.groupBox_5 = QGroupBox(self.page)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.formLayoutWidget_3 = QWidget(self.groupBox_5)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(10, 20, 331, 95))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Label_4 = QLabel(self.formLayoutWidget_3)
        self.Label_4.setObjectName(u"Label_4")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.Label_4)

        self.LineEdit_3 = QLineEdit(self.formLayoutWidget_3)
        self.LineEdit_3.setObjectName(u"LineEdit_3")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.LineEdit_3)

        self.sub = QLabel(self.formLayoutWidget_3)
        self.sub.setObjectName(u"sub")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.sub)

        self.ComboBox = QComboBox(self.formLayoutWidget_3)
        self.ComboBox.setObjectName(u"ComboBox")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.ComboBox)

        self.Label_5 = QLabel(self.formLayoutWidget_3)
        self.Label_5.setObjectName(u"Label_5")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.Label_5)

        self.ComboBox_2 = QComboBox(self.formLayoutWidget_3)
        self.ComboBox_2.setObjectName(u"ComboBox_2")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.ComboBox_2)


        self.verticalLayout_4.addWidget(self.groupBox_5)

        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)

        self.verticalLayout_4.addWidget(self.pushButton)

        self.toolBox.addItem(self.page, u"\ud544\ud130")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 439, 450))
        self.verticalLayout_3 = QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.page_2)
        self.groupBox.setObjectName(u"groupBox")

        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_4 = QGroupBox(self.page_2)
        self.groupBox_4.setObjectName(u"groupBox_4")

        self.verticalLayout_3.addWidget(self.groupBox_4)

        self.RefreshChart = QPushButton(self.page_2)
        self.RefreshChart.setObjectName(u"RefreshChart")

        self.verticalLayout_3.addWidget(self.RefreshChart)

        self.toolBox.addItem(self.page_2, u"\ucc28\ud2b8 \uc635\uc158")

        self.option.addWidget(self.toolBox)


        self.horizontalLayout.addLayout(self.option)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_time = QWidget()
        self.tab_time.setObjectName(u"tab_time")
        self.verticalLayout_2 = QVBoxLayout(self.tab_time)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Linechart = QWebEngineView(self.tab_time)
        self.Linechart.setObjectName(u"Linechart")
        self.Linechart.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_2.addWidget(self.Linechart)

        self.tabWidget.addTab(self.tab_time, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Form)
        self.RefreshChart.clicked.connect(self.Linechart.repaint)

        self.toolBox.setCurrentIndex(0)
        self.pushButton.setDefault(False)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\uae30\uac04 \ud544\ud130", None))
        self.Label.setText(QCoreApplication.translate("Form", u"\uae30\uac04 \uc870\uc815", None))
        self.Label_2.setText(QCoreApplication.translate("Form", u"\ub0a0\uc9dc \uc870\uc815", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\ud14d\uc2a4\ud2b8 \ud544\ud130", None))
        self.Label_3.setText(QCoreApplication.translate("Form", u"\ud3ec\ud568\ud560 \ub2e8\uc5b4", None))
        self.Label_6.setText(QCoreApplication.translate("Form", u"\uc81c\uc678\ud560 \ub2e8\uc5b4", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"\ubd84\ub958 \ud544\ud130", None))
        self.Label_4.setText(QCoreApplication.translate("Form", u"\uce74\ud14c\uace0\ub9ac \uc120\ud0dd", None))
        self.sub.setText(QCoreApplication.translate("Form", u"\uc911\uce74\ud14c\uace0\ub9ac \uc120\ud0dd", None))
        self.Label_5.setText(QCoreApplication.translate("Form", u"\uc18c\ubd84\ub958 \uc120\ud0dd", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\uc801\uc6a9\ud558\uae30", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("Form", u"\ud544\ud130", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.RefreshChart.setText(QCoreApplication.translate("Form", u"\ucc28\ud2b8 \uc0c8\ub85c\uace0\uce68", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("Form", u"\ucc28\ud2b8 \uc635\uc158", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_time), QCoreApplication.translate("Form", u"\uc2dc\uacc4\uc5f4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\ubd84\ud3ec", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\ubc14", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\ub124\ud2b8\uc6cc\ud06c", None))
    # retranslateUi

