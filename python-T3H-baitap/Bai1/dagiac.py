import abc
import math

class Hinh(abc.ABC):     # bắt buộc phải xây dựng tất cả phương thức trừu tượng ở lớp con con 
    '''
    classdocs : Hinh la abstract base class
    '''
    # class Hinh(object)
    # __metaclass__ = abc.ABCMeta     : nhu vầy là ko bắt buộc phải viết lại các phương thức trừu tượng 

    @classmethod
    @abc.abstractmethod
    def tinh_chu_vi(self):
        pass

    @abc.abstractmethod
    def tinh_dien_tich(self):
        pass


class HinhTron(Hinh):
    '''
    classdocs : HinhTron tinh chu vi va dien tich
    phai xay dung 2 phuong thuc tinh_chu_vi va tinh_dien_tich
    lop cha xay dung phuong thuc truu tuong gi thi lop con phai xay dung lai phuong thuc do
    '''

    def __init__(self, r):
        self.r = r

    def tinh_chu_vi(self):
        return 2* math.pi * self.r

    def tinh_dien_tich(self):
        return math.pi * math.pow(self.r, 2)

'''
hinh chu nhat
'''

if __name__ =='__main__':
    hinhtron = HinhTron(3)
    print("Chu vi : " + str(hinhtron.tinh_chu_vi()))
    print("Dien tich : " + str(hinhtron.tinh_dien_tich()))


    
