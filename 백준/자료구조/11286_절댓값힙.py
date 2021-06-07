import heapq
import sys

'''
11286 절댓값 힙
https://www.acmicpc.net/problem/11286

절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.

배열에 정수 x (x ≠ 0)를 넣는다.
배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.

첫째 줄에 연산의 개수 N(1≤N≤100,000)이 주어진다. 
다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 
만약 x가 0이 아니라면 배열에 x라는 값을 넣는(추가하는) 연산이고, 
x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 
입력되는 정수는 -231보다 크고, 231보다 작다.


절댓값함수 : abs(x)
'''

def 절댓값힙():
  n = int(sys.stdin.readline())
  l = []

  for _ in range(n):
    x = int(sys.stdin.readline())
    if x != 0 :
      heapq.heappush(l, (abs(x), x))
    else:
      if len(l) ==0:
        print(0)
      else:
        print(heapq.heappop(l)[1])



if __name__ == "__main__":
  절댓값힙()