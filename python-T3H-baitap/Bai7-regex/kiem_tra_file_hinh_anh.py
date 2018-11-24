import re
ten_file = input('Nhap ten file: ')
matchObj = re.match(r'^([A-Z0-9._%+-]{3,})+(\.(jpg|png|bmp|gif))$',ten_file, re.M|re.I)
                                    #{3,} phần tên phải có 3 ký tự 

if matchObj:
    print('Ten hop le')
else:
    print('Ten ko hop le')

