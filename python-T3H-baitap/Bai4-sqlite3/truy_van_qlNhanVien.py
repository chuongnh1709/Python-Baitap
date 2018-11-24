import sqlite3
from sqlite3 import Error


conn = sqlite3.connect('D:/Python - T3H/ThucHanh/Bai4/dulieu/qlNhanVien.db')
# sql='insert into PHONG(id,ten,chuc_nang) values(?,?,?)'
# conn.execute(sql,(str(i),'Hành Chính '+str(i),'Giải quyết cv hành chính cty'))
sql = 'select * from phong'
cursor = conn.execute(sql)

# print('ID   Ten Phong       Chuc nang')
# for row in cursor:
#     print('ID = ', row[0] ,'Ten phong = ', row[1], 'Chuc nang = ', row[2])
# or 
for row in conn.execute('select * from phong where id between 2 and 8'):
    print(row)

conn.close()

import sqlite3
from sqlite3 import Error


conn = sqlite3.connect('D:/Python - T3H/ThucHanh/Bai4/dulieu/qlNhanVien.db')
# sql='insert into PHONG(id,ten,chuc_nang) values(?,?,?)'
# conn.execute(sql,(str(i),'Hành Chính '+str(i),'Giải quyết cv hành chính cty'))
sql = 'select * from phong'
cursor = conn.execute(sql)

# print('ID   Ten Phong       Chuc nang')
# for row in cursor:
#     print('ID = ', row[0] ,'Ten phong = ', row[1], 'Chuc nang = ', row[2])

for row in conn.execute('select * from phong where id between 2 and 8'):
    print(row)

conn.close()
