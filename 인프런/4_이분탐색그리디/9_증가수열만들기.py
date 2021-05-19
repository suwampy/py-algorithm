from collections import deque


def 증가수열():
    n = int(input())
    a = list(map(int, input().split()))
    lt=0
    rt=n-1
    last =0
    res="" #문자열

    tmp=[] #빈 list

    while lt<=rt:
        if a[lt]>last:
            tmp.append((a[lt],'L'))
        if a[rt]<last:
            tmp.append((a[rt],'R'))
        tmp.sort()
        if len(tmp)==0:
            break
        else:
            res=res+tmp[0][1]
            last=tmp[0][0]
            if tmp[0][1]=='L':
                lt+=1
            else:
                rt+=1
        tmp.clear()
    print(len(res()))
    print(res)

if __name__ =="__main__":
    증가수열()