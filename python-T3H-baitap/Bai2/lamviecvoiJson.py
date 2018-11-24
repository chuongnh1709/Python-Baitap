import json
import urllib.request
from thu_vien_b2.read_json_from_intenet_unicode import *

url_string = 'http://dev-er.com/service_api_ban_sach/api_service_sach.php'
url = urllib.request.urlopen(url_string)
data = json.loads(url.read().decode())
# print(data)
print('Tong so sach : ', len(data))
print('Danh sach sach : ')
count=1
for i in data:
    print(count, '/', i['ten_sach'], 'Ngay Xuat ban: ', i['ngay_xuat_ban'], 'Gia Bia: ',i['gia_bia'])
    count+=1

