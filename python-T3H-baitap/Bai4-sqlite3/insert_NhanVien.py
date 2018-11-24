import sqlite3
conn = sqlite3.connect('D:/Python - T3H/ThucHanh/Bai2/dulieu/qlNhanVien.db')
sql='insert into PHONG(id,ten,chuc_nang) values(?,?,?)'
for i in range(2,10):
    conn.execute(sql,(str(i),'Hành Chính '+str(i),'Giải quyết cv hành chính cty'))
    conn.commit()

conn.close()