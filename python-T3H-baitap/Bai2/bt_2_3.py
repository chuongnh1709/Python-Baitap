import json
f = open('QLCT_1.json',encoding='utf8')
data=json.load(f)
f.close()
print(data)
CONGTY=data['CONG_TY'][0]
# print(data['CONG_TY'][0]['Ten'])   : 'Công ty Dịch vụ Hoàng hôn Sớm'
DONVI=data['DON_VI']
tong_so_nhan_vien = 0
for dv in DONVI:
    tong_so_nhan_vien+=int(dv['So_Nhan_vien'])
print('Tên công ty: ',CONGTY['Ten'])
print('Địa chỉ: ',CONGTY['Dia_chi'])
print('Tổng số nhân viên: ',tong_so_nhan_vien)


