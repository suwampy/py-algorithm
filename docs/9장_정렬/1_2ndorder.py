## 2차 정렬
## 1. 버블 정렬
## 인접한 두 항목을 비교하여 정렬하는 방식
## 시간 복잡도는 O(n²)
def bubble_sort(seq):
    print(seq)
    length = len(seq) -1
    for num in range(length, 0, -1):
        print("**** ", num, " 번째 순회 ****")
        for i in range(num):
            ## n번째 항이 n+1번째항보다 클 때
            print(i,"번째 항 : [",seq[i],"]")
            print(i+1,"번째 항 : [",seq[i+1],"]")
            if seq[i] > seq[i+1]:
                print("교환!")
                seq[i], seq[i+1] = seq[i+1], seq[i]
                print("교환끝~")
    return seq

def test_bubble_sort():
    seq = [4,5,2,1,6]
    assert(bubble_sort(seq) == sorted(seq))


## 2. 선택 정렬
# 리스트에서 가장 작거나 큰 항목을 찾아서 첫 번째 항목과 위치를 바꿈
# 그러고 나서 그 다음 항목을 찾아서 두 번째 항목과 위치를 바꿈
# 이런 식으로 리스트 끝에 도달할 떄까지 과정을 반복..
# 리스트가 이미 정렬되어 있어도 시간복잡도는 O(n²)
def selection_sort(seq):
    length = len(seq)
    for i in range(length-1):
        min_j = i
        print("min_j : ",min_j)
        for j in range(i+1, length):
            print("==== 이중 반복문 =====")
            print("min_j : ", min_j)
            print("j : ",j)
            if seq[min_j] > seq[j]:
                min_j = j
            print("==== 이중 반복문 끝=====")
        seq[i], seq[min_j] = seq[min_j], seq[i]
    return seq

def test_selection_sort():
    seq = [11, 3, 28, 43, 9, 4]
    assert(selection_sort(seq) == sorted(seq))

if __name__ == "__main__":
    ##test_bubble_sort()
    test_selection_sort()