import _thread
import time

def tinh_tong(gt):
    tong=0
    chuoi=''
    for i in range(1,gt+1):
        tong+=i
        chuoi+=str(i) + ' '
        if i%2 == 0:
            print('i = ', chuoi)
            thong_bao()
            time.sleep(1)

def thong_bao():
    print('Dang tinh tong, vui long cho')

_thread.start_new_thread(tinh_tong,(50,))

while 1:
    pass