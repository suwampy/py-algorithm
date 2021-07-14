def 이진수출력():
    n = int(input())
    DFS(n)

def DFS(x):
    if x == 0:
        return
    else:
        DFS(x//2)
        print(x % 2, end='')

if __name__ == "__main__":
    이진수출력()