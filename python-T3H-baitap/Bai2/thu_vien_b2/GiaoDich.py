'''
Giao dich Vàng và Tiền có chung nhiều thuộc tính -> xây dựng lớp giao dịch (mặc định là Vàng)
Tiền tệ = gd vàng có thêm thuộc tính mua/bán
'''

class GiaoDich(object):
    def __init__(self, ma, ngay, don_gia, so_luong, loai):
        self.ma = ma
        self.ngay = ngay
        self.don_gia = don_gia
        self.so_luong = so_luong
        self.loai = loai

    def thanh_tien(self):
        return self.so_luong * self.don_gia

    def in_giao_dich(self):
        return self.ma + " - " + self.ngay + " - " + self.loai + " - " + str(self.so_luong)\
        + " - " + str(self.don_gia) + " - " + str(self.thanh_tien)

class GiaoDichTienTe(GiaoDich):
    '''
    classdocs: class GiaoDichTienTe kế thừa lớp GiaoDich 
    '''

    def __init__(self, ma, ngay, don_gia, so_luong, loai, mua):
        '''
        Contrucstor
        '''
        self.mua = mua      # thuộc tính riêng của lớp con 
        #super().__init__(ma, ngay, don_gia, so_luong, loai)
        GiaoDich.__init__(self, ma, ngay, don_gia, so_luong, loai)

    def thanh_tien(self):
        if self.mua:
            return GiaoDich.thanh_tien(self)    # gọi phương thức cha
        else:
            return GiaoDich.thanh_tien(self) * 1.05     # overwrite phương thức cha

    def in_giao_dich(self):
        if self.mua == True:
            return "GD Mua : " + GiaoDich.in_giao_dich(self)
        else :
            return "GD Ban : " + GiaoDich.in_giao_dich(self)

    