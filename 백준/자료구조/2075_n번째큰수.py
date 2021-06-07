import heapq
import sys

'''
5 7 9 12 15
6 8 11 13 19
10 16 21 26 31
14 25 28 35 48
20 32 41 49 52
'''


def n번째큰수() :
  n = int(input())
  l = []

  for _ in range(n):
    nums = list(map(int,sys.stdin.readline().split()))

    if not l: 
        # 초기 list : push만
        for num in nums:
            heapq.heappush(l,num)
    else:
        # n번째큰수를 구하는거이므로
        for num in nums:
            if l[0] < num:
                # 힙 정렬된 list에서 0번째 요소보다 크다면 넣고뺀다
                heapq.heappush(l,num)
                heapq.heappop(l)
    
    heapq.heapify(l)

  print(l[0])


if __name__=="__main__":
  n번째큰수()