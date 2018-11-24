import json
import sqlite3

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
