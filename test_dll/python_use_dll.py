from ctypes import *

if __name__ == "__main__":
    TestDll=CDLL('TestDll.dll')
    TestDll.hello()
    print(TestDll.SumNumbers(5,6))
    