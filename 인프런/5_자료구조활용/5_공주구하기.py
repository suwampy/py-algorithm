## 큐
# 선입선출
# deque 자료구조를 사용해서 큐를 구현할 수 있다
import sys
from collections import deque

n, k = map(int, input().split())
dq=list(range(1,n+1))
dq = deque(dq)

while dq:
    for _ in range(k-1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq)==1:
        print(dq[0])
        dq.popleft()