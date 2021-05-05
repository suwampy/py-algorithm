import sys

def k번째수():
    t = int(sys.stdin.readline())
    for i in range(0,t):
        n,s,e,k = map(int, input().split())
        ##  map은 리스트의 요소를 지정된 함수로 처리해주는 함수
        #map이편하네..참ㅋㅋ
        a = list(map(int, input().split()))
        a=a[s-1,e]
        a.sort()
        print("#d %d" %(t+1,a[k-1]))
        #print(a[k])

if __name__=="__main__":
    k번째수()