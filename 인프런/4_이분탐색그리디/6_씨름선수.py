import sys

def 씨름선수():
    n = int(input())
    list=[]

    for _ in range(n):
        t1, t2 = map(int,input().split())
        list.append((t1, t2))

    list.sort(reverse=True)
    print(list)

    cnt = 1
    upper = list[0][1]

    for i in range(1,n):
        if list[i][1] >=upper:
            cnt+=1
            upper = list[i][1]

    print(cnt)

if __name__ =="__main__":
    씨름선수()