'''
무게가 서로 다른 k개의 추와 빈 그릇이 있다...
양팔저울을 한 번만 이용하여 원하는 물의 무게를 그릇에 담자

추의 무게 {1,5,7}
모든 추 무게의 합 S=13
그릇에 담을 수 있는 물의 무게 {1,2,3,4,5,6,7,8,11,12,13}
9와 10은 담을수없삼

경우=>왼쪽(+1), 오른쪽(-1), 넣지않는다(0)
'''

def DFS(L, sum):
    global res

    if L == n:
        if 0<sum<=s:
            res.add(sum)
    else:
        DFS(L+1, sum+G[L]) # 왼쪽 추 :더한다
        DFS(L+1, sum-G[L]) # 오른쪽 추 : 뺀다
        DFS(l+1, sum) # 넣지 않는다다

if __name__=="__main__":
    n =int(input())
    G=list(map(int, input().split()))
    s=sum(G) #추 무게의 총합
    res=set() # 중복 제거하면서 값 추가. 특정 될 수 있는 무게
    DFS(0,0)

    print(s-len(res))
