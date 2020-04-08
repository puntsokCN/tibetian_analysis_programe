#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import analysis
from ui import Ui_MainWindow
from os import getcwd
from sqlite3 import connect
from webbrowser import  get, open_new_tab
from PyQt5.QtWidgets import  QFontDialog, QMessageBox, QApplication, QMainWindow, QFontDialog
from PyQt5.QtCore import QCoreApplication



class MyPyQT_Form(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MyPyQT_Form, self).__init__()
        self.setupUi(self)

    def retranslateUi(self, MainWindow):
        """
        连接控件和槽函数
        Parameters
        ----------
        MainWindow

        Returns
        -------

        """
        super(MyPyQT_Form, self).retranslateUi(self)
        # --------- code here ----------
        # Menu
        self.actionchange_Font.triggered.connect(self.font_func)  # 设置字体
        self.actionhelp.triggered.connect(self.help_func)  # 设置帮助
        self.actionquit.triggered.connect(self.quit_func)  # 设置退出
        # Button
        self.button_analysis_aux.clicked.connect(self.analysis_aux_func)
        self.button_analysis_verb.clicked.connect(self.analysis_verb_func)

    # ------------------------------------------------------------------------------
    # 槽函数
    def font_func(self):
        """
        修改textEdit区域的字体设置
        Returns
        -------
        """

        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit_input.setFont(font)
            self.textBrowser_rec.setFont(font)

    def help_func(self):
        """
        显示帮助窗口
        Returns
        -------
        """
        url = "https://gitee.com/ahgey/tibetan_analysis_programe/blob/master/README.md"
        try:
            get('chrome').open_new_tab(url)
        except Exception as e:
            open_new_tab(url)


    def quit_func(self):
        """
        退出函数
        :return:
        """
        choice = QMessageBox.question(self, '退出', '您确定退出吗？',
                                                QMessageBox.Close | QMessageBox.Cancel)
        if choice == QMessageBox.Close:
            QCoreApplication.instance().quit()
        if choice == QMessageBox.Cancel:
            pass

    def analysis_aux_func(self):
        """
        助词分析按钮槽函数
        Returns
        -------
        """
        str = self.textEdit_input.toPlainText()
        res = analysis.Auxiliary_Word(str).analysis()

        self.textBrowser_rec.setText(res)

    def analysis_verb_func(self):
        """
        动词分析按钮槽函数
        Returns
        -------
        """
        # 一、获取文本
        str = self.textEdit_input.toPlainText()
        # 二、数据库查询
        word = [str]  # 必须以列表的形式才能查询
        conn = connect(getcwd() + r"\Verb.db")  # 在其他地方需要完整的路径
        curs = conn.cursor()  # 创建1个游标 用作提交SQL语句
        store = []  # 数据库查询结果缓存
        for col_name in ['present', 'past', 'future', 'command']:  # 在每个列里寻找存在目标值的行
            cmd = "select * from verb where {}=?".format(col_name)
            curs.execute(cmd, word)
            res = curs.fetchall() 
            if len(res) == 1 or len(res) > 1:  # 找到存在此动词的1行数据 
                store.append(res)
        # print("1:", store)
        # 三、对缓存进行去重 、存到result中
        result = list()
        for i in store:
            if i not in result:
                result.append(i)
        # print("2:", result)
        # print("3:", len(result[0]))
        # print( result[0][0][3] )
        # 四、设计输出
        set_text = ""
        if len(result) == 0:  # 如果查询为空
            self.textBrowser_rec.setText("བྱ་ཚིག་འདི་རེའུ་མིག་ནང་མིན་འདུག་།")
        else:
            for i in range(len(result[0])):
                # print("4:", result[0][i][3])  
                if result[0][i][3] == None:  # 判断及物性 和  命令式
                    comm = "མིན་འདུག་།"
                    yn = "ཐ་མི་དད་པ་།"
                else:
                    comm = result[0][i][3]
                    yn = "ཐ་དད་པ་།"
                set_text = set_text + "[{}]:".format(i+1) + " ད་ལྟ་བ་། " + result[0][i][0] + "\tའདས་པ་། " + result[0][i][1] + "\tམ་འོངས་པ་། " + \
                            result[0][i][2] + "\tསྐུལ་ཚིག་། " + comm + "\tབྱ་བྱེད་" + yn + "\n"
            self.textBrowser_rec.setText(set_text)

# 启动入口
if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())
