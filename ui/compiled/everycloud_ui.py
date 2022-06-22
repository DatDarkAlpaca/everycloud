# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'everycloud.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_EveryCloud(object):
    def setupUi(self, EveryCloud):
        if not EveryCloud.objectName():
            EveryCloud.setObjectName(u"EveryCloud")
        EveryCloud.resize(480, 450)
        EveryCloud.setMinimumSize(QSize(480, 450))
        self.central_widget = QWidget(EveryCloud)
        self.central_widget.setObjectName(u"central_widget")
        self.verticalLayout = QVBoxLayout(self.central_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(self.central_widget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setStyleSheet(u"QFrame#main_frame\n"
"{\n"
"	background-color: rgb(24, 45, 60);\n"
"}")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.titlebar = QFrame(self.main_frame)
        self.titlebar.setObjectName(u"titlebar")
        self.titlebar.setMaximumSize(QSize(16777215, 30))
        self.titlebar.setFrameShape(QFrame.NoFrame)
        self.titlebar.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.titlebar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.title_label = QLabel(self.titlebar)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMinimumSize(QSize(0, 30))
        self.title_label.setMaximumSize(QSize(16777215, 30))
        self.title_label.setStyleSheet(u"background-color: rgb(46, 172, 104);\n"
"color: white")

        self.horizontalLayout_2.addWidget(self.title_label)

        self.settings_button = QToolButton(self.titlebar)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setMinimumSize(QSize(45, 30))
        self.settings_button.setMaximumSize(QSize(45, 30))
        font = QFont()
        font.setBold(True)
        self.settings_button.setFont(font)
        self.settings_button.setStyleSheet(u"QToolButton\n"
"{\n"
"	background-color: rgb(46, 172, 104);\n"
"	border: 0px;\n"
"	color: white;\n"
"}\n"
"QToolButton:hover\n"
"{\n"
"	background-color: rgb(58, 203, 123);\n"
"}\n"
"QToolButton:pressed\n"
"{\n"
"	background-color: rgb(101, 214, 152);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.settings_button)

        self.minimize_button = QToolButton(self.titlebar)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setMinimumSize(QSize(45, 30))
        self.minimize_button.setMaximumSize(QSize(45, 30))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        self.minimize_button.setFont(font1)
        self.minimize_button.setStyleSheet(u"QToolButton\n"
"{\n"
"	background-color: rgb(46, 172, 104);\n"
"	border: 0px;\n"
"	color: white;\n"
"}\n"
"QToolButton:hover\n"
"{\n"
"	background-color: rgb(58, 203, 123);\n"
"}\n"
"QToolButton:pressed\n"
"{\n"
"	background-color: rgb(101, 214, 152);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.minimize_button)

        self.close_button = QToolButton(self.titlebar)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMinimumSize(QSize(45, 30))
        self.close_button.setMaximumSize(QSize(45, 30))
        self.close_button.setFont(font1)
        self.close_button.setStyleSheet(u"QToolButton\n"
"{\n"
"	background-color: rgb(46, 172, 104);\n"
"	border: 0px;\n"
"	color: white;\n"
"}\n"
"QToolButton:hover\n"
"{\n"
"	background-color: rgb(58, 203, 123);\n"
"}\n"
"QToolButton:pressed\n"
"{\n"
"	background-color: rgb(241, 112, 122);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.close_button)


        self.verticalLayout_2.addWidget(self.titlebar)

        self.vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_2.addItem(self.vertical_spacer)


        self.verticalLayout.addWidget(self.main_frame)

        EveryCloud.setCentralWidget(self.central_widget)

        self.retranslateUi(EveryCloud)
        self.close_button.released.connect(EveryCloud.close)
        self.minimize_button.released.connect(EveryCloud.hide)

        QMetaObject.connectSlotsByName(EveryCloud)
    # setupUi

    def retranslateUi(self, EveryCloud):
        EveryCloud.setWindowTitle(QCoreApplication.translate("EveryCloud", u"MainWindow", None))
        self.title_label.setText(QCoreApplication.translate("EveryCloud", u"   EveryCloud", None))
        self.settings_button.setText(QCoreApplication.translate("EveryCloud", u"\ue712", None))
        self.minimize_button.setText(QCoreApplication.translate("EveryCloud", u"\ue738", None))
        self.close_button.setText(QCoreApplication.translate("EveryCloud", u"\ue711", None))
    # retranslateUi

