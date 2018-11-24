import json

f = open('ho_ten.json',encoding='utf-8')
noi_dung = json.load(f)
f.close()
noi_dung_bo_sung = {"dien_thoai":"12345678", "Email":"asbc@gmail.com"}
noi_dung.update(noi_dung_bo_sung)
f = open('ho_ten.json','w', encoding='utf-8')
json.dump(noi_dung, f, indent=4, ensure_ascii=False)
f.close()
