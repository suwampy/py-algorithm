import sys

def 소수의개수():
    n = int(sys.stdin.readline())
    ch=[0]*(n+1)
    cnt=0
    #2부터 n까지 돈다
    for i in range(2,n+1):
        # 소수인지 아닌지 확인
        if ch[i] == 0 :
            cnt+=1
            # i의 배수 체크
            for j in range(i, n+1, i): #start, end, step
                ch[j]=1
    print(cnt)

if __name__ == "__main__":
    소수의개수()