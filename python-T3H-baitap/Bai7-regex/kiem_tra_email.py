import re

dia_chi_mail = input('Nhap email address :')
matchObj = re.match(r'^[A-Z0-9.%+=]+@[A-Z0-9.-]+\.[A-Z]{2,}$', dia_chi_mail, re.M|re.I)

if matchObj:
    print('Hop le')
else:
    print(dia_chi_mail, ' Khong hop le')

# chuong@yahoo.com : ok 
# chuong_ngn@yahoo.com : not ok 