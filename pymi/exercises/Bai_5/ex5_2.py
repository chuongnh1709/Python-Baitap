#!/usr/bin/env python3

'''
Tips: dùng stdlib copy.deepcopy

In [14]: import copy

In [15]: d = [{'name': 'Dung', 'languages': ['C', 'Python']}]

In [16]: dnew = copy.deepcopy(d)

In [18]: dnew[0]['languages'].append('Elixir')

In [19]: dnew
Out[19]: [{'languages': ['C', 'Python', 'Elixir'], 'name': 'Dung'}]

In [20]: d
Out[20]: [{'languages': ['C', 'Python'], 'name': 'Dung'}]
'''


data = [
    {"name": "Hoang",
     "phone": "0988888888",
     "languages": ["Python", "C", "SQL", "HTML", "CSS", "JavaScript",
                   "Golang"],
     },
    {"name": "Duy", "girl_friend": "Maria"},
    {"name": "Dai", "girl_friend": "Angela"},
    {"name": "Tu"},
]


def solve(last_year_data):
    '''
    Trả về list thông tin các học viên sau khi đã update sau 1 năm.
    Không thay đổi thông tin năm cũ.

    Biết các học viên đều học được các ngôn ngữ lập trình
    trong "languages" của học viên "Hoang".
    Sau đó "Hoang" học thêm được ngôn ngữ "Elixir", các học
    viên khác không biết ngôn ngữ này.
    "Tu" có bạn gái tên là "Do Anh".
    "Duy" chia thay bạn gái, không còn bạn gái nữa.
    '''
    result = []

    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    # raise NotImplementedError("Học viên chưa làm bài này")

    import copy
    
    current_year_data = copy.deepcopy(last_year_data)
    hoang_lang = []
    for i in range(len(current_year_data)):
        if current_year_data[i]['name'] == 'Hoang':
            hoang_lang = current_year_data[i]['languages']

    for i in range(len(current_year_data)):
        if current_year_data[i]['name'] != 'Hoang' :
            current_year_data[i]['languages'] = hoang_lang
            if current_year_data[i]['name'] == 'Tu':
                current_year_data[i]['girl_friend'] = 'Do Anh'
            if current_year_data[i]['name'] == 'Duy':
               del current_year_data[i]['girl_friend'] 
        else:
            current_year_data[i]['languages'].append('Elixir')

            
    result = current_year_data
    return result


def main():
    # Cho list chứa các dictionary chứa thông tin của các học viên:
    students = data
    # In ra màn hình tên học viên kèm tên bạn gái (nếu có)
    for i in range(len(students)):
        if len(students[i]['name']) > 0 :
            print(students[i]['name'])
                              
    result = solve(students)  # NOQA
    # In ra các thông tin đã thay đổi so với năm trước của mỗi học viên.
    # ko can sort do list moi duoc copy tu list cu, neu so sanh 2 list bat ky
    # thi phai sort 
    diffkeys = [k for k in range(len(result)) if result[k] != students[k]]
    for k in diffkeys:
      print (k, ':', result[k], '->', students[k])                              
        

if __name__ == "__main__":
    main()
