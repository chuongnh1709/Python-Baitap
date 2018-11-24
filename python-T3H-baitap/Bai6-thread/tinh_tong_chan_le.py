import _thread
import time

def tong_chan(gt):
    tong = 0 
    chuoi=''
    for i in range(1,gt+1):
        if i%2==0:
            tong+=i
            chuoi += str(i) + ' '
            print(chuoi)
            time.sleep(0.5)
    print('Tong cac so chan tu 1 den ',gt, ' = ', tong)

def tong_le(gt):
    tong = 0 
    chuoi=''
    for i in range(1,gt+1):
        if i%2 != 0:
            tong+=i
            chuoi += str(i) + ' '
            print(chuoi)
            time.sleep(0.5)
    print('Tong cac so le tu 1 den ',gt, ' = ', tong)

## Main 
if __name__=='__main__':
    _thread.start_new_thread(tong_chan,(20,))
    _thread.start_new_thread(tong_le,(20,))
    
    while 1:
        pass