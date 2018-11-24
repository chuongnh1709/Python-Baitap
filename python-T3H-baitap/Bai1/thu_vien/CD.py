class CD(object):
    '''
    classdocs : class CD
    '''
    tong_tien = 0
    def __init__(self, ten, ca_sy, so_bai_hat, gia_thanh):
        '''
        constructor
        '''
        self.ten = ten
        self.ca_sy = ca_sy
        self.so_bai_hat = so_bai_hat
        self.gia_thanh = gia_thanh
        CD.tong_tien += self.gia_thanh

    def thong_tin_cd(self):
        return ("# CD:  " + self.ten + " - " + self.ca_sy + " - "\
        + str(self.so_bai_hat)+ " - " + str(self.gia_thanh))