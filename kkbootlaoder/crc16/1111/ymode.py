import crc16pure
from time import sleep
import serial
import binascii
#checK_sun
def check_sum(data):
    sum_a=0
    for i in data:
        sum_a=i+sum_a
        if(sum_a>=256):
            sum_a=sum_a-256
    return int(sum_a)
#open filed   
def file_hdl(filed_name):
    arr =[]
    name=filed_name
    f = open(name,'rb')
    d = f.read()
    lentgh = len(d)
    for data in d:
        arr.append(data)
    f.close()
    return arr

class Yomde_sprotocol:
    def __init__(self):
        self.head=[0xd5,0x5d]
        self.id=''
        self.len=0
        self.data_comand=[]
        self.check_sum=0
        self.data_in=[]
        self.crc_check=0
        self.f=[]
        self.filed_name=''
        self.filed_len=0
        self.Kbits=0
        self.fac=0
        self.end_tab=[]
        self.list=0
        self.open_filed()
        self.back_data=''
    def open_filed(self):
        print("请输入ID")
        self.id=input('\n ID:')
        print("请输入文件名：")
        self.filed_name=input('文件名：')
        self.f=file_hdl(self.filed_name)
        self.filed_len=len(self.f)
        self.Kbits=int(self.filed_len/1024)+1
        self.fac  =1024-self.filed_len%1024
        for i in range(self.fac):
            self.end_tab.append(0xff)
        self.list=0
    def send_start_command(self):
        self.data_comand=[0xff,0xfc]
        self.len=3
        self.data_comand.insert(0,int(self.id))
        self.data_comand.insert(1,self.len)
        self.check_sum=check_sum(self.data_comand)
        self.data_comand.append(self.check_sum)
        self.data_comand=self.head+self.data_comand
        while  self.back_data=='':
            send_data(self.data_comand)
            self.back_data=get_data()
            data=bytes.fromhex(self.back_data)
            data=str(bytes(data[5:6]))[2:-1]
            if  data =='C':
                self.back_data='a'
            else:
                self.back_data=''
        self.back_data=''
    def test(self):
        data_tab=[]
        data_tab=self.f[0:1024]
        chenk_s=check_sum(data_tab)
        print(chenk_s)
        #print(data_tab)

    def send_SOH(self,first_flag):
        data_send=[]
        self.data_comand=[0xff,0xfe]
        self.len=128+8
        self.data_comand.insert(0,int(self.id))
        self.data_comand.insert(1,self.len)
        for data in range(128):
            data_send.append(0x00)
        if first_flag==1:
            data_send[0]=(self.filed_len>>24)&0x00ff
            data_send[0]=(self.filed_len>>16)&0x00ff
            data_send[2]=(self.filed_len>>8)&0x00ff
            data_send[3]=self.filed_len&0x00ff
        self.crc_check=crc16pure.crc16xmodem(data_send)
        data_send.append(self.crc_check>>8)
        data_send.append(self.crc_check&0x00ff)

        data_send.insert(0,0x01)#SOH
        data_send.insert(1,0x00)
        data_send.insert(2,0xff)

        data_send=self.data_comand+data_send
        self.check_sum=check_sum(data_send)
        data_send.append(self.check_sum)
        data_send=self.head+data_send
        send_data(data_send)
        while self.back_data=='':
            self.back_data=get_data()
            data=bytes.fromhex(self.back_data)
            data_ack=str(bytes(data[5:6]))[4:-1]
            #print('ack',data_ack)
            if data_ack=='06':#C
                if first_flag==0:
                    self.back_data = 'a'
                    #print('get ACK')
                else:
                    data_c=str(bytes(data[6:7]))[2:-1]
                    #print('data_c=:',data_c)
                    if data_c=='C':
                        self.back_data='a'
                    else:
                        #print("wrong")
                        self.back_data=''            
            elif data_ack=='18':
                break
            elif data_ack=='15':
                send_data(data_send)
                self.back_data=''
            else:
                self.back_data=''
        self.back_data=''
    def send_STX(self):
        data_tab=[]
        list_f=0
        self.data_comand=[0xff,0xfe]
        self.data_comand.insert(0,int(self.id))
        self.data_comand.insert(1,0xff)
        #print(self.data_comand)
        for list_f in range(self.Kbits):
            list_first= list_f*1024
            list_end  = list_first+1024
            if list_f==self.Kbits-1:
                data_tab=self.f[list_first:]
                data_tab=data_tab+self.end_tab
            else:
                data_tab=self.f[list_first:list_end]
            self.crc_check=crc16pure.crc16xmodem(data_tab)
            data_tab.append(self.crc_check>>8)
            data_tab.append(self.crc_check&0x00ff)
            data_tab.insert(0,0x02)#SOH
            data_tab.insert(1,list_f+1)
            data_tab.insert(2,0xff^(list_f+1))
            data_tab=self.data_comand+data_tab
            self.check_sum=check_sum(data_tab)
            data_tab.append(self.check_sum)
            data_tab=self.head+data_tab
            print('发送第',list_f ,'帧数据')
            send_data_len=len(data_tab)
            print('发送数据长度：',send_data_len)
            #data_tab=data_pack(data_tab,self.data_comand,list_f+1)
            send_data(data_tab)
            self.back_data=''
            while self.back_data=='':
                self.back_data=get_data()
                data=bytes.fromhex(self.back_data)
                data_ack=str(bytes(data[5:6]))[4:-1]
                sleep(1)
                if data_ack=='06':
                    self.back_data='a'
                elif data_ack=='18':
                    break
                elif data_ack=='15':
                    print('第',list_f,'帧数据错误 重新发送')
                    send_data(data_tab)
                    self.back_data=''
                else:
                    self.back_data=''
        print('数据发送完成')
        self.back_data=''
    def send_EOT(self):
        data_tab=[]
        self.data_comand=[0xff,0xfe]
        self.data_comand.insert(0,int(self.id))
        self.data_comand.insert(1,4)
        self.data_comand.append(4)
        check_s=check_sum(self.data_comand)
        data_tab=self.data_comand
        data_tab.append(check_s)
        data_tab=self.head+data_tab
        send_data(data_tab)
        while self.back_data=='':
            self.back_data=get_data()
            data=bytes.fromhex(self.back_data)
            data_ack=str(bytes(data[5:6]))[4:-1]
            data_c  =str(bytes(data[6:7]))[2:-1]
            if (data_ack=='06')and(data_c=='C'):
                self.back_data='a'
            else:
                self.back_data=''
        self.back_data=''
    def send_pack(self,x,y):
        data = []
        self.x=x
        self.y=y
        #data[1]=self.y
        #self.dispoint()
       # data=add_head(x,y)
        print("OK")
        #print(data)
        #ser.write(data)
        sleep(0.5)
def data_pack(data_in,command,lsit):
    data_comand=command
    data_s=data_in
    check_crc=crc16pure.crc16xmodem(data_in)
    data_s.append(check_crc>>8)
    data_s.append(check_crc&0x00ff)
    if lsit==0:
        data_s.insert(0,0x01)
        data_s.insert(1,0x00)
        data_s.insert(2,0xff)
    else:
        data_s.insert(0,0x02)
        data_s.insert(1,lsit)
        data_s.insert(2,(lsit)^(0xff))
    data_s=data_comand+data_s
    check_sm=check_sum(data_s)
    data_s.append(check_sm)
    data_s=qh_sprotocol.head+data_s
    return data_s
def send_data(a):
    data_send=[]
    for temp in a:
        data_send.append(hex(temp))
    print('正在发送')
    print('发送数据', data_send)
    ser.write(a)
    sleep(1) 
def get_data():
    data=''
    while ser.inWaiting()>0:
        #data.append(hex(ser.read(1)))
        data=data+str(binascii.b2a_hex(ser.read(1)))[2:-1]+' '
        #data.append(ser.read(1))
    print('接收数据:',data)
    sleep(0.5)
    return data
        
        #data+=binascii.b2a_hex(ser.read(1))
if __name__ == '__main__':
    from  serial.tools import list_ports
    print('\n当前可用串口：')
    for port_list in list(list_ports.comports()):
        print(port_list)
    com_id = input('\n打开串口：')
    com_id = 'COM' + com_id
    #baud = input('设置波特率：')
    ser = serial.Serial(com_id, 115200)
    ser.close() 
    ser.open()
    qh_sprotocol = Yomde_sprotocol()
    qh_sprotocol.send_start_command()
    qh_sprotocol.send_SOH(1)
    qh_sprotocol.send_STX()
    qh_sprotocol.send_EOT()
    qh_sprotocol.send_SOH(0)
    print('升级成功')

    #qh_sprotocol.test()
    
    #data=''    
   # while 1:
    #    data=get_data()
        
    #    if data!='':
    #        print(data)
    #        data=bytes.fromhex(data)
    #        data_send=str(bytes(data[5:6]))[2:-1]
    #        print(data_send)
    #        if data_send=='00':
    #            data='a'
    #            print('OKKK')
    #        else:
    #            data=''
            #ser.write(data_send)
            #data=''
    

    
