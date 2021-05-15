import sys

# 그리디 알고리즘 = 문제를 해결하는 단계에 있어서 가장 좋은 방법 선택!!
# 그리디는 거의.. 정렬과 동반됨
def 회의실배정():
    n = int(input())
    list = []
    for _ in range(n):
        t1, t2 = map(int, input().split())
        list.append((t1, t2)) # tuple 로 넣는당

    list.sort(key=lambda x : (x[1], x[0])) # x[1]이 1순위, x[0]이 2순위
    print(list)

    et = list[0][1]
    cnt = 1

    for i in range(1,n):
        if list[i][0] >= et:
            print(list[i])
            cnt+=1
            et = list[i][1]

    print(cnt)

if __name__ == "__main__":
    회의실배정()