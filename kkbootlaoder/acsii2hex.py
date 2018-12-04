def data_acsii_2_hex(data):
    ascii=chr(data)

    if ascii == "0":
        return 0
    elif ascii == "1":
        return 1
    elif ascii == '2':
        return 2        
    elif ascii == "3":
        return 3
    elif ascii == "4":
        return 4
    elif ascii == "5":
        return 5
    elif ascii == "6":
        return 6
    elif ascii == "7":
        return 7
    elif ascii == "8":
        return 8
    elif ascii == "9":
        return 9
    elif ascii == "a" or ascii == 'A':
        return 10
    elif ascii == "b" or ascii == 'B':
        return 11
    elif ascii == "c" or ascii == 'C':
        return 12
    elif ascii == "d" or ascii == 'D':
        return 13
    elif ascii == "e" or ascii == 'E':
        return 14
    elif ascii == "f" or ascii == 'F':
        return 15
    else:
        return 255
if __name__ =="__main__":
    data=[]
    data=data_acsii_2_hex(55)
    if chr(50)=='1':
        print("ok")
    print(data)
