# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zige.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!
import sys
from time import sleep
import serial
import binascii
from  serial.tools import list_ports
import threading
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(722, 436)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(210, 210, 91, 31))
        self.toolButton.setObjectName("toolButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(210, 60, 81, 31))
        self.textEdit.setObjectName("textEdit")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(310, 60, 171, 31))
        self.horizontalSlider.setMaximum(700)
        self.horizontalSlider.setSliderPosition(0)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 30, 71, 31))
        self.label.setObjectName("label")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(510, 80, 91, 31))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_3.setGeometry(QtCore.QRect(510, 20, 91, 31))
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_4.setGeometry(QtCore.QRect(510, 150, 91, 31))
        self.toolButton_4.setObjectName("toolButton_4")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(310, 160, 171, 31))
        self.horizontalSlider_2.setMaximum(359)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(210, 160, 81, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 90, 71, 31))
        self.label_2.setObjectName("label_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(210, 120, 81, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 160, 31, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 120, 31, 31))
        self.label_4.setObjectName("label_4")
        self.horizontalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(310, 120, 171, 31))
        self.horizontalSlider_3.setMaximum(1000)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(150, 250, 551, 161))
        self.textBrowser.setObjectName("textBrowser")
        self.toolButton_5 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_5.setGeometry(QtCore.QRect(610, 150, 91, 31))
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_6 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_6.setGeometry(QtCore.QRect(610, 80, 91, 31))
        self.toolButton_6.setObjectName("toolButton_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150, 230, 41, 21))
        self.label_5.setObjectName("label_5")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 260, 111, 151))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 240, 41, 21))
        self.label_6.setObjectName("label_6")
        self.toolButton_7 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_7.setGeometry(QtCore.QRect(310, 210, 91, 31))
        self.toolButton_7.setObjectName("toolButton_7")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(70, 30, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 30, 31, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 70, 41, 21))
        self.label_8.setObjectName("label_8")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(70, 70, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.toolButton_8 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_8.setGeometry(QtCore.QRect(20, 110, 121, 31))
        self.toolButton_8.setObjectName("toolButton_8")
        self.toolButton_9 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_9.setGeometry(QtCore.QRect(20, 150, 121, 31))
        self.toolButton_9.setObjectName("toolButton_9")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(320, 10, 69, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(260, 10, 41, 21))
        self.label_9.setObjectName("label_9")
        self.toolButton_10 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_10.setGeometry(QtCore.QRect(410, 210, 91, 31))
        self.toolButton_10.setObjectName("toolButton_10")
        self.toolButton_11 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_11.setGeometry(QtCore.QRect(610, 20, 91, 31))
        self.toolButton_11.setObjectName("toolButton_11")
        self.toolButton_12 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_12.setGeometry(QtCore.QRect(30, 240, 61, 21))
        self.toolButton_12.setObjectName("toolButton_12")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.horizontalSlider.valueChanged.connect(self.set_speed_value)
        self.horizontalSlider_3.valueChanged.connect(self.set_pos_r_value)
        self.horizontalSlider_2.valueChanged.connect(self.set_pos_d_value)
        self.toolButton_3.clicked.connect(self.Ping)
        self.toolButton_11.clicked.connect(self.clear_state)
        self.toolButton_2.clicked.connect(self.send_speed)
        self.toolButton_4.clicked.connect(self.send_position)
        self.toolButton_6.clicked.connect(self.get_speed)
        self.toolButton_5.clicked.connect(self.get_position)
        self.toolButton.clicked.connect(self.start_motor)
        self.toolButton_7.clicked.connect(self.stop_motor)
        self.toolButton_10.clicked.connect(self.lock_motor)
        self.toolButton_12.clicked.connect(self.textBrowser_2.clear)
        self.toolButton_8.clicked.connect(self.check_com)
        self.toolButton_9.clicked.connect(self.open_com)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "嘉友锦磁——子歌电机调试助手"))
        self.toolButton.setText(_translate("MainWindow", "启动"))
        self.label.setText(_translate("MainWindow", "速度设置"))
        self.toolButton_2.setText(_translate("MainWindow", "发送速度"))
        self.toolButton_3.setText(_translate("MainWindow", "Ping"))
        self.toolButton_4.setText(_translate("MainWindow", "发送位置"))
        self.label_2.setText(_translate("MainWindow", "位置设置"))
        self.label_3.setText(_translate("MainWindow", "度数"))
        self.label_4.setText(_translate("MainWindow", "圈数"))
        self.toolButton_5.setText(_translate("MainWindow", "位置查询"))
        self.toolButton_6.setText(_translate("MainWindow", "速度查询"))
        self.label_5.setText(_translate("MainWindow", "数据"))
        self.label_6.setText(_translate("MainWindow", "状态"))
        self.toolButton_7.setText(_translate("MainWindow", "停止"))
        self.comboBox.setItemText(0, _translate("MainWindow", "COM1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "COM2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "COM3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "COM4"))
        self.comboBox.setItemText(4, _translate("MainWindow", "COM5"))
        self.label_7.setText(_translate("MainWindow", "串口"))
        self.label_8.setText(_translate("MainWindow", "波特率"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "115200"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "9600"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "38400"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "256000"))
        self.toolButton_8.setText(_translate("MainWindow", "搜索串口"))
        self.toolButton_9.setText(_translate("MainWindow", "打开串口"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "6"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "7"))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "8"))
        self.comboBox_3.setItemText(8, _translate("MainWindow", "9"))
        self.comboBox_3.setItemText(9, _translate("MainWindow", "10"))
        self.comboBox_3.setItemText(10, _translate("MainWindow", "255"))
        self.label_9.setText(_translate("MainWindow", "电机ID :"))
        self.toolButton_10.setText(_translate("MainWindow", "电机锁"))
        self.toolButton_11.setText(_translate("MainWindow", "清除状态"))
        self.toolButton_12.setText(_translate("MainWindow", "清除"))
        #self.por = serial.Serial()
        self.check_com()
    def __init__(self):
         self.Com_List    =0
         self.pack_head   = [0xaa, 0x55]
         self.id          = 0
         self.len         = 0
         self.data_comand = []
         self.data_in     = []
         self.check_sum   = 0

    def check_com(self):
        self.Com_List=[]
        self.por = serial.Serial()
        port_list = list(serial.tools.list_ports.comports())
        self.comboBox.clear()
        for port in port_list:
            self.Com_List.append(port[0])
            self.comboBox.addItem(port[0])
        if(len(self.Com_List) == 0):
            self.comboBox.addItem('没有串口')

    def open_com(self):
        self.task = threading.Thread(target=self.receive_data)
        if len(self.Com_List)==0:
            self.textBrowser.append('无可用串口' )
            self.textBrowser.moveCursor(QtGui.QTextCursor.End)
        else:
            self.por = serial.Serial()
            self.por.close()
            sleep(0.2)
            self.port = self.comboBox.currentText()
            self.baudrate =int(self.comboBox_2.currentText())
            self.por=serial.Serial( self.port,self.baudrate)
            self.por.close()
            self.por.open()
            if self.por.isOpen():
                self.textBrowser.append('串口已打开')
                self.textBrowser.moveCursor(QtGui.QTextCursor.End)
                self.task.setDaemon(True)
                self.task.start()

    def receive_data(self):
        print("data sss")
        data_send = []
        data_str=''
        s=''
        receive_data = ''
        self.textBrowser.append('The receive_data task is start')
        while self.por.isOpen():
            size = self.por.inWaiting()
            if size:
                receive_data = self.por.read_all()
                for get_data in receive_data:
                    s = str(hex(get_data)[2:])
                    if len(s) == 1:
                        s = '0' + s
                    s = ' ' + s
                    data_send.append(s)
                data_str = ''.join(data_send)
                self.textBrowser.append(' 接收数据为:'+data_str)
                self.textBrowser.moveCursor(QtGui.QTextCursor.End)
                self.check_motor_state(receive_data)
                self.textBrowser.moveCursor(QtGui.QTextCursor.End)
                data_send=[]
                s = ''
                data_str = ''
    def check_motor_state(self,get_data):
        get_data_tab=[]
        get_data_tab=get_data
        lengt = len(get_data)
        if  lengt<=5:
            self.textBrowser_2.append('数据格式错误')
            self.textBrowser_2.moveCursor(QtGui.QTextCursor.End)
        else:
            sate=int(get_data_tab[lengt-2])
            if   sate==1:
                self.textBrowser_2.append('校验和错误')
            elif sate==2:
                self.textBrowser_2.append('过流')
            elif sate==4:
                self.textBrowser_2.append('堵转')
            elif sate==8:
                self.textBrowser_2.append('欠压')
            elif sate==16:
                self.textBrowser_2.append('指令不存在')
            self.textBrowser_2.moveCursor(QtGui.QTextCursor.End)
        if lengt==8:
            speed=int(get_data_tab[4])+ (int(get_data_tab[5]&0x7f)<<8)
            if get_data_tab[5]&0x80:
                self.textBrowser.append(' 速度为：-' + str(speed))
            else:
                self.textBrowser.append(' 速度为：'+str(speed))

    def send_data(self,data):
        data_send = []
        data_str=''
        s=''
        for temp in data:
            s=str(hex(temp)[2:])
            if len(s)==1:
                s='0'+s
            s=' '+s
            data_send.append(s)
        data_str =''.join(data_send)

        if self.por.isOpen():
             self.textBrowser.append('发送数据为:'+data_str)
             self.textBrowser.moveCursor(QtGui.QTextCursor.End)
             self.por.write(data)
        else:
            self.textBrowser.append('请打开串口' )
            self.textBrowser.moveCursor(QtGui.QTextCursor.End)

    def Ping(self):
        self.data_comand=[0x01]
        self.data_in =[]
        self.PCK_data(self.data_comand,self.data_in)

    def clear_state(self):
        self.data_comand=[0x10]
        self.data_in =[]
        self.PCK_data(self.data_comand,self.data_in)

    def send_speed(self):
        self.data_comand=[0x04]
        self.dat_in = []
        if(self.textEdit.toPlainText()==''):
            speed=0
        else:
            speed=int(self.textEdit.toPlainText())
        self.data_in.append(speed&0x00ff)
        self.data_in.append((speed>>8)&0x00ff)
        self.PCK_data(self.data_comand,self.data_in)

    def send_position(self):
        self.data_comand = [0x05]
        self.data_in=[]
        if self.textEdit_3.toPlainText()=='':
            pos_r=0
        else:
            pos_r=int(self.textEdit_3.toPlainText())
        if self.textEdit_2.toPlainText() == '':
            pos_d=0
        else:
            pos_d=int(self.textEdit_2.toPlainText())
        self.data_in.append(pos_d&0x00ff)
        self.data_in.append((pos_d>>8) & 0x00ff)
        self.data_in.append(pos_r&0x00ff)
        self.data_in.append((pos_r>>8) & 0x00ff)
        self.PCK_data(self.data_comand, self.data_in)

    def get_speed(self):
        self.data_comand = [0x03]
        self.data_in = []
        self.PCK_data(self.data_comand, self.data_in)

    def get_position(self):
        self.data_comand = [0x02]
        self.data_in = []
        self.PCK_data(self.data_comand, self.data_in)

    def start_motor(self):
        self.data_comand = [0x06]
        self.data_in = []
        self.PCK_data(self.data_comand, self.data_in)

    def stop_motor(self):
        self.data_comand = [0x07]
        self.data_in = []
        self.PCK_data(self.data_comand, self.data_in)

    def lock_motor(self):
        self.data_comand = [0x08]
        self.data_in = []
        self.PCK_data(self.data_comand, self.data_in)

    def set_speed_value(self):
        num=self.horizontalSlider.value()
        self.textEdit.setText(str(num))

    def set_pos_r_value(self):
        num=self.horizontalSlider_3.value()
        self.textEdit_3.setText(str(num))

    def set_pos_d_value(self):
        num = self.horizontalSlider_2.value()
        self.textEdit_2.setText(str(num))

    def PCK_data(self,data_cmd,data_in):
        self.len     =len(self.data_in)
        self.id      =int(self.comboBox_3.currentText())
        self.data_comand.insert(0,self.id)
        self.data_comand.insert(1,self.len)
        self.data_in= self.data_comand+self.data_in
        self.check_sum=check_sum( self.data_in)
        self.data_in.append(self.check_sum)
        self.data_in = self.pack_head + self.data_in
        self.send_data(self.data_in)
        self.data_in=[]
def check_sum(data):
    sum_a=0
    for i in data:
        sum_a=i+sum_a
        if(sum_a>=256):
            sum_a=sum_a-256
    return int(sum_a)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

