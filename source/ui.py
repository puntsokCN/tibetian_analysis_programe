# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(867, 269)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("language_128px_1233037_easyicon.net.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_text = QtWidgets.QWidget(self.centralwidget)
        self.widget_text.setObjectName("widget_text")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_text)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit_input = QtWidgets.QTextEdit(self.widget_text)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_input.sizePolicy().hasHeightForWidth())
        self.textEdit_input.setSizePolicy(sizePolicy)
        self.textEdit_input.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_input.setObjectName("textEdit_input")
        self.horizontalLayout.addWidget(self.textEdit_input)
        self.frame = QtWidgets.QFrame(self.widget_text)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout.addWidget(self.frame)
        self.textBrowser_rec = QtWidgets.QTextBrowser(self.widget_text)
        self.textBrowser_rec.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser_rec.setObjectName("textBrowser_rec")
        self.horizontalLayout.addWidget(self.textBrowser_rec)
        self.verticalLayout.addWidget(self.widget_text)
        self.widget_button = QtWidgets.QWidget(self.centralwidget)
        self.widget_button.setObjectName("widget_button")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_button)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_analysis_aux = QtWidgets.QPushButton(self.widget_button)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_analysis_aux.sizePolicy().hasHeightForWidth())
        self.button_analysis_aux.setSizePolicy(sizePolicy)
        self.button_analysis_aux.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_analysis_aux.setAutoFillBackground(False)
        self.button_analysis_aux.setObjectName("button_analysis_aux")
        self.horizontalLayout_2.addWidget(self.button_analysis_aux)
        self.button_analysis_verb = QtWidgets.QPushButton(self.widget_button)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_analysis_verb.sizePolicy().hasHeightForWidth())
        self.button_analysis_verb.setSizePolicy(sizePolicy)
        self.button_analysis_verb.setAutoFillBackground(False)
        self.button_analysis_verb.setObjectName("button_analysis_verb")
        self.horizontalLayout_2.addWidget(self.button_analysis_verb)
        self.verticalLayout.addWidget(self.widget_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 867, 23))
        self.menubar.setObjectName("menubar")
        self.menu_font = QtWidgets.QMenu(self.menubar)
        self.menu_font.setObjectName("menu_font")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        self.menu_quit = QtWidgets.QMenu(self.menubar)
        self.menu_quit.setObjectName("menu_quit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionchange_Font = QtWidgets.QAction(MainWindow)
        self.actionchange_Font.setObjectName("actionchange_Font")
        self.actionhelp = QtWidgets.QAction(MainWindow)
        self.actionhelp.setObjectName("actionhelp")
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.actionquit = QtWidgets.QAction(MainWindow)
        self.actionquit.setObjectName("actionquit")
        self.actionyuyan = QtWidgets.QAction(MainWindow)
        self.actionyuyan.setObjectName("actionyuyan")
        self.actiondf = QtWidgets.QAction(MainWindow)
        self.actiondf.setObjectName("actiondf")
        self.actiongithub = QtWidgets.QAction(MainWindow)
        self.actiongithub.setObjectName("actiongithub")
        self.menu_font.addAction(self.actionchange_Font)
        self.menu_help.addAction(self.actionhelp)
        self.menu_help.addAction(self.actiongithub)
        self.menu_quit.addAction(self.actionquit)
        self.menubar.addAction(self.menu_font.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menubar.addAction(self.menu_quit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "藏文助词动词分析器 v1.0.0"))
        self.button_analysis_aux.setText(_translate("MainWindow", "开始助词分析"))
        self.button_analysis_verb.setText(_translate("MainWindow", "开始动词分析"))
        self.menu_font.setTitle(_translate("MainWindow", "字体"))
        self.menu_help.setTitle(_translate("MainWindow", "帮助"))
        self.menu_quit.setTitle(_translate("MainWindow", "退出"))
        self.actionchange_Font.setText(_translate("MainWindow", "字体"))
        self.actionhelp.setText(_translate("MainWindow", "码云"))
        self.actionabout.setText(_translate("MainWindow", "关于"))
        self.actionquit.setText(_translate("MainWindow", "退出"))
        self.actionyuyan.setText(_translate("MainWindow", "界面语言"))
        self.actiondf.setText(_translate("MainWindow", "界面语言"))
        self.actiongithub.setText(_translate("MainWindow", "github"))
