## 스택
# 스택은 배열의 끝에서만 접근할 수 있는 선형 자료 구조임
# 스택은 배열 인덱스 접근이 제한되며
# 후입선출(LIFO) 구조. 책상 위에 쌓여 있는 책을 연상
# 시간 복잡도는 모두 O(1)

# push : 스택 맨 끝(맨 위)에 항목을 삽입
# pop : 스택 맨 끝 항목을 반환하는 동시에 제거
# top/peek : 스택 맨 끝 항목을 조회
# empty : 스택이 비어 있는지 확인
# size : 스택 크기를 확인

# 파이썬에서는 리스트의 append() 와 pop() 메서드로 스택을 구현할 수 있음
class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not bool(self.items)

    def push(self,value):
        self.items.append(value)

    def pop(self):
        value = self.items.pop()
        if value is not None:
            return value
        else:
            print("Stack is empty.")

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("Stack is empty.")

    def __repr__(self):
        return repr(self.items)

if __name__ == "__main__":
    stack = Stack()
    print("스택이 비었나요? {0}".format(stack.isEmpty()))