## 리스트
# 연결 리스트(linked list) : 여러 분리된 노드가 서로 연결되어 있는 구조
# 자료구조의 내용을 순회하는 데에는 둘 모두 똑같이 효율적이지만
# 어떤 요소에 직접 접근할 때 배열의 시간복잡도는 O(1) 이고
# 연결 리스트는 O(n) 이다. ( 연결 리스트는 어떤 노드에 접근하려면 처음부터 순회를 시작해야 함)
# 또한 연결 리스트에서 어떤 노드를 삽입할 때
# 그 위치를 안다면 연결 리스트 노드 수에 상관 없이 시간복잡도는 O(1) 이다
# 배열에서 어떤 위치에 항복을 삽입하려면
# 그 위치에서부터 모든 항목을 오른쪽으로 옮겨야 하므로
# 시간 복잡도는 O(n) 이다

## 파이썬의 리스트 : 배열과 유사한 객체
# 리스트는 크기를 동적으로 조정할 수 있는 배열
# 리스트는 항목을 쉼표로 구분하고 대괄호 [] 로 감쌈
# 리스트의 항목은 모두 다른 데이터 타입이어도 됨

def listsample():
    q = [2,3]
    p = [1,q,4]
    ## append() : 리스트 끝에서 항목을 추가할 때. 시간복잡도는 O(1)
    p[1].append("버피")
    print(p) # [1,[2,3,"버피"],4]
    print(q) # [2,3,"버피"]
    ## pop() : 리스트 끝에서 항목을 제거할 때. 시간복잡도는 O(1)

    ## 리스트 항목을 검색해야 하는 remove(), index(), 멤버십 테스트 in등의
    ## 시간 복잡도는 O(n)
    ## insert() 메서드 또한 지정한 인덱스에 항목을 삽입한 후
    ## 그 이후의 인덱스 항목들을 한 칸 씩 뒤로 밀어야 하므로
    ## 시간 복잡도는 O(n)

    ## 검색이나 멤버십 테스트 시 빠른 속도가 필요하다면
    ## 셋이나 딕셔너리 같은 컬렉션 타입을 선택하는 것이 적합
    ## 또는 리스트에서 항목을 순서대로 정렬하여 보관하면 빠른 검색을 제공할 수 있음


## 1. 리스트 메서드
## append()
# A.append(x) 는 리스트 A 끝에 항목 x를 추가한다.
## A[len(A):] = [x]
def listMethodAppend():
    people = ["버피", "페이스"]
    people.append("자일스")
    print(people) ## ['버피', '페이스', '자일스']

    people[len(people):] = ["잰더"]
    print(people) ## ['버피', '페이스', '자일스', '잰더']

## extend()
## A.extend(c) 는 반복 가능한 모든 항목 c를 리스트 A에 추가한다
## A[len(A):] = c 또는 A+=c와 동일
def listMethodExtend():
    people = ["버피", "페이스"]
    people.extend("자일스")
    print(people) ## ['버피', '페이스', '자', '일', '스']
    people += "윌로"
    print(people) ## ['버피', '페이스', '자', '일', '스', '윌', '로']

## insert()
## A.insert(i,x)는 리스트 A의 인덱스 위치 i에 항목 x를 삽입한다.
def listMethodInsert():
    people =["버피","페이스"]
    people.insert(1,"잰더")
    print(people) ## ['버피', '잰더', '페이스']

## remove()
## A.remove(x)는 리스트 A의 항목 x를 제거한다.
def listMehotdRemove():
    people = ["버피", "페이스"]
    people.remove("버피")
    print(people) ## ['페이스']

## pop()
## A.pop(x) 는 리스트 A에서 인덱스 x에 있는 항목을 제거하고 그 항목을 반환
def listMethodPop():
    people = ["버피","페이스", "아스틴"]
    print(people.pop(1)) ## '페이스'
    print(people) ## ['버피','아스틴']
    print(people.pop()) ## '아스틴'
    print(people) ## ['버피']

## del
## 리스트 인덱스를 지정하여 특정한 항목을 삭제.
## 그 뿐만 아니라 슬라이스를 사용하여 특정 범위 항목들을 삭제할 수도 있음
def listMethodDel():
    a = [-1, 4, 5, 7, 10]
    del a[0]
    print(a) ## [4,5,7,10]

    del a[2:3]
    print(a) ## [4,5,10]

    del a ## a자체를 삭제

## index()
## A.index(x)는 리스트 A에서 항목 x의 인덱스를 반환
def listMethodIndex():
    people = ["버피", "페이스"]
    people.index("버피") ## 0

## count()
## A.count(x)는 리스트 A에 항목 x가 몇 개 들어 있는지 개수를 반환
def listMethodCount():
    people =["버피","페이스",'버피']
    people.count("버피") ## 2

## sort()
## 리스트 A의 항목을 정렬하여 그 변수 자체에 적용
## A.sort(key, re-verse)에 아무런 인수가 없으면 오름차순으로 정렬하며
## 인수를 지정할 때는 키워드 인수를 사용해야 한다
def listMethodSort():
    people =["잰더", "페이스" , "버피"]
    people.sort()
    print(people) ## ['버피', '페이스', '잰더']

    people.sort(reverse=True)
    print(people) ## ['잰더, '페이스', '버피']

## reserve()


if __name__ == "__main__":
    listsample()
    listMethodAppend()