#!/usr/bin/env python3


data = ['Trang', 'Trung', 'Tien',
        'Dai', 'Duong', 'Dung', 'Hung', 'Huy', 'Hoang']

MAGIC_NUMBER = 20200000


def solve(students, N=5):
    '''Biết những bạn có tên bắt đầu bằng chữ `D` sẽ ngồi phòng thi số N,
    các bạn có tên bắt đầu chữ `H` ngồi phòng thi số N+1, và các bạn còn lại,
    nếu có tên kết thúc là `ng` sẽ ngồi cùng phòng các bạn tên `H`, còn lại
    ngồi cùng phòng `D`.
    Tất cả các học viên đều sinh năm 1990.
    Mã học viên được tính bằng: hash(NAME) % MAGIC_NUMBER
    (chú ý số này mỗi lần chạy sẽ khác nhau).
    Ví dụ: mã học viên của 'Dung' là: hash('Dung') % MAGIC_NUMBER

    Trả về result là list các tuple chứa
    (mã sinh viên, tên học viên, năm sinh, phòng thi), sắp xếp
    theo thứ tự tên học viên.
    '''

    result = []
    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    # raise NotImplementedError("Học viên chưa làm bài này")

    nam_sinh = []
    ma_hv = []
    phong = []
    #for i in range(len(data)):
    for i in data :
        nam_sinh.append('1990')
        ma_hv.append(hash(i) % MAGIC_NUMBER)
        if i[0] == 'H' or i[-2:] == 'ng':
            phong.append(N+1)       
        else:
            phong.append(N)   
    result = list(zip(ma_hv,data,nam_sinh,phong))
    return result


def main():
    students = data
    # Cho danh sách học viên students
    for msv, *ignore, room in solve(students):
        print(msv, room)
        print("DEBUG", ignore, type(ignore), len(ignore))


if __name__ == "__main__":
    main()
