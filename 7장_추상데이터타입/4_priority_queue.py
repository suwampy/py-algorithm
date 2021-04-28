## 우선순위 큐와 힙
# 힙 (heap) : 노드가 하위 노드보다 작은 이진트리
# 균형 트리의 모양이 수정될 때 다시 이를 균형 트리로 만드는 시간복잡도는 O(log n)
# 힙은 리스트에서 가장 작은 요소(또는 가장 큰 요소)에 반복적으로 접근하는 프로그램에 유용
import heapq
def heap():
    list1 = [4,6,8,1]
    # heapq.heapify() = O(n) 시간에 리스트를 힙으로 변환할 수 있음
    heapq.heapify(list1)
    print(list1) #[1,4,8,6]

    # 항목에 힙을 삽입할 땐 heapq.heappush(heap, item)을 사용
    h=[]
    heapq.heappush(h, (1,'food'))
    heapq.heappush(h, (2, 'have fun'))
    heapq.heappush(h, (3, 'work'))
    heapq.heappush(h, (4, 'study'))

    print(h) # [(1,'food'),(2,'have fun'),(3,'work'),(4,'study')]

    # heapq.heappop(heap) 함수는 힙에서 가장 작은 항목을 제거하고 반환
    print(heapq.heappop(list1)) # 1
    print(list1) # [4,6,8]

    # heapq.heappushpop(heap, item)은 새 항목을 힙에 추가한 후 가장 작은 항목을 제거하고 반환

## 최대 힙 구현
class Heapify(object):
    def __init__(self,data=None):
        self.data = data or []
        for i in range(len(data)//2, -1, -1):
            self.__max_heapify__(i)

    def __repr__(self):
        return repr(self.data)

    def parent(self,i):
        if i & 1:
            return i >>1
        else:
            reutrn (i>>1) -1

    def left_child(self,i):
        return (i << 1 ) + 1

    def right_child(self,i):
        return (i << 1) + 2

    def __max_heapify__(self,i):
        largest = i # 현재 노드
        left = self.left_child(i)
        right = self.right_child(i)
        n = len(self.data)

        #왼쪽 자식
        largest = (left < n and self.data[left] > self.data[i]) and left or i

        # 오른쪽 자식
        largest = (right < n and self.data[right] > self.data[largest] and
                   right or largest)

        # 현재 노드가 자식들보다 크다면 Skip, 자식이 크다면 Swap
        if i is not largest:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]

            # print(self.data)
            self.__max_heapify__(largest)

    def extract_max(self):
        print(self.data)
        n = len(self.data)
        max_element = self.data[0]

        # 첫번째 노드에 마지막 노드를 삽입
        self.data[0] = self.data[n-1]
        print(self)

        # 마지막노드 제거
        self.data = self.data[:n-1]
        print(self)
        print("-----------------------")
        self.__max_heapify__(0)
        print(max_element)

        return max_element

    def insert(self, item):
        i = len(self.data)
        self.data.append(item)
        while(i!=0) and item > self.data[self.parent(i)]:
            print(self.data)
            self.data[i] = self.data[self.parent(i)]
            i = self.parent(i)
        self.data[i] = item

def test_heapify():
    l1=[3,2,5,1,7,8,2]
    h = Heapify(l1)
    assert(h.extract_max()==8)

if __name__ == "__main__":
    test_heapify()