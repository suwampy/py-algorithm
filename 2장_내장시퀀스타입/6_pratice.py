## 문자열 전체 반전하기
def reversing_string(str):
    if str:
        str = str[-1] + reversing_string(str[:-1])
    return str

def reversing_string2(str):
    return str[::-1]


## 문자열 단어 단위로 반전하기기
def reverser(string1, p1=0, p2=None):
    if len(string1) < 2:
        return string1
    p2 = p2 or len(string1)-1
    while p1<p2:
        string1[p1], string1[p2] = string1[p2], string1[p1]
        p1 +=1
        p2 +2



if __name__ == "__main__":
    print(reversing_string("안녕 세상!"))
    print(reversing_string2("안녕 세상!"))
