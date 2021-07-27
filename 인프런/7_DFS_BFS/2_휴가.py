'''
n+1일 되는 날 휴가
n일동안 일을 하자~

하루에 하나씩 서로 다른 사람의 상담이 예약되어있음
상담을 완료하는데 걸리는 날수 T
상담을 했을 때 받을 수 있는 금액 P
1일 : 4 20 # 총 4일이 걸림, 20을 받을 수 있음 4일까지는 상담을 할 수 없음
이 상담을,,,,, 하느냐 안하느냐?
한다->5일째로
안한다->2일째로
'''
def DFS(L,sum):
    global res

    if L == n+1:
        if sum>res:
            res=sum
    else:
        if L+T[L]<=n+1: #상담을한다
            DFS(L+T[L],sum+P[L]) #현재날짜+상담에 걸리는 날짜
        DFS(L+1,sum) #다음날짜로

if __name__ == "__main__":
    n = int(input())
    T=[]
    P=[]
    for _ in range(n):
        t,p = map(int,input())
        T.append(t)
        P.append(p)
    res = -2147000000

    # 인덱스 번호를 날짜로 사용하기 위해 0인덱스에 0 삽입
    T.insert(0,0)
    P.insert(0,0)

    DFS(1,0)
    print(res)