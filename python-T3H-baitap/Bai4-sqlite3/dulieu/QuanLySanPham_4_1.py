import sqlite3

# from produclib import *       # để các function ở file/module khác 
def HienThiSP():    # 1
    conn = sqlite3.connect('D:/Python - T3H/ThucHanh/Bai4/dulieu/du_lieu_41/product.db')
    cursor = conn.execute('select id, name, price, amount from product')
    ds = cursor.fetchall()
    # ds = cursor.fetchone()      # nếu ko có thì trả về None
    conn.close()
    return(ds)

def DocSP(id):    # Trả về 1 dòng để check sản phẩm có tồn tại ko, ko có thì trả về None
    conn = sqlite3.connect('D:/Python - T3H/ThucHanh/Bai4/dulieu/du_lieu_41/product.db')
    sqlstr = 'select id, name, price, amount from product where id = ?'
    cursor = conn.execute(sqlstr,(id,))
    ds = cursor.fetchone()      # nếu ko có thì trả về None
    conn.close()
    return(ds)

def ThemSP(sp):     # 2     # hoặc ThemSP(name,price,amount)
    conn = sqlite3.connect('D:/Python - T3H/ThucHanh/Bai4/dulieu/du_lieu_41/product.db')
    sqlstr = 'insert into product(name, price, amount ) values(?,?,?)'
    cursor = conn.execute(sqlstr,(sp['name'],sp['price'],sp['amount']))
    n = cursor.rowcount
    conn.commit()
    conn.close()
    return(n)

def TimKiemSP(str):     # 3
    conn = sqlite3.connect('D:/Python - T3H/ThucHanh/Bai4/dulieu/du_lieu_41/product.db')
    BieuThucDieuKien = '%'+str+'%'
    sqlstr = 'Select * from product where lower(name) like lower(?)'
    # sqlstr = 'Select * from product where lower(name) like ?'    # where lower(name) like lower('%choi%');
    cursor = conn.execute(sqlstr,(BieuThucDieuKien,))
    ds = cursor.fetchall()
    conn.close()
    return(ds)

def CapNhatSP(sp):  # 4
    conn = sqlite3.connect('D:/Python - T3H/ThucHanh/Bai4/dulieu/du_lieu_41/product.db')
    sqlstr = 'update product set name=?, price=?, amount=? where id=?'
    cursor = conn.execute(sqlstr,(sp['name'],sp['price'],sp['amount'],sp['id']))
    n = cursor.rowcount
    conn.commit()
    conn.close()
    return(n)

def XoaSP(id):      # 5
    conn = sqlite3.connect('D:/Python - T3H/ThucHanh/Bai4/dulieu/du_lieu_41/product.db')
    sqlstr = 'Delete from product where id = ?'
    cursor = conn.execute(sqlstr,(id,))
    n = cursor.rowcount
    conn.commit()
    conn.close()
    return(n)

'''
Main function 
'''

def main():
    tt = 1
    while tt:
        print('Menu \n 1.Hien thi danh sach SP \n 2.Them SP moi \n 3.Tim kiem SP theo ten \
        \n 4.Cap nhat SP \n 5.Xóa SP ')
        chucnang = int(input('Chon chuc nang: '))
        sp={}

        if chucnang == 1 :      # List San Pham 
            dsSanPham = HienThiSP()
            if len(dsSanPham) > 0:
                for i in dsSanPham:
                    print('Ma SP: ', i[0], 'Ten SP: ', i[1], 'Gia Tien: ', i[2], 'SL: ', i[3])
            else:
                print('Khong co SP nao')
        
        elif chucnang ==2 :     # ThemSP
            sp['name'] = input('Nhap ten sp: ')
            sp['price'] = input('Nhap gia: ')
            sp['amount'] = input('Nhap SL: ')
            print(ThemSP(sp))  
            # ThemSP(name,price,amount)
            # hoặc 
            # name = 
            # price = 
            # amount = 
            # sp{'name':name, 'price':price, 'amount':amount}
        
        elif chucnang == 3 :    # TimKiemSP 
            str = input('Nhap vao Ten SP muon tim: ')
            # print(TimKiemSP(str), type(TimKiemSP(str)))
            kq = TimKiemSP(str)
            if len(kq) > 0:
                print(kq)
            else:
                print('Ko tim thay')

        elif chucnang == 4 :    # Cap Nhat San Pham 
            id = int(input('ID SP can Cap Nhat: '))
            sp = DocSP(id)
            if sp!= None:
                name = input('Ten = ')
                price = eval(input('Gia = '))
                amount = eval(input('SL = '))
                sp = {'id':id, 'name':name, 'price':price, 'amount':amount}
                
                if CapNhatSP(sp) == 1:
                    print('Da cap nhat')
                else :
                    print('Cap nhat khong thanh cong')         
            else:
                print('San Pham khong ton tai')

        elif chucnang == 5 :    # Xoa San Pham 
            id = input('Nhap ID muon Xoa: ')
            sp = DocSP(id)
            if sp != None:
                if XoaSP(id) == 1:
                    print('Đã xóa xong')
                else:
                    print('Xóa ko thành công')
            else :
                print('San pham ko ton tai')        

        else:
            print('Vui long Nhap chuc nang theo tuy chon 1,2,3,4,5 - hoac nhan 0 de thoat')
        tt = int(input ('Ban co muon tiep tuc khong (1:Yes / 0:No): '))


if __name__ == "__main__":
    main()


