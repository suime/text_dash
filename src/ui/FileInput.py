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
from PySide6.QtQuickWidgets import QQuickWidget
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QGroupBox, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_FileInput(object):
    def setupUi(self, FileInput):
        if not FileInput.objectName():
            FileInput.setObjectName(u"FileInput")
        FileInput.resize(886, 459)
        self.gridLayout = QGridLayout(FileInput)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(FileInput)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(300, 300))

        self.gridLayout.addWidget(self.tableWidget, 1, 1, 1, 1)

        self.groupBox = QGroupBox(FileInput)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(300, 300))
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

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FolderVisiting))
        self.pushButton.setIcon(icon)

        self.verticalLayout.addWidget(self.pushButton)

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

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.dataLabel = QLabel(self.groupBox)
        self.dataLabel.setObjectName(u"dataLabel")
        self.dataLabel.setMidLineWidth(0)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.dataLabel)

        self.DateCol = QComboBox(self.groupBox)
        self.DateCol.setObjectName(u"DateCol")
        self.DateCol.setMinimumSize(QSize(150, 0))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.DateCol)

        self.textLabel = QLabel(self.groupBox)
        self.textLabel.setObjectName(u"textLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.textLabel)

        self.TextCol = QComboBox(self.groupBox)
        self.TextCol.setObjectName(u"TextCol")
        self.TextCol.setMinimumSize(QSize(150, 0))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.TextCol)

        self.Label = QLabel(self.groupBox)
        self.Label.setObjectName(u"Label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.Label)

        self.QuickWidget = QQuickWidget(self.groupBox)
        self.QuickWidget.setObjectName(u"QuickWidget")
        self.QuickWidget.setMinimumSize(QSize(150, 0))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.QuickWidget)


        self.verticalLayout.addLayout(self.formLayout)

        self.colSetBtn = QPushButton(self.groupBox)
        self.colSetBtn.setObjectName(u"colSetBtn")
        self.colSetBtn.setMinimumSize(QSize(0, 50))
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AddressBookNew))
        self.colSetBtn.setIcon(icon1)

        self.verticalLayout.addWidget(self.colSetBtn)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)


        self.retranslateUi(FileInput)
        self.colSetBtn.clicked.connect(self.tableWidget.repaint)

        QMetaObject.connectSlotsByName(FileInput)
    # setupUi

    def retranslateUi(self, FileInput):
        FileInput.setWindowTitle(QCoreApplication.translate("FileInput", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("FileInput", u"\ud30c\uc77c \uc785\ub825", None))
        self.label.setText(QCoreApplication.translate("FileInput", u"\ud14d\uc2a4\ud2b8 \ud30c\uc77c\uc744 \uc785\ub825\ud558\uc138\uc694.", None))
        self.pushButton.setText(QCoreApplication.translate("FileInput", u"\ud14d\uc2a4\ud2b8 \ud30c\uc77c \ubd88\ub7ec\uc624\uae30", None))
#if QT_CONFIG(shortcut)
        self.pushButton.setShortcut(QCoreApplication.translate("FileInput", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.label_2.setText(QCoreApplication.translate("FileInput", u"\ud30c\uc77c\uba85 : ", None))
        self.label_3.setText(QCoreApplication.translate("FileInput", u"\ud589 \uac1c\uc218 : ", None))
        self.dataLabel.setText(QCoreApplication.translate("FileInput", u"\uc77c\uc790 \ud544\ub4dc :", None))
        self.textLabel.setText(QCoreApplication.translate("FileInput", u"\ubb38\uc790 \ud544\ub4dc :", None))
        self.Label.setText(QCoreApplication.translate("FileInput", u"\ubd84\ub958 \ud544\ub4dc :", None))
        self.colSetBtn.setText(QCoreApplication.translate("FileInput", u"\uc5f4 \uc124\uc815\ud558\uae30", None))
#if QT_CONFIG(shortcut)
        self.colSetBtn.setShortcut(QCoreApplication.translate("FileInput", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

