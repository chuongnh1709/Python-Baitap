#!/usr/bin/env python3

from fractions import Fraction as F


def solve(*args):
    '''Return tổng (kiểu float) của các phân số trong args

    https://docs.python.org/3/library/fractions.html
    Thư viện fractions cung cấp class Fraction để tạo ra kiểu phân số trên
    Python.

    Tham khảo:
    http://www.familug.org/2017/03/python-fractions-tinh-toan-phan-so-tren.html
    '''
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")
    result = sum([F(i) for i in args])
    return result


def main():
    print(solve('1/10', '1/10', '1/10'))


if __name__ == "__main__":
    main()
