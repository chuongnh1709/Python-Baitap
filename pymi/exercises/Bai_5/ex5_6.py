#!/usr/bin/env python3

term1 = {'math': 3, 'python': 5, 'data': 2}
term2 = {'math': 7, 'python': 9, 'SQL': 8, 'HTML': 6}
data = [term1, term2]


def solve(term1, term2):
    '''Trả về result là dict chứa bảng điểm của các môn học sau hai học kỳ.
    Biết điểm số được chọn là điểm số ở lần học sau cùng.
    '''

    result = {}
    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    # raise NotImplementedError("Học viên chưa làm bài này")

    s1 = set(term1)
    s2 = set(term2)
    s3 = (s1 ^ s2)  
    s3 = s1 - s1.intersection(s2) | s2
    result = {i:term2[i] if i in term2 else term1[i] for i in s3}

    return result

    
def main():
    # Một học viên có bảng điểm học kỳ 1 trong term1
    # Học kỳ 2, học thêm/lại có bảng điểm trong term2

    print(solve(*data))


if __name__ == "__main__":
    main()
