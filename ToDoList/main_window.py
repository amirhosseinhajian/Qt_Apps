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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QFrame,
    QGridLayout, QHBoxLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(313, 600)
        MainWindow.setMinimumSize(QSize(312, 600))
        MainWindow.setMaximumSize(QSize(313, 600))
        MainWindow.setStyleSheet(u"background-color: #045757;\n"
"color: white;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_8 = QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.new_task_title = QLineEdit(self.centralwidget)
        self.new_task_title.setObjectName(u"new_task_title")
        self.new_task_title.setMinimumSize(QSize(93, 0))

        self.gridLayout_8.addWidget(self.new_task_title, 6, 2, 1, 2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout_8.addWidget(self.line, 4, 0, 1, 4)

        self.new_task_descryption = QTextEdit(self.centralwidget)
        self.new_task_descryption.setObjectName(u"new_task_descryption")
        self.new_task_descryption.setMaximumSize(QSize(16777215, 75))

        self.gridLayout_8.addWidget(self.new_task_descryption, 7, 0, 1, 4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.new_task_btn = QPushButton(self.centralwidget)
        self.new_task_btn.setObjectName(u"new_task_btn")
        self.new_task_btn.setMaximumSize(QSize(40, 40))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.new_task_btn.setFont(font)
        self.new_task_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_task_btn.setStyleSheet(u"background-color: orange;\n"
"color: white;\n"
"border-radius: 20px;")

        self.horizontalLayout.addWidget(self.new_task_btn)


        self.gridLayout_8.addLayout(self.horizontalLayout, 8, 0, 1, 4)

        self.tasks_gl = QGridLayout()
        self.tasks_gl.setObjectName(u"tasks_gl")

        self.gridLayout_8.addLayout(self.tasks_gl, 0, 0, 3, 4)

        self.dateTimeEdit = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setMinimumSize(QSize(130, 0))
        self.dateTimeEdit.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_8.addWidget(self.dateTimeEdit, 6, 0, 1, 1)

        self.select = QComboBox(self.centralwidget)
        self.select.addItem("")
        self.select.addItem("")
        self.select.addItem("")
        self.select.setObjectName(u"select")
        self.select.setMinimumSize(QSize(60, 0))
        self.select.setEditable(False)

        self.gridLayout_8.addWidget(self.select, 6, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer, 3, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 313, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ToDoList", None))
        self.new_task_title.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0639\u0646\u0648\u0627\u0646...", None))
        self.new_task_descryption.setPlaceholderText(QCoreApplication.translate("MainWindow", u"descryption...", None))
        self.new_task_btn.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.select.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0639\u0627\u062f\u06cc", None))
        self.select.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0645\u062a\u0648\u0633\u0637", None))
        self.select.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0628\u062d\u0631\u0627\u0646\u06cc", None))

        self.select.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u0648\u0644\u0648\u06cc\u062a", None))
    # retranslateUi

