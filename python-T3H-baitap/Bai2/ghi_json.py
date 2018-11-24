import json
noi_dung={'Ho_ten':'Nguyen van A', "Dia_chi":'Nguyen Chi Thanh'}
f = open("ho_ten.json",'w')
json.dump(noi_dung, f, indent=4, ensure_ascii=False)        # ensure_ascii=False : để ko mã hóa ASCII (tiếng Việt)
f.close()

