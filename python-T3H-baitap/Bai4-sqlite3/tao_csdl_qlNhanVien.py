import sqlite3
conn = sqlite3.connect('dulieu/qlNhanVien.db')
sql = '''
create table phong (
    id integer primary key,
    ten text not null unique,
    chuc_nang text not null
);
'''
conn.execute(sql)
conn.commit()
conn.close()