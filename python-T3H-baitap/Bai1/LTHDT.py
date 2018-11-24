class HinhChuNhat():
    def __init__(self, _cd, _cr):
        self._cd = cd
        self._cr = cr
    
    def Chuvi(self):
        return (self._cd + self._cr) * 2
    
    def Dientich(self):
        return self._cd * self._cr
    

if __name__ == "__main__":
    cd, cr = eval(input('nhap chieu dai, chieu rong : '))
    HCM = HinhChuNhat(cd, cr)
    chuvi = print(HCM.Chuvi())
    dientich = print(HCM.Dientich())

