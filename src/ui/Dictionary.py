# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dictionary.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpinBox, QTabWidget,
    QTableWidget, QTableWidgetItem, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Dictionary(object):
    def setupUi(self, Dictionary):
        if not Dictionary.objectName():
            Dictionary.setObjectName(u"Dictionary")
        Dictionary.resize(951, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dictionary.sizePolicy().hasHeightForWidth())
        Dictionary.setSizePolicy(sizePolicy)
        Dictionary.setMinimumSize(QSize(600, 600))
        self.horizontalLayout = QHBoxLayout(Dictionary)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 10)
        self.groupBox = QGroupBox(Dictionary)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(300, 0))
        self.groupBox.setMaximumSize(QSize(300, 16777215))
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.opt_personal = QCheckBox(self.groupBox)
        self.opt_personal.setObjectName(u"opt_personal")
        self.opt_personal.setChecked(True)

        self.gridLayout_2.addWidget(self.opt_personal, 4, 0, 1, 1)

        self.opt_space = QCheckBox(self.groupBox)
        self.opt_space.setObjectName(u"opt_space")

        self.gridLayout_2.addWidget(self.opt_space, 0, 0, 1, 1)

        self.opt_sinmungo = QCheckBox(self.groupBox)
        self.opt_sinmungo.setObjectName(u"opt_sinmungo")
        self.opt_sinmungo.setChecked(True)

        self.gridLayout_2.addWidget(self.opt_sinmungo, 5, 0, 1, 1)

        self.opt_special = QCheckBox(self.groupBox)
        self.opt_special.setObjectName(u"opt_special")
        self.opt_special.setChecked(True)

        self.gridLayout_2.addWidget(self.opt_special, 2, 0, 1, 1)

        self.opt_foriegn = QCheckBox(self.groupBox)
        self.opt_foriegn.setObjectName(u"opt_foriegn")

        self.gridLayout_2.addWidget(self.opt_foriegn, 3, 0, 1, 1)

        self.opt_num = QCheckBox(self.groupBox)
        self.opt_num.setObjectName(u"opt_num")
        self.opt_num.setChecked(True)
        self.opt_num.setTristate(False)

        self.gridLayout_2.addWidget(self.opt_num, 1, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Dictionary)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(300, 16777215))
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_4.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)

        self.spinBox = QSpinBox(self.groupBox_2)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setFrame(True)
        self.spinBox.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.spinBox.setMinimum(3)
        self.spinBox.setMaximum(8)

        self.gridLayout_4.addWidget(self.spinBox, 2, 2, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_4.addWidget(self.lineEdit_2, 1, 0, 1, 2)

        self.toolButton_2 = QToolButton(self.groupBox_2)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.gridLayout_4.addWidget(self.toolButton_2, 1, 2, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Dictionary)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(300, 16777215))
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit = QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setMaximumSize(QSize(300, 16777215))
        self.lineEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.toolButton = QToolButton(self.groupBox_3)
        self.toolButton.setObjectName(u"toolButton")

        self.gridLayout_3.addWidget(self.toolButton, 1, 2, 1, 1)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_3.addWidget(self.label_7, 0, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tabWidget = QTabWidget(Dictionary)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(500, 0))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.tableWidget = QTableWidget(self.tab)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 6):
            self.tableWidget.setRowCount(6)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(50)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.tableWidget)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.tableWidget_2 = QTableWidget(self.tab_2)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.verticalLayout_2.addWidget(self.tableWidget_2)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_3 = QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.listWidget_3 = QListWidget(self.tab_3)
        self.listWidget_3.setObjectName(u"listWidget_3")

        self.verticalLayout_3.addWidget(self.listWidget_3)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_6.addWidget(self.tabWidget)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Dictionary)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dictionary)
    # setupUi

    def retranslateUi(self, Dictionary):
        Dictionary.setWindowTitle(QCoreApplication.translate("Dictionary", u"Dictionary", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dictionary", u"\uc790\uc5f0\uc5b4 \ucc98\ub9ac \uc635\uc158", None))
        self.opt_personal.setText(QCoreApplication.translate("Dictionary", u"\uac1c\uc778\uc815\ubcf4 \uc81c\uac70", None))
        self.opt_space.setText(QCoreApplication.translate("Dictionary", u"\ub744\uc5b4\uc4f0\uae30 \uad50\uc815", None))
        self.opt_sinmungo.setText(QCoreApplication.translate("Dictionary", u"\uad6d\ubbfc\uc2e0\ubb38\uace0, \uc548\uc804\uc2e0\ubb38\uace0 \uc790\ub3d9 \uc785\ub825 \ubb38\uc790 \uc81c\uac70", None))
        self.opt_special.setText(QCoreApplication.translate("Dictionary", u"\ud2b9\uc218 \ubb38\uc790, \uae30\ud638 \uc81c\uac70", None))
        self.opt_foriegn.setText(QCoreApplication.translate("Dictionary", u"\ud55c\uae00 \uc774\uc678 \ubb38\uc790 \uc81c\uac70 (\uc601\uc5b4, \ud55c\uc790 \ub4f1)", None))
        self.opt_num.setText(QCoreApplication.translate("Dictionary", u"\uc22b\uc790 \uc81c\uac70", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dictionary", u"AI \uc635\uc158", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dictionary", u"\ubaa8\ub378 \ub2e4\uc6b4\ub85c\ub4dc", None))
        self.label_6.setText(QCoreApplication.translate("Dictionary", u"\ucd5c\uc18c \ud1a0\ud53d \uac1c\uc218", None))
        self.label_4.setText(QCoreApplication.translate("Dictionary", u"\uc784\ubca0\ub529 \ubaa8\ub378 \uc704\uce58", None))
        self.toolButton_2.setText(QCoreApplication.translate("Dictionary", u"...", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dictionary", u"ollama AI \uc124\uc815", None))
        self.lineEdit.setText(QCoreApplication.translate("Dictionary", u"http://localhost:11434", None))
        self.toolButton.setText(QCoreApplication.translate("Dictionary", u"...", None))
        self.label_7.setText(QCoreApplication.translate("Dictionary", u"ollama \uc11c\ubc84", None))
        self.label.setText(QCoreApplication.translate("Dictionary", u"\ubd88\uc6a9\uc5b4\ub294 \ubd84\uc11d\uc5d0\uc11c \uc544\uc608 \uc81c\uc678\ud560 \ub2e8\uc5b4\ub97c \uc758\ubbf8\ud569\ub2c8\ub2e4. \ud14d\uc2a4\ud2b8 \ubd84\uc11d\uc774 \uc2dc\uc791\ub418\uae30 \uc804\uc5d0 \uc0ad\uc81c \ucc98\ub9ac\ub429\ub2c8\ub2e4.", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dictionary", u"\uc124\uba85", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dictionary", u"\ubd88\uc6a9\uc5b4", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem2 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dictionary", u"\uad6d\ubbfc\uc2e0\ubb38\uace0 \uc720\uc785", None));
        ___qtablewidgetitem3 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dictionary", u".*\ubbfc\uc6d0 \uc720\uc785 \uacbd\ub85c]", None));
        ___qtablewidgetitem4 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dictionary", u"\uc548\uc804\uc2e0\ubb38\uace0", None));
        ___qtablewidgetitem5 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dictionary", u"\uc548\uc804\uc2e0\ubb38\uace0 \uc2e0\uace0\ud30c\uc77c.*", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dictionary", u"\ubd88\uc6a9\uc5b4", None))
        self.label_2.setText(QCoreApplication.translate("Dictionary", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:2px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\uc0ac\uc6a9\uc790 \ub2e8\uc5b4\ub294 \ubd84\uc11d\uc5d0 \ucd94\uac00\ud558\uace0 \uc2f6\uc740 \ub2e8\uc5b4\uc758 \uc9d1\ud569\uc785\ub2c8\ub2e4. </p>\n"
"<p style=\" margin-top:2px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\uc77c\ubc18 \uc0ac\uc804\uc5d0 \uc4f0\uc774\uc9c0 \uc54a\uc740 \uc6b0\ub9ac \uacf5\uc0ac\uc5d0\uc11c\ub9cc \uc4f0"
                        "\uc774\ub294 \ub2e8\uc5b4\ub97c \ubd84\uc11d\uc5d0 \ud3ec\ud568\ud569\ub2c8\ub2e4.</p>\n"
"<p style=\" margin-top:2px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ex) \ud558\uc774\ud328\uc2a4, TCS, \ubc84\uc2a4\uc804\uc6a9\ucc28\ub85c</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dictionary", u"\uc0ac\uc6a9\uc790 \ub2e8\uc5b4", None))
        self.label_3.setText(QCoreApplication.translate("Dictionary", u"\ud14d\uc2a4\ud2b8\uc5d0\uc11c \ubcf4\uc774\ub294 \ub2e8\uc5b4\ub97c \uad50\uc815\ud569\ub2c8\ub2e4. \ud2b9\uc815 \ub2e8\uc5b4\uc758 \uc624\ud0c0\uac00 \uc790\uc8fc \ubc1c\uc0dd\ud560 \ub54c \uc720\uc6a9\ud569\ub2c8\ub2e4.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Dictionary", u"\uc624\ud0c8\uc790 \uad50\uc815", None))
    # retranslateUi

