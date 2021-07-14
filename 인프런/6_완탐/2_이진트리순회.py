def DFS(v):
    if v > 7 :
        return
    else :
        print(v, end =" ") # 전위 순회
        DFS(v*2)    # 왼쪽 노드 호출
        print(v, end = "") # 중위 순회
        DFS(v*2+1) # 오른쪽 노드 호출
        print(v, end ="") # 후위 순회

if __name__ == "__main__":
    DFS(1)