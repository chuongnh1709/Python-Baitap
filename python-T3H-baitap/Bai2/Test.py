import json
f = open('QLCT_1.json',encoding='utf8')
data=json.load(f)
f.close()

print(data['CONG_TY'][0]['Ten'])
