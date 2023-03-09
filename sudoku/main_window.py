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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(440, 470)
        MainWindow.setMinimumSize(QSize(440, 470))
        MainWindow.setMaximumSize(QSize(440, 470))
        MainWindow.setStyleSheet(u"")
        self.menu_new = QAction(MainWindow)
        self.menu_new.setObjectName(u"menu_new")
        self.menu_open_file = QAction(MainWindow)
        self.menu_open_file.setObjectName(u"menu_open_file")
        self.abbout = QAction(MainWindow)
        self.abbout.setObjectName(u"abbout")
        self.menu_exit = QAction(MainWindow)
        self.menu_exit.setObjectName(u"menu_exit")
        self.menu_help = QAction(MainWindow)
        self.menu_help.setObjectName(u"menu_help")
        self.menu_about = QAction(MainWindow)
        self.menu_about.setObjectName(u"menu_about")
        self.menu_help_ = QAction(MainWindow)
        self.menu_help_.setObjectName(u"menu_help_")
        self.menu_solve = QAction(MainWindow)
        self.menu_solve.setObjectName(u"menu_solve")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 421, 371))
        self.grid_layout = QGridLayout(self.gridLayoutWidget)
        self.grid_layout.setObjectName(u"grid_layout")
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.color_mood_btn = QPushButton(self.centralwidget)
        self.color_mood_btn.setObjectName(u"color_mood_btn")
        self.color_mood_btn.setGeometry(QRect(159, 390, 121, 31))
        self.color_mood_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_mood_btn.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border-radius: 6px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 440, 22))
        self.menuGame = QMenu(self.menubar)
        self.menuGame.setObjectName(u"menuGame")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuGame.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuGame.addAction(self.menu_new)
        self.menuGame.addAction(self.menu_open_file)
        self.menuGame.addAction(self.menu_about)
        self.menuGame.addAction(self.menu_exit)
        self.menuHelp.addAction(self.menu_help_)
        self.menuHelp.addAction(self.menu_solve)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sudoku Game", None))
        self.menu_new.setText(QCoreApplication.translate("MainWindow", u"New...", None))
        self.menu_open_file.setText(QCoreApplication.translate("MainWindow", u"Open File...", None))
        self.abbout.setText(QCoreApplication.translate("MainWindow", u"about", None))
        self.menu_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.menu_help.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menu_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.menu_help_.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menu_solve.setText(QCoreApplication.translate("MainWindow", u"Solve", None))
        self.color_mood_btn.setText(QCoreApplication.translate("MainWindow", u"Change Color Mood", None))
        self.menuGame.setTitle(QCoreApplication.translate("MainWindow", u"Game", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

