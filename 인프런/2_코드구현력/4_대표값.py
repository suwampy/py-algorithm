import sys

def 대표값():
    n = int(sys.stdin.readline())
    a = list(map(int, input().split()))
    ave = round(sum(a)/n)
    min = 214700000
    # enumerate(a): a list를 탐색할때 인덱스값을 밯놘해줌
    # idx에는 인덱스 값이 들어감
    # x에는 리스트의 값이 들어감
    for idx, x in enumerate(a):
        tmp=abs(x-ave) # abs : 절대값
        if tmp<min:
            min=tmp
            score=x
            res=idx+1
        # 같은 거리가 나ㅇ왔을 때
        elif tmp==min:
            if x>score:
                score=x
                res=idx+1

    print(ave,res)

if __name__ == "__main__":
    대표값()