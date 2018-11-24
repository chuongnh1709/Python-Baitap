#!/usr/bin/env python3


data = {
    'xanh lá': '#3cba54',
    'vàng': '#f4c20d',
    'đỏ': '#db3236',
    'xanh da trời': '#4885ed',
}


def solve(colors):
    '''Ghi ra file index.html code HTML để tạo ra logo của Google với màu sắc
    chính xác.
    Biết cách để tạo chữ G màu xanh da trời dùng code HTML sau::

      <span style="color:#4885ed">G</span>

    Return list chứa các tuple, mỗi tuple  chứa chữ cái trong 'Google' và màu
    của nó.
    Gợi ý: dùng `zip`

        In [1]: list(zip(['xanh', 'do'], ['XXX', 'YYY']))
        Out[1]: [('xanh', 'XXX'), ('do', 'YYY')]
    '''
    result = []
    
    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    # raise NotImplementedError("Học viên chưa làm bài này")


    char = 'Google'
    google_color = [colors['xanh da trời'],colors['đỏ'],colors['vàng'],colors['xanh da trời'],colors['xanh lá'],colors['đỏ']]
    list_ = list(zip(char, google_color ))
    
    f = open('/home/chuong/index.html', 'wt')
    for i in list_:
        f.write('<span style="color:{0}">{1}</span>'.format(i[1],i[0]))

    f.close()    
    return result


def main():
    '''Biết mã hex của các màu trong Google logo là:
    '''
    colors = data
    print(solve(colors))


if __name__ == "__main__":
    main()
