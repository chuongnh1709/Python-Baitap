#!/usr/bin/env python3


def solve(*args, **kwargs):
    '''Return tuple chứa
    - Đường dẫn tới code của module `os`
    - list chứa các attribute của os và sys
    - Số dòng trong module `os`

    Biết dir(object) sẽ trả về tất cả thuộc tính (attribute) của object đó.
    Module cũng là object.

    In [11]: import os

    In [12]: len(dir(os))
    Out[12]: 284
    '''

    import sys, os

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")
    num = 0
    with open(os.__file__,'r') as f:
        for line in f:
            num += 1
    
    return (os.__file__,dir(os) + dir(sys), num)


def main():
    print(solve())


if __name__ == "__main__":
    main()
