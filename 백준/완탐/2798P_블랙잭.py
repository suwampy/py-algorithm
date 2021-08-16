from itertools import permutations
'''
1. for, if 문을 반복해서 처음부터 끝까지 탐색하는 방법

2. 순열, 조합을 사용하는 방법

3. 재귀함수를 사용하는 방법

4. 비트마스크를 사용하는 방법

5. 백트래킹을 사용하는 방법

6. bfs를 사용하는 방법

출처: https://ebbnflow.tistory.com/241 [Dev Log : 삶은 확률의 구름]
'''
if __name__ == "__main__":
   n ,m = map(int,input().split())

   # 라이브러리를 통한 완탐 508ms
   res=0
   a=list(permutations(list(map(int,input().split())),3))

   for i in range(len(a)):
       temp = sum(a[i])

       if temp <=m and res<=temp:
           res = temp

   print(res)

def sol():
    # 3중반복문을 통한...완탐 132ms
    n, m =list(map(int, input().split()))
    data = list(map(int, input().split()))

    result = 0
    length = len(data)

    for i in range(0, length):
        for j in range(i+1, length):
            for k in range(j+1, length):
                sum_value = data[i] + data[j] + data[k]
                if sum_value <= m:
                    result = max(result, sum_value)

    print(result)