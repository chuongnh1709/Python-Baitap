#!/usr/bin/env python3


def add_item(result,element,counter):
        if counter == 1:
            result.append(element)
        else:
            result.append(2*element + str('-' + counter))
    

def solve(text):
    '''Thc hin bin đi

      input: [a, abbbccccdddd, xxyyyxyyx]
      output: [a, abb3cc4dd4, xx2yy3xyy2x]

    Gii thích: Nhng ch cái không lp li thì output gi nguyên ch cái đó.
    Nhng ch cái liên tip s in ra 2 ln + s ln lp li liên tip.

    Đây là mt bin th ca mt thut toán nén d liu có tên Run-length
    encoding (RLE).
    NOTE: không dùng itertools.groupby
    '''
    result = []

    # Xoá dòng sau và vit code vào đây set các giá tr phù hp
    # raise NotImplementedError("Hc viên cha làm bài này")

    input_text = list(text)
    count = 1
    first_char = input_text[0]
    if len(input_text) > 1:
            for i in range(1,len(input_text)):
                    cur_char = input_text[i]
                    if cur_char == first_char:
                            count += 1
                    else:
                            add_item(result, first_char, count)
                            count = 1
                            first_char = cur_char
            add_item(result, cur_char, count)
    else:
            add_item(result, cur_char, count)
    result = ' '.join(result)
    return result

def add_item(result_list, char, count):
        if count == 1:
                result_list.append(char)
        else:
                result_list.append(2*char + str(count))


# def solve(text):
#    count=1
#    result=""
#    for i in range(1,len(text)):
#        if text[i-1]==text[i]:
#           count+=1
#        else :
#            result+= printchar(text[i-1],count)
#            count=1
#    result+= printchar(text[i],count)
#    return result

# def printchar(chr, count):
#    if count==1:
#        return chr
#    else:
#        return 2*chr+str(count)

#-- So lan character xuat hien trong word, ko can lien tiep
# def solve(text):
#    solved_char = []
#    result=[]
#    for i in text:
#        if i not in solved_char:
#            if text.count(i) == 1:
#                result.append(i)
#            else:
#                result.append(2*i + str(text.count(i)))
#            solved_char.append(i)
#    return ''.join(result)	

def main():
    print(solve('abbbccccddddaaj'))


if __name__ == "__main__":
    main()
