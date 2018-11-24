import re

noi_dung = 'COng hoa xa hoi chu nghia viet nam'
gia_tri_tim = input('Tim gi: ')
matchObj = re.search(r'(.*)'+gia_tri_tim+('.*'), noi_dung, re.M| re.I)

if matchObj:
    print('Tim thay')
else : 
    print('Khong tim thay')

#### Tìm kiếm và thay thế #### 
# phone = "(08) 38-3521332 # This is Phone number"
# # Delete comment
# num = re.sub(r'#.*$' ,"", phone)        # bắt đầu từ dấu # trở về sau
# print ("Phone number : ", num)

# # Remove anything other than digit
# num = re.sub(r'\D', "", phone)
# print ("Phone number : ", num)