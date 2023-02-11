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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 500)
        MainWindow.setMinimumSize(QSize(600, 500))
        MainWindow.setMaximumSize(QSize(600, 500))
        MainWindow.setStyleSheet(u"background-color: #d1ccc0;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(9, 236, 225, 22))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(9, 10, 422, 44))
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(9, 256, 412, 22))
        self.label_3.setFont(font1)
        self.remove_btn = QPushButton(self.centralwidget)
        self.remove_btn.setObjectName(u"remove_btn")
        self.remove_btn.setGeometry(QRect(10, 190, 141, 31))
        self.remove_btn.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setPointSize(10)
        self.remove_btn.setFont(font2)
        self.remove_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.remove_btn.setStyleSheet(u"background-color: #e67e22;\n"
"color: white;\n"
"border-radius: 8px;")
        self.reset_btn = QPushButton(self.centralwidget)
        self.reset_btn.setObjectName(u"reset_btn")
        self.reset_btn.setGeometry(QRect(180, 190, 75, 31))
        self.reset_btn.setMinimumSize(QSize(0, 30))
        self.reset_btn.setFont(font2)
        self.reset_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.reset_btn.setStyleSheet(u"background-color: #e67e22;\n"
"color: white;\n"
"border-radius: 8px;")
        self.copy_btn = QPushButton(self.centralwidget)
        self.copy_btn.setObjectName(u"copy_btn")
        self.copy_btn.setGeometry(QRect(10, 418, 141, 31))
        self.copy_btn.setMinimumSize(QSize(0, 30))
        self.copy_btn.setFont(font2)
        self.copy_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.copy_btn.setStyleSheet(u"background-color: #2980b9;\n"
"color: white;\n"
"border-radius: 8px;")
        self.plain_text = QPlainTextEdit(self.centralwidget)
        self.plain_text.setObjectName(u"plain_text")
        self.plain_text.setGeometry(QRect(10, 60, 581, 121))
        font3 = QFont()
        font3.setPointSize(11)
        self.plain_text.setFont(font3)
        self.plain_text.setStyleSheet(u"background-color: white;")
        self.clear_text = QPlainTextEdit(self.centralwidget)
        self.clear_text.setObjectName(u"clear_text")
        self.clear_text.setGeometry(QRect(10, 287, 581, 111))
        self.clear_text.setFont(font3)
        self.clear_text.setStyleSheet(u"background-color: white;")
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Remove Line Breaks", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"New Text without Line Breaks", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Paste your text in the box below and then click the button.\n"
"The new text will appear in the box at the bottom of the page.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Copy your new text without line breaks from the box below.", None))
        self.remove_btn.setText(QCoreApplication.translate("MainWindow", u"Remove Line Breaks", None))
        self.reset_btn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.copy_btn.setText(QCoreApplication.translate("MainWindow", u"Copy to Clipboard", None))
        self.plain_text.setPlainText("")
    # retranslateUi

