import json
from thu_vien.GiaoDich import *

print("Quản lý giao dịch:")
list_vang = []
list_tien = []
tieptuc = 1

while tieptuc == 1:
    ma = input("Nhap Ma GD: ")
    ngay = input("Nhap ngay: ")
    so_luong = int(input("Nhap So luong GD: "))

    i = int(input('Chon loai Giao dich : 1:Vang / 2:Tiền tệ: '))

    if i == 1:
        tong_slv = 0
        tong_tien_vang  = 0
        loai = input("Chon loại Vàng : 18k/ 24k/ 9999: ")
        don_gia = eval(input('Nhap don gia: '))
        gdv = GiaoDich(ma, ngay, don_gia, so_luong, loai)
        list_vang.append

        for i in list_vang:
            tong_slv += i.so_luong
            tong_tien_vang += i.thanh_tien()
            print(i.in_giao_dich())

        print('Tổng số lượng: ', tong_slv)
        print('Tổng số tiền: ', tong_tien_vang)

    if i==2:
        tong_slt = 0
        tong_tien_tien = 0
        loai = input('Chon loai: USD/EUR/AUD: ')
        don_gia = eval(input('Nhập tỷ giá: '))
        mua = True
        gd = int(input('Bạn mua hay bán: 1:mua / 2:bán : \t'))
        if gd!=1:
            mua = False

        gdtt = GiaoDichTienTe(ma, ngay, don_gia, so_luong, loai, mua)
        list_tien.append(gdtt)

        ## In giao dịch ra màn hình
        print('')
        for i in list_tien:
            tong_slt += i.so_luong
            tong_tien_tien += i.thanh_tien()
            print(i.in_giao_dich())
        print('Tổng số lượng: ', tong_slt)
        print('Tổng số tiền: ', tong_tien_tien)

    tieptuc = int(input('Bạn muốn tiếp tục giao dịch không ? 1:có/ 2:không: \t'))

# Write to Json (lúc này đã thoát khỏi vòng while)

# if tieptuc != 1:
