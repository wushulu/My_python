import serial
from  serial.tools import list_ports
import sys
from time import sleep
import linecache
import crc16pure
import acsii2hex
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QMainWindow
from demo import Ui_MainWindow

class My_windows(QMainWindow, Ui_MainWindow):
    _window_list = []

    def __init__(self):
        super(My_windows, self).__init__()

        My_windows._window_list.append(self)
        self.setupUi(self)
        self.SOH = 0x01
        self.EOT = 0x04 
        self.DLE = 0x10
        self.CMD = []
        self.READ_BOOT_INFO = 0x01
        self.ERASE_FLASH = 0x02
        self.PROGRAM_FLASH =0x03
        self.READ_CRC =0x04
        self.JMP_TO_APP = 0x05
        self.crc_check = 0
        self.hexfile = ''
        self.hexline = 0
        self.opnefile_falg = False
        self.receive_right_flag=False
        self.sleep_time=0.05
        self.pushButton.clicked.connect(self.OpenCOM)
        self.pushButton_2.clicked.connect(self.Read_boot_Info)
        self.pushButton_3.clicked.connect(self.Erase_Flash)
        self.pushButton_4.clicked.connect(self.Program_Flash)
        self.pushButton_5.clicked.connect(self.Jmp_To_App)
        self.pushButton_7.clicked.connect(self.check_com)
        self.actionOpenhex.triggered.connect(self.actionOpenfile)
        self.actionSave.triggered.connect(self.actionSaved_data)
        self.check_com()

    def OpenCOMtest(self):
        print("nihao")
    def check_com(self):
        self.Com_List=[]
        self.por = serial.Serial()
        port_list = list(serial.tools.list_ports.comports())
        self.comboBox.clear()
        for port in port_list:
            self.Com_List.append(port[0])
            self.comboBox.addItem(port[0])
        if(len(self.Com_List) == 0):
            self.comboBox.addItem('No uart COM')

    def OpenCOM(self):
        #self.task = threading.Thread(target=self.receive_data)
        if len(self.Com_List)==0:
            self.textBrowser.append('No serial uart COM' )
            self.textBrowser.moveCursor(QtGui.QTextCursor.End)
        else:
            self.por = serial.Serial()
            self.por.close()
            sleep(0.2)
            self.port = self.comboBox.currentText()
            self.baudrate =int(self.comboBox_2.currentText())
            try:
                self.por=serial.Serial( self.port,self.baudrate)
                self.textBrowser.append('COM is open  baud rate:'+self.comboBox_2.currentText())
                self.textBrowser.moveCursor(QtGui.QTextCursor.End)
                self.task = threading.Thread(target=self.received_data) #add received thread
                self.por.close()
                self.por.open()
                self.task.setDaemon(True)
                self.task.start()
            except IOError:
                print('Error: COM is busing')
                self.textBrowser.append('Error: this COM is busing can not open it')
                self.textBrowser.moveCursor(QtGui.QTextCursor.End)
            else:
                print("COM error")


    def Serial_Send_data(self,data):
        i=0
        if self.por.isOpen():
            while i<=4:
                self.por.write(data)
                self.textBrowser.append('send data:'+str(data))
                self.textBrowser.moveCursor(QtGui.QTextCursor.End)
                sleep(self.sleep_time)
                if self.receive_right_flag==True:
                    self.receive_right_flag=False
                    break
                elif i==4:
                    self.textBrowser.append('received data time out')
                    self.textBrowser.moveCursor(QtGui.QTextCursor.End)                    
                i+=1

        else:
            self.textBrowser.append('please open uart com')
            self.textBrowser.moveCursor(QtGui.QTextCursor.End)           

    def received_data(self):
        test_recevied=[]
        data_send = []
        data_change=[]
        data_str=''
        s=''
        receive_data = ''
        self.textBrowser.append('The receive_data task is start')
        while self.por.isOpen():
            size = self.por.inWaiting()
            if size:
                receive_data = self.por.read_all()
                data_change=self.check_received_data(receive_data)## received data change delte DLE
                print('dat_change',data_change)
                '''
                for get_data in receive_data:
                    test_recevied.append(hex(get_data))
                    s = str(hex(get_data)[2:])
                    if len(s) == 1:
                        s = '0' + s
                    s = ' ' + s
                    data_send.append(s)
                data_str = ''.join(data_send)
                self.textBrowser.append('received data:'+data_str)
                self.textBrowser.moveCursor(QtGui.QTextCursor.End)
                    '''
                for get_data in data_change:
                    test_recevied.append(get_data)
                    
                self.textBrowser.append('received data:'+str(test_recevied))
                self.textBrowser.moveCursor(QtGui.QTextCursor.End)
                test_recevied=[]                
                if data_change:
                    self.CMD_explain(data_change)
                data_send=[]
                s = ''
                data_str = ''

    def check_received_data(self,data):
        data_re=[]
        date_ret=[]
        datcont=[]
        data_len=len(data)
        if data_len>=5:
            for i in data:
                try:
                    data_re.append(int(i))
                except ValueError:
                    print("Error: received data is error ")
                    break
                else:
                    print("Error: other error")
                    break

            for j in range(data_len):
                if data_re[j]==self.DLE:
                    data_next=data_re[j+1]
                    if data_next==self.DLE or data_next==self.SOH or data_next==self.EOT:
                        datcont.append(j)
                    else:
                        date_ret.append(data_re[j])

                else:
                    date_ret.append(data_re[j])
        else:
            date_ret=[]

        return date_ret

    def CMD_explain(self,data):
        receive_cmd = data[1]
        if receive_cmd==self.READ_BOOT_INFO:
            self.receive_right_flag=True
            self.textBrowser.append('Software version:'+str(data[2])+'.'+str(data[3]))
            self.textBrowser.moveCursor(QtGui.QTextCursor.End)
        elif receive_cmd==self.ERASE_FLASH:
            self.receive_right_flag=True
            self.textBrowser.append('Flash is erased')
            self.textBrowser.moveCursor(QtGui.QTextCursor.End)
        elif receive_cmd==self.PROGRAM_FLASH:
            if data[2]==1:
                self.receive_right_flag=True

            #return
            #self.textBrowser.append('Progarming ...')
            #self.textBrowser.moveCursor(QtGui.QTextCursor.End)
        elif receive_cmd==self.JMP_TO_APP:
            self.receive_right_flag=True
            self.textBrowser.append('RUN APP')
            self.textBrowser.moveCursor(QtGui.QTextCursor.End)
        

        






    def actionOpenfile(self):
        fileName,filetype = QFileDialog.getOpenFileName(None,
                    "choose file",
                    "./",
                    "Hex Files (*.hex);;All Files (*)")
        if not(fileName==''):
            self.hexfile=[]
            self.hexline=[]
            self.hexfile = open(fileName,"rb")
            self.hexline = self.hexfile.readlines()
            self.textBrowser.append(fileName+"    file is load")
            self.opnefile_falg = True
            #print(self.hexline)
            
            #print(linecache.getline(fileName,11))
            #print('file is OK')
        else:#if not open file
            #print('return')
            return 
    def actionSaved_data(self):
        with open("save.txt","w") as f:
            text = self.textBrowser.toPlainText()
            f.write(text)
            #print("save")
        

    def Read_boot_Info(self):
        data=[]
        self.CMD = [self.READ_BOOT_INFO]
        data=self.CMD
        data=self.Check_data(data)
        self.sleep_time=0.05
        self.Serial_Send_data(data)
        #print(data)

        #print(crc_check)
        #self.Check_data(data)
    def Erase_Flash(self):
        data=[]
        self.CMD = [self.ERASE_FLASH]
        data=self.CMD
        data=self.Check_data(data)
        self.sleep_time=0.8
        self.Serial_Send_data(data)
        

    def Program_Flash(self):
        '''
        data=[]
        self.CMD = [self.PROGRAM_FLASH]
        data=self.CMD
        data.append(0x01)
        data=self.Check_data(data)
        self.Serial_Send_data(data)
        '''
        self.sleep_time=0.05
        if  self.opnefile_falg==True:
            data=[]
            data_cmd=[]
            self.CMD = [self.PROGRAM_FLASH]
            data_cmd=self.CMD
            for line in self.hexline:
                #print(line[1:-2])
                if chr(line[0]) == ':':
                    data= data_cmd+self.changehex(line)
                    #print('cmd',data)
                    data=self.Check_data(data)
                    self.Serial_Send_data(data)
                    #print(data)
                    data=[]
                else:
                    self.textBrowser.append('Error :this file is not standard hex file')
                    break
        else:
            self.textBrowser.append("please open standard hex file")
    def Jmp_To_App(self):
        data=[]
        self.CMD = [self.JMP_TO_APP]
        data=self.CMD
        data=self.Check_data(data)
        self.sleep_time=0.03
        self.Serial_Send_data(data)

    def Check_data(self,data):
        data_send =[]
        s_data_send=[]
        s_data_send=data
        crc_check=crc16pure.crc16xmodem(s_data_send)
        #print("crc",crc_check)
        s_data_send.append(crc_check&0x00ff)
        s_data_send.append(crc_check>>8)
        print('cmd+data',s_data_send)
        for s_data in s_data_send:
            if s_data==self.SOH or s_data==self.DLE or s_data==self.EOT:
                data_send.append(self.DLE)
            data_send.append(s_data)
        data_send.append(self.EOT)
        data_send.insert(0,self.SOH)
        return data_send
        #print(data_send)
    def changehex(self,data):##check and pack
        change_data=[]
        combine_data=[]
        data=data[1:-2]
        #print(data)
        for s_data in data:
            s_data=acsii2hex.data_acsii_2_hex(s_data)
            change_data.append(s_data)
        #print('list',change_data)
        for i in range(len(change_data)-1):
            if i%2==0:
                combine_data.append((change_data[i]<<4)+change_data[i+1])
        #print('combine',combine_data)
        return combine_data



        



        




if __name__=="__main__":

    app = QtWidgets.QApplication(sys.argv)
    ui = My_windows()
    ui .show()
    sys.exit(app.exec_())
