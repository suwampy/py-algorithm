import sys

def 경고():
    h1, m1, s1 = map(int, input().split(":"))
    h2, m2, s2 = map(int, input().split(":"))

    t1 = h1*60+60 + m1*60 + s1
    t2 = h2 * 60 + 60 + m2 * 60 + s2

    t = t2 -t1

def test():
    s="try hello world"
    answer=''
    l = s.split()
    for i in l:
        for j in range(0,len(i)):
            if j % 2 == 0 :
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        else:
            answer+=" "
    answer=answer[:len(answer)-1]
    print(answer)
if __name__ == "__main__":
    test()