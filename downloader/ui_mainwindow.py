# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 210)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(300, 210))
        MainWindow.setMaximumSize(QSize(300, 210))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.url = QLineEdit(self.centralwidget)
        self.url.setObjectName(u"url")
        self.url.setMinimumSize(QSize(0, 25))
        self.url.setStyleSheet(u"margin: 0 7px;")

        self.verticalLayout.addWidget(self.url)

        self.location = QLineEdit(self.centralwidget)
        self.location.setObjectName(u"location")
        self.location.setMinimumSize(QSize(0, 25))
        self.location.setStyleSheet(u"margin: 0 7px;")

        self.verticalLayout.addWidget(self.location)

        self.brows_btn = QPushButton(self.centralwidget)
        self.brows_btn.setObjectName(u"brows_btn")
        self.brows_btn.setMinimumSize(QSize(0, 25))
        self.brows_btn.setStyleSheet(u"margin: 0 7px;")

        self.verticalLayout.addWidget(self.brows_btn)

        self.progress_bar = QProgressBar(self.centralwidget)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setStyleSheet(u"margin: 0 7px;")
        self.progress_bar.setValue(0)
        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.progress_bar.setInvertedAppearance(False)

        self.verticalLayout.addWidget(self.progress_bar)

        self.download_btn = QPushButton(self.centralwidget)
        self.download_btn.setObjectName(u"download_btn")
        self.download_btn.setMinimumSize(QSize(0, 25))
        self.download_btn.setStyleSheet(u"margin: 0 7px;\n"
"")

        self.verticalLayout.addWidget(self.download_btn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 300, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyDownloader", None))
        self.url.setPlaceholderText(QCoreApplication.translate("MainWindow", u"URL", None))
        self.location.setPlaceholderText(QCoreApplication.translate("MainWindow", u"File save location", None))
        self.brows_btn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.download_btn.setText(QCoreApplication.translate("MainWindow", u"Download", None))
    # retranslateUi

