if __name__ == "__main__":
    T=int(input()) #테스크 케이스의 개수

    # M = 배추를 심은 배추밭의 가로길이
    # N = 세로길이
    # K = 배추가 심어진 위치으 ㅣ개수
    for _ in range(T):
        m, n, k = map(int, input().split())

        #좌표
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]

        l=[]
        # 배추의 위치 X, Y
        for i in range(k):
            X,Y=map(int, input().split())
            l.append([X,Y])

    print(l)
