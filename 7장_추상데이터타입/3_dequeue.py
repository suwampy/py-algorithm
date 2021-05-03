## 덱 : 스택과 큐의 결합체
## 양쪽 끝에서 항목의 조회, 삽입, 삭제가 가능
from collections import deque
if __name__ == "__main__":
    q = deque(["버피", "잰더", "윌로"])
    print(q.append("자일스"))
    print(q)# deque(['버피', '잰더', '윌로','자일스])
    print(q.popleft()) # '버피'
    print(q.pop()) # '자일스'
    print(q) # deque(['잰더','윌로'])
    print(q.appendleft('엔젤'))
    print(q) # depque(['엔젤','잰더','윌로']
    print(len(q))