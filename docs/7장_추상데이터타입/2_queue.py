## 큐
## 항목이 들어온 순서대로 접근 가능
## 먼저 들어온 데이터가 먼저 나가는 선입선출(FIFO) 구조
## 배열의 인덱스 접근이 제한됨
## 롤러코스터 타는 것을 기다리는 사람들의 줄~
## 시간복잡도는 모두 O(1)

# enqueue : 큐 뒤쪽에 항목을 삽입
# dequeue : 큐 앞쪽의 항목을 반환하고 제거
# peek/front : 큐 앞쪽의 항목을 조회
# empty : 큐가 비어있는지 확인
# size : 큐의 크기를 확인

class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not bool(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        value = self.items.pop()
        if value is not None:
            return value
        else:
            print("Queue is empty.")

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("Queue is empty.")

    def __repr__(self):
        return repr(self.items)

