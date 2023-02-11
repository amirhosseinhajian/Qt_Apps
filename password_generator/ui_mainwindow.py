# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'front.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 500)
        MainWindow.setMinimumSize(QSize(600, 500))
        MainWindow.setMaximumSize(QSize(600, 500))
        MainWindow.setStyleSheet(u"background-color: #8E24AA;\n"
"padding: 0 7px;\n"
"color: white;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"images/qt.png"))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.password = QLineEdit(self.centralwidget)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(0, 37))
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.password.setFont(font)
        self.password.setFocusPolicy(Qt.ClickFocus)
        self.password.setStyleSheet(u"border-radius: 8px;\n"
"background-color: white;\n"
"color: black;")

        self.horizontalLayout.addWidget(self.password)

        self.generate_btn = QPushButton(self.centralwidget)
        self.generate_btn.setObjectName(u"generate_btn")
        self.generate_btn.setMinimumSize(QSize(0, 40))
        self.generate_btn.setMaximumSize(QSize(100, 16777215))
        font1 = QFont()
        font1.setPointSize(12)
        self.generate_btn.setFont(font1)
        self.generate_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.generate_btn.setStyleSheet(u"background-color: #4A148C;\n"
"border-radius: 8px;")

        self.horizontalLayout.addWidget(self.generate_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.strong_password_btn = QRadioButton(self.centralwidget)
        self.strong_password_btn.setObjectName(u"strong_password_btn")
        self.strong_password_btn.setChecked(True)

        self.verticalLayout.addWidget(self.strong_password_btn)

        self.extera_strong_password_btn = QRadioButton(self.centralwidget)
        self.extera_strong_password_btn.setObjectName(u"extera_strong_password_btn")

        self.verticalLayout.addWidget(self.extera_strong_password_btn)

        self.super_strong_password_btn = QRadioButton(self.centralwidget)
        self.super_strong_password_btn.setObjectName(u"super_strong_password_btn")

        self.verticalLayout.addWidget(self.super_strong_password_btn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Generator", None))
        self.label.setText("")
        self.password.setText("")
        self.generate_btn.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.strong_password_btn.setText(QCoreApplication.translate("MainWindow", u"Generate a Standard Strength Password", None))
        self.extera_strong_password_btn.setText(QCoreApplication.translate("MainWindow", u"Generate an Extra Strong Password", None))
        self.super_strong_password_btn.setText(QCoreApplication.translate("MainWindow", u"Generate a Super Strong Password", None))
    # retranslateUi

