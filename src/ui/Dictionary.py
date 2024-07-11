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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Dictionary(object):
    def setupUi(self, Dictionary):
        if not Dictionary.objectName():
            Dictionary.setObjectName(u"Dictionary")
        Dictionary.resize(994, 600)
        Dictionary.setMinimumSize(QSize(600, 600))
        self.horizontalLayout = QHBoxLayout(Dictionary)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setContentsMargins(-1, -1, -1, 10)
        self.groupBox = QGroupBox(Dictionary)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(300, 0))
        self.groupBox.setMaximumSize(QSize(300, 16777215))
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_2.addWidget(self.checkBox_2, 2, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_2.addWidget(self.checkBox_3, 0, 0, 1, 1)

        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.gridLayout_2.addWidget(self.checkBox, 1, 0, 1, 1)

        self.checkBox_4 = QCheckBox(self.groupBox)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setChecked(True)

        self.gridLayout_2.addWidget(self.checkBox_4, 3, 0, 1, 1)

        self.checkBox_5 = QCheckBox(self.groupBox)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setChecked(True)

        self.gridLayout_2.addWidget(self.checkBox_5, 4, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(Dictionary)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)


        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(Dictionary)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton = QPushButton(self.groupBox_3)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_3, 2, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.tabWidget = QTabWidget(Dictionary)
        self.tabWidget.setObjectName(u"tabWidget")
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

        self.horizontalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Dictionary)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dictionary)
    # setupUi

    def retranslateUi(self, Dictionary):
        Dictionary.setWindowTitle(QCoreApplication.translate("Dictionary", u"Dictionary", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dictionary", u"\uc790\uc5f0\uc5b4 \ucc98\ub9ac \uc635\uc158", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dictionary", u"\ud55c\uae00 \uc774\uc678 \ubb38\uc790 \uc81c\uac70 (\uc601\uc5b4, \ud55c\uc790 \ub4f1)", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dictionary", u"\ub744\uc5b4\uc4f0\uae30 \uad50\uc815", None))
        self.checkBox.setText(QCoreApplication.translate("Dictionary", u"\ud2b9\uc218 \ubb38\uc790, \uae30\ud638 \uc81c\uac70", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dictionary", u"\uac1c\uc778\uc815\ubcf4 \uc81c\uac70", None))
        self.checkBox_5.setText(QCoreApplication.translate("Dictionary", u"\uad6d\ubbfc\uc2e0\ubb38\uace0, \uc548\uc804\uc2e0\ubb38\uace0 \uc790\ub3d9 \uc785\ub825 \ubb38\uc790 \uc81c\uac70", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dictionary", u"GroupBox", None))
        self.label_4.setText(QCoreApplication.translate("Dictionary", u"\uc5ec\uae30\ub294 \ub9cc\ub4dc\ub294 \uc911\uc785\ub2c8\ub2e4.", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dictionary", u"\uc124\uc815", None))
        self.pushButton.setText(QCoreApplication.translate("Dictionary", u"\uc124\uc815 \ub0b4\ubcf4\ub0b4\uae30", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dictionary", u"\uc124\uc815 \ubd88\ub7ec\uc624\uae30", None))
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
        self.label_2.setText(QCoreApplication.translate("Dictionary", u"\uc0ac\uc6a9\uc790 \ub2e8\uc5b4\ub294 \ubd84\uc11d\uc5d0 \ucd94\uac00\ud558\uace0 \uc2f6\uc740 \ub2e8\uc5b4\uc758 \uc9d1\ud569\uc785\ub2c8\ub2e4.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dictionary", u"\uc0ac\uc6a9\uc790 \ub2e8\uc5b4", None))
        self.label_3.setText(QCoreApplication.translate("Dictionary", u"\ud14d\uc2a4\ud2b8\uc5d0\uc11c \ubcf4\uc774\ub294 \ub2e8\uc5b4\ub97c \uad50\uc815\ud569\ub2c8\ub2e4. \ud2b9\uc815 \ub2e8\uc5b4\uc758 \uc624\ud0c0\uac00 \uc790\uc8fc \ubc1c\uc0dd\ud560 \ub54c \uc720\uc6a9\ud569\ub2c8\ub2e4.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Dictionary", u"\uc624\ud0c8\uc790 \uad50\uc815", None))
    # retranslateUi

