


class Donvi(object):
    '''
    classdocs : Class Don Vi
    '''
    def __init__(self, iddv, ten):
        self.iddv = iddv
        self.ten = ten


class NhanVien(object):
    '''
    classdocs : Class Nhan Vien 
    '''

    def __init__(self,iddv, ho_ten, gioi_tinh, ngay_sinh, cmnd, muc_luong, dia_chi, idnv):
        self.iddv = iddv
        self.ho_ten = ho_ten
        self.gioi_tinh = gioi_tinh
        self.ngay_sinh = ngay_sinh
        self.cmnd = cmnd
        self.muc_luong = muc_luong
        self.dia_chi = dia_chi
        self.idnv = idnv

    def in_thong_tin(self):
        # gioi_tinh = ""
        if self.gioi_tinh == 'true':
            gioi_tinh = "Nam"
        else: 
            gioi_tinh = "Nu"
        
        print(self.idnv + "-" +self.ho_ten +"-"+ self.gioi_tinh +"-"+ self.ngay_sinh\
        +"-"+ self.cmnd +"-"+ self.muc_luong +"-"+ self.dia_chi)

