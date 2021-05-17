from collections import deque

def 타이타닉():
    n, limit = map(int,input().split())
    p = list(map(int,input().split()))
    p.sort()

    cnt = 0

    while p:
        if len(p)== 1 :
            cnt+=1
            break
        if p[0] + p[-1] > limit:
            p.pop()
            cnt+=1
        else:
            p.pop(0)
            p.pop()
            cnt+=1
    print(cnt)

def 타이이타닉withDeque():

    n, limit = map(int,input().split())
    p = list(map(int,input().split()))
    p.sort()
    p=deque(p)
    cnt = 0

    while p:
        if len(p)== 1 :
            cnt+=1
            break
        if p[0] + p[-1] > limit:
            p.pop()
            cnt+=1
        else:
            p.popleft()
            p.pop()
            cnt+=1
    print(cnt)


if __name__ =="__main__":
    타이타닉()