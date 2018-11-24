import json
import sqlite3

# insert json vao sqlite thongtincty, Nhom_tv, NhanVien 

def load_json_sqlite():
    continue_ = 1
    while continue_ == 1:
        print(' Load data Json vao product.db - sqlite3 \n Chon data muon load')
        print(' Load Thong tin cty - chon 1 \n Load Nhom TV - chon 2 \n Load Thong tin Nhan Vien - chon 3')
        selection_ = int(input('Chon : '))

        if selection_ == 1:
            ## Load thong tin cong ty 
            f = open('Dulieu/Cong_ty.json', encoding='utf-8')
            noi_dung = json.load(f)
            f.close()
            ThongtinCT=[]
            # for i in noi_dung['Danh_sach_Nhom_Tivi']:
            #     DS_Nhom.append(i['Ma_so'])
            ThongtinCT.append(noi_dung['Ten'])
            ThongtinCT.append(noi_dung['Ma_so'])
            ThongtinCT.append(noi_dung['Dien_thoai'])
            ThongtinCT.append(noi_dung['Dia_chi'])
            ThongtinCT.append(noi_dung['Mail'])
            print(ThongtinCT)
            conn = sqlite3.connect('D:\PYTHON\Python-T3H\ThucHanh\Bai9-wxFormbuilder\Dulieu\product.db')
            sql='insert into tblThongTinCongTy(Ten, Ma_so, Dien_thoai, Dia_chi, Mail) values(?,?,?,?,?)'
            conn.execute(sql,(ThongtinCT[0],ThongtinCT[1],ThongtinCT[2],ThongtinCT[3],ThongtinCT[4]))
            conn.commit()
            conn.close()

        if selection_ == 2:
            f = open('Dulieu/Cong_ty.json', encoding='utf-8')
            noi_dung = json.load(f)
            f.close()
            Nhom_TV=[]
            # ....

            conn = sqlite3.connect('D:\PYTHON\Python-T3H\ThucHanh\Bai9-wxFormbuilder\Dulieu\product.db')
            sql='insert into tblNhomTivi(....) values(?,?,?,?,?)'
            # conn.execute(sql,(........))
            conn.commit()
            conn.close()

        if selection_ == 3:
            pass
        
        continue_ = int(input('Bạn muốn tiếp tục giao dịch không ? 1:có/ 0:không: \t'))

if __name__=='__main__':
    load_json_sqlite()


