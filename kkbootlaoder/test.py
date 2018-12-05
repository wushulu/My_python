import crc16pure
data_tab='x'
if __name__ =="__main__":
    data=[]
    try:
        print('try')
        data.append(int(data_tab))
    except ValueError:
        print('ValueError') 
    else:
        print('other erro')

            


    #check=crc16pure.crc16xmodem(data)
    print(data)
