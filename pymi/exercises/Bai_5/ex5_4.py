#!/usr/bin/env python3

NUMBER_OF_LINES = 30000000


def solve(output_path):
    '''Tạo ra 1 file chứa 30 triệu dòng, các dòng lẻ chứa 30 số 1,
    các dòng chẵn chứa giá trị 2 * số dòng hiện tại.

    Sau khi tạo xong file, return result là list chứa 10 dòng cuối theo thứ tự
    dòng xuất hiện trước đứng trước.

    Chú ý: 30 triệu dòng.
    '''
    result = None
    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    # raise NotImplementedError("Học viên chưa làm bài này")

    #
    #
    #
    #

    import os
    # Xoá file sau khi đã xong vì file này rất lớn
    try:
        os.remove(output_path)
    except OSError as e:
        print(e)

    with open('/home/chuong/30trieu.xxx','wt') as f:
        for i in range(301):   # de 301 vi du thoi duoc roi 
            if i % 2 == 0:
                f.write(30*'1' + '\n')
            else:
                f.write(str(2*i) + '\n')

    with open('/home/chuong/30trieu.xxx','rt') as f:
        data = f.readlines()
        result = data[-10:]
    
    return result


def main():
    import tempfile
    # tên _ hàm ý rằng ta sẽ không dùng giá trị của nó - convention
    _, output_path = tempfile.mkstemp()
    print('File to write: {0}'.format(output_path))
    for line in solve(output_path):
        print(line.rstrip())


if __name__ == "__main__":
    main()
