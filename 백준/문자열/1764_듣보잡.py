# set 을 통해서 풀자
# 집합(set)은 집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형이다.

# 집합 자료형은 다음과 같이 set 키워드를 사용해 만들 수 있다.
# >>> s1 = set([1,2,3])
# >>> s1
# {1, 2, 3}





# 듣도 못함 n
# 보도 못함 m
n , m = map(int, input().split())


# 듣도 못함
l1=set()
for _ in range(n):
  l1.add(input())

# 보도 못함
l2=set()
for _ in range(m):
  l2.add(input())

# sorted(iterable) 함수는 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수이다.
res = sorted(list(l1 & l2))
print(len(res))
for i in res:
  print(i)