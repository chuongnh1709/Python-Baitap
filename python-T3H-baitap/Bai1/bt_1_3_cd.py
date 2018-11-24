from thu_vien.CD import *       # import tất cả các hàm trong Module CD
list_cd = []
tt=1        # Tiep tuc 
while tt==1:   # Tiep tuc khi tt=1
    tenCD = input('Ten CD : ')
    tenCaSi = input('Ten Ca Si: ')
    sobaihat = int(input('So bai hat : '))
    giathanh = int(input('Gia Thanh : '))
    cd = CD(tenCD, tenCaSi, sobaihat, giathanh)
    list_cd.append(cd)
    tt = int(input('Nhap tiep ? (1 :co / 0 :dung) : '))

tong_tien = 0
if len(list_cd):
    for i in list_cd:
        print(i.thong_tin_cd())
    
    print('Tong tien: ', i.tong_tien)   # trong object CD đã có sẵn thuộc tính tong_tien
