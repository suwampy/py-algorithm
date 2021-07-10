def 재귀함수와스택():
    n = int(input())
    DFS(n)

def DFS(x) :
    if x>0:
        DFS(x-1)
        print(x, end=' ')

    '''
    if x>0:
        print(x, end = ' ')
        DFS(x-1)
    
    print(x)가 DFS 위에 있을 때는
    3 2 1, 
    
    DFS 밑에 있을 때는                                                                                                                                                                                                                                                                                                                              
    1 2 3 
    으로 호출 되는데
    이것은 재귀함수는 스택 구조를 사용하기기 때문
   
    '''


if __name__ == "__main__":
    재귀함수와스택()