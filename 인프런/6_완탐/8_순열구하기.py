# 어려워ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ

def DFS(L):
    if L == m :
        for i in range(L):
            print(res[i],end=" ")
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            ## 체크리스트 확인
            if ch(i)==0:
                ch[i]=1
                res[L]=i
                DFS(L+1)
                #back을하고 되돌아와서 다시 0으로 풀어줌
                ch[i]=0

if __name__=="__main__":
    n,m = map(int,input().split())
    res = [0] * m

    '''
    체크리스트를 만들어야해 [0,0,0,0] 0으로 초기화
    D(0)
    '''
    ch = [0] * (n+1)
    cnt=0
    DFS(0)
    print(cnt)