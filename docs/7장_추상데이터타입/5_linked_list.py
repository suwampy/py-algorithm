## 연결 리스트 : 값과 다음 노드에 대한 포인터(참조)가 포함된 노드로 이루어진 선형 리스트
# 마지막 노드는 null(None) 값을 가짐
# 또한 연결 리스트로 스택과 큐를 구현할 수 있음

class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer

    def getData(self):
        return self.value

    def getNext(self):
        return self.pointer

    def setData(self, newdata):
        self.value = newdata

    def setNext(self, newpointer):
        self.pointer = newpointer

if __name__ == "__main__":
    L = Node("a", Node("b", Node("c", Node("d"))))

    print(L.getData(),L.getNext().getData(),L.getNext().getNext().getData(),L.getNext().getNext().getNext().getData())