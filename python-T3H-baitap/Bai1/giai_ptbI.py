class PTBN():
    def __init__(self, _a, _b):
        self.a = _a
        self.b = _b
    def TinhNghiem(self):
        nghiem = None
        if self.a==0 and self.b!=0:
            nghiem = 'Phuong trinh vo nghiem'
        elif self.a==0 and self.b==0:
            nghiem = "Phuong trinh vo so nghiem"
        else:
            nghiem = - self.b / self.a
        return nghiem
if __name__ =="__main__":
    a, b = eval(input('Nhap vao tham so a, b: '))
    ptbn = PTBN(a, b)
    # print(ptbn.TinhNghiem())

    if hasattr(ptbn, 'a'):
        print('thuoc tinh a : ' + str(getattr(ptbn, 'a')))