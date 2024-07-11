# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FileInput.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)

class Ui_FileInput(object):
    def setupUi(self, FileInput):
        if not FileInput.objectName():
            FileInput.setObjectName(u"FileInput")
        FileInput.resize(847, 502)
        self.gridLayout = QGridLayout(FileInput)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tableView = QTableView(FileInput)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setMinimumSize(QSize(300, 300))
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setGridStyle(Qt.PenStyle.DotLine)
        self.tableView.setSortingEnabled(True)

        self.gridLayout.addWidget(self.tableView, 1, 1, 1, 1)

        self.groupBox = QGroupBox(FileInput)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(300, 300))
        self.groupBox.setMaximumSize(QSize(300, 16777215))
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 0, 10, 0)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.label)

        self.fileBtn = QPushButton(self.groupBox)
        self.fileBtn.setObjectName(u"fileBtn")
        self.fileBtn.setMinimumSize(QSize(0, 60))
        self.fileBtn.setAutoFillBackground(False)
        self.fileBtn.setStyleSheet(u"font-size: 15px;\n"
"font-weight: 600;\n"
"border-radius: 4px;\n"
"border-width: 0;\n"
"background-color: #242a35;\n"
"color: white;\n"
"border: solid 1px #e8e8e82d;")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FolderVisiting))
        self.fileBtn.setIcon(icon)

        self.verticalLayout.addWidget(self.fileBtn)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.label_3)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setTextFormat(Qt.TextFormat.RichText)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_4)

        self.dataLabel = QLabel(self.groupBox)
        self.dataLabel.setObjectName(u"dataLabel")
        self.dataLabel.setMidLineWidth(0)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.dataLabel)

        self.DateCol = QComboBox(self.groupBox)
        self.DateCol.setObjectName(u"DateCol")
        self.DateCol.setMinimumSize(QSize(150, 0))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.DateCol)

        self.textLabel = QLabel(self.groupBox)
        self.textLabel.setObjectName(u"textLabel")
        self.textLabel.setTextFormat(Qt.TextFormat.RichText)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.textLabel)

        self.TextCol = QComboBox(self.groupBox)
        self.TextCol.setObjectName(u"TextCol")
        self.TextCol.setMinimumSize(QSize(150, 0))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.TextCol)

        self.Label = QLabel(self.groupBox)
        self.Label.setObjectName(u"Label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.Label)

        self.category1ComboBox = QComboBox(self.groupBox)
        self.category1ComboBox.setObjectName(u"category1ComboBox")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.category1ComboBox)

        self.Label_2 = QLabel(self.groupBox)
        self.Label_2.setObjectName(u"Label_2")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.Label_2)

        self.category2ComboBox = QComboBox(self.groupBox)
        self.category2ComboBox.setObjectName(u"category2ComboBox")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.category2ComboBox)

        self.Label_3 = QLabel(self.groupBox)
        self.Label_3.setObjectName(u"Label_3")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.Label_3)

        self.category3ComboBox = QComboBox(self.groupBox)
        self.category3ComboBox.setObjectName(u"category3ComboBox")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.category3ComboBox)

        self.Label_4 = QLabel(self.groupBox)
        self.Label_4.setObjectName(u"Label_4")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.Label_4)

        self.removeDupCheckBox = QCheckBox(self.groupBox)
        self.removeDupCheckBox.setObjectName(u"removeDupCheckBox")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.removeDupCheckBox)

        self.Label_5 = QLabel(self.groupBox)
        self.Label_5.setObjectName(u"Label_5")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.Label_5)

        self.removeNanCheckBox = QCheckBox(self.groupBox)
        self.removeNanCheckBox.setObjectName(u"removeNanCheckBox")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.removeNanCheckBox)

        self.line_3 = QFrame(self.groupBox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.line_3)

        self.line_4 = QFrame(self.groupBox)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout.setWidget(7, QFormLayout.SpanningRole, self.line_4)


        self.verticalLayout.addLayout(self.formLayout)

        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.setCols = QPushButton(self.groupBox)
        self.setCols.setObjectName(u"setCols")
        self.setCols.setMinimumSize(QSize(0, 50))
        self.setCols.setStyleSheet(u"font-size: 15px;\n"
"font-weight: 600;\n"
"border-radius: 4px;\n"
"border-width: 0;\n"
"background-color: #21dc62;\n"
"color: white;\n"
"border: solid 1px #e8e8e82d;")

        self.verticalLayout.addWidget(self.setCols)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        QWidget.setTabOrder(self.fileBtn, self.DateCol)
        QWidget.setTabOrder(self.DateCol, self.TextCol)
        QWidget.setTabOrder(self.TextCol, self.category1ComboBox)
        QWidget.setTabOrder(self.category1ComboBox, self.category2ComboBox)
        QWidget.setTabOrder(self.category2ComboBox, self.category3ComboBox)
        QWidget.setTabOrder(self.category3ComboBox, self.removeDupCheckBox)
        QWidget.setTabOrder(self.removeDupCheckBox, self.removeNanCheckBox)
        QWidget.setTabOrder(self.removeNanCheckBox, self.setCols)
        QWidget.setTabOrder(self.setCols, self.tableView)

        self.retranslateUi(FileInput)

        QMetaObject.connectSlotsByName(FileInput)
    # setupUi

    def retranslateUi(self, FileInput):
        FileInput.setWindowTitle(QCoreApplication.translate("FileInput", u"Form", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("FileInput", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">\ud14d\uc2a4\ud2b8 \ub370\uc774\ud130 \ubd84\uc11d\uae30</span><span style=\" font-size:12pt; vertical-align:sub;\">(24.07)</span></p></body></html>", None))
        self.fileBtn.setText(QCoreApplication.translate("FileInput", u"\ud14d\uc2a4\ud2b8 \ud30c\uc77c \ubd88\ub7ec\uc624\uae30 (Ctrl + O)\n"
".xlsx, .xls, .csv", None))
#if QT_CONFIG(shortcut)
        self.fileBtn.setShortcut(QCoreApplication.translate("FileInput", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.label_2.setText(QCoreApplication.translate("FileInput", u"\ud30c\uc77c\uba85 : ", None))
        self.label_3.setText(QCoreApplication.translate("FileInput", u"\ud589 \uac1c\uc218 : ", None))
        self.label_4.setText(QCoreApplication.translate("FileInput", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">\ubd84\uc11d \uae30\ubcf8 \uc124\uc815</span></p></body></html>", None))
        self.dataLabel.setText(QCoreApplication.translate("FileInput", u"<html><head/><body><p><span style=\" font-weight:700;\">\uc77c\uc790 \ud544\ub4dc :</span></p></body></html>", None))
        self.textLabel.setText(QCoreApplication.translate("FileInput", u"<html><head/><body><p><span style=\" font-weight:700;\">\ubb38\uc790 \ud544\ub4dc :</span></p></body></html>", None))
        self.Label.setText(QCoreApplication.translate("FileInput", u"\ub300\ubd84\ub958 :", None))
        self.Label_2.setText(QCoreApplication.translate("FileInput", u"\uc911\ubd84\ub958 :", None))
        self.Label_3.setText(QCoreApplication.translate("FileInput", u"\uc18c\ubd84\ub958", None))
#if QT_CONFIG(tooltip)
        self.Label_4.setToolTip(QCoreApplication.translate("FileInput", u"<html><head/><body><p>\ub370\uc774\ud130\uc5d0\uc11c \uc911\ubcf5\ub41c \ud589\uc744 \uc81c\uac70\ud558\uace0 \ubd84\uc11d\ud560 \uac83\uc778\uc9c0 \uc5ec\ubd80</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Label_4.setText(QCoreApplication.translate("FileInput", u"\uc911\ubcf5 \uc81c\uac70", None))
        self.Label_5.setText(QCoreApplication.translate("FileInput", u"\uacb0\uce21\uce58 \uc81c\uac70", None))
        self.setCols.setText(QCoreApplication.translate("FileInput", u"\uc124\uc815\ud558\uae30", None))
#if QT_CONFIG(shortcut)
        self.setCols.setShortcut(QCoreApplication.translate("FileInput", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

