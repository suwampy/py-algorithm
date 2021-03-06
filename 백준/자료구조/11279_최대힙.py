import heapq
import sys
'''
11279 최대 힙
https://www.acmicpc.net/problem/11279

널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

배열에 자연수 x를 넣는다.
배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.
'''

def 최대힙():
  n = int(sys.stdin.readline())
  l = []

  for _ in range(n):
    x = int(sys.stdin.readline())
    if x>0:
      # x가 자연수라면 배열에 x라는 값을 추가
      heapq.heappush(l, (-x, x))
    else:
      # x가 0이라면 배열에서 가장 큰 값을 출력하고 그값을 배열에서 추가
      if len(l)==0:
        print(0)
      else:
        print(heapq.heappop(l)[1])


if __name__ == "__main__":
  최대힙()