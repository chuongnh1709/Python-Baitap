from thu_vien.CD import *
list_cd = []
ten_cd = "1"    # Chon ten CD lam dieu kien tiếp tục
while ten_cd != "":
    ten_cd = input('Ten CD (Enter = thoat): ')
    if len(ten_cd)>0:     # = len(ten_cd) > 0
        tenCaSi = input('Ten Ca Si: ')
        sobaihat = int(input('So bai hat : '))
        giathanh = int(input('Gia Thanh : '))
        cd = CD(ten_cd, tenCaSi, sobaihat, giathanh)
        list_cd.append(cd)

tong_tien = 0
if len(list_cd):
    for i in list_cd:
        tong_tien += i.gia_thanh
        print(i.thong_tin_cd())
    print('Tong tien : ' , tong_tien)