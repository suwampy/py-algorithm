## Use Case

### 테스트 케이스 입력

input 보다 더 빠른 속도가 필요할 경우

```python
import sys
sys.stdin.readline().rsplit('\n')
```



### 문자열 처리

1. 대문자 소문자 변환

   ```python
   words = 'a bc'
   words_upper = words.upper()
   words_lower = words.lower()
   ```

2. 중복 문자 제거

   ```python
   words = 'abc abcdef'
   words_abbreviation = ''.join(set(words))
   ```

3. 문자 개수 계산

   ```python
   words = 'aaabbbcde'
   word_count_k = words.count('a')
   ```

4. 리스트 또는 튜플 변환

   ```python
   >>> list('abc')
   ['a','b','c']
   >>> tuple('abc')
   ('a', 'b', 'c')
   ```

5. 역순 출력

   ```python
   def reverse_string1(string):
       return string[::-1]
      
   def reverse_string2(string):
       return reversed(string)
   
   words = input()
   print(''.join(reverse_string1(words)))
   ```

   



## 파이썬 메소드

### isalnum()

문자와 숫자의 문자열을 탐지한다.

```python
s = "helhleo123"
if s.isalnum():
    print("참")
else:
    print("거짓")
### 출력 값
# 참
```



### isalpha()

오직 문자인지 확인한다

```python
s = "helhleo123"
if s.isalpha():
    print("참")
else:
    print("거짓")
### 출력 값
# 거짓
```



### isdigit()

오직 숫자인지 확인한다

```python
s = "124124123"
if s.isdigit():
    print("참")
else:
    print("거짓")
### 출력 값
# 참
```



### islower(), isupper()

islower()은 문자열이 적어도 영숫자 문자 중 하나, 이들 모두를 포함하는 경우 (대소 문자 구분) 문자가 소문자 true, 그렇지 않은 경우는 false를 반환한다.

마찬가지로 isupper()는 문자열이 적어도 영숫자 문자중 하나, 이들 모두를 포함하는 경우 (대소 문자 구분) 문자가 대문자 true, 그렇지 않은 경우는 false를 반환한다.

```python
_str = "THIS is string example....wow!!!"
print(_str.islower())

_str = "this is string example....wow!!!"
print(_str.islower())

_str = "THIS IS STRING EXAMPLE....WOW!!!"
print(_str.isupper())


## 출력 값
# False
# True
# True
```



### isnumeric(), isdigit(), isdecimal()

isnumeric, isdigit() : 유니코드 및 다양한 문자열 안에 숫자가 있으면 True 없으면 False를 출력합니다.

isdecimal() : 문자열의 모든 문자가 10 진수 문자이고 하나 이상의 문자가 있으면 true를, 그렇지 않으면 false를 반환합니다. 10 진수는 10 진수로 숫자를 형성하는 데 사용할 수있는 문자입니다 (예 : U + 0660, 아랍어-인식 디지털 제로. 공식적으로 10 진수 문자는 유니 코드 일반 범주“Nd”의 문자입니다.

```python
s = "3⁸"

print(s.isnumeric()) 
print(s.isdigit()) 
print(s.isdecimal())

## 출력 값
# True
# True
# False
```



### isspace()

isspace()는 문자열이 모드 공백으로 이루어져 있으면 True 아니면 False를 출력한다.

```python
s = "      "
print(s.isspace())

## 출력 값
# True
```



### istitle()

istitle()는 문자열 내의 모든 단어들의 첫글자가 대문자이면 True 아니면 else를 출력합니다.

```python
title = "Hello My Name Is Hyun"
print(title.istitle())
title = "Hello My Name is Hyun"
print(title.istitle())

## 출력 값
# True
# False
```



### ord()

char -> int



### datetime

```python
from datetime import datetime

today = datetime.now()

print('년 : %s' % today.year)
print('월 : %s' % today.month)
print('일 : %s' % today.day)
print('시 : %s' % today.hour)
print('분 : %s' % today.minute)
print('초 : %s' % today.second)

print(today.strftime('%Y/%m/%d %H:%M:%S'))
print(today.strftime('%y-%m-%d %p %H:%M'))
```



### enumerate()

자료형(list, set, tuple, dictionary, string)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴합니다.

```python
a = ['hong','gil','dong']
b = list(enumerate(randomlist))

#[(0, 'hong'), (1, 'gil'), (2, 'dong')]
```



### sum(), min(), max(), eval()

```python
#리스트의 원소 합
result = sum([1,2,3,4,5])

#리스트의 최소값
result = min([1,2,3,4,5])

#리스트의 최대값
result = max([1,2,3,4,5])

#문자열 수식 계산
result = eval("(3+5)*7")
```



### itertools

- permutations

  : r개의 데이터를 뽑아서 **일렬로** 나열하는 모든 경우

- combinations

  : r개의 데이터를 뽑아서 **순서 상관없이** 나열하는 모든 경우

- product

  : r개의 데이터를 뽑아서 **일렬로 나열**하는데 **중복 허용**

- combinations_with_replacement

  : r개의 데이터를 뽑아서 **순서 상관없이** 나열하는데 **중복 허용**

```python
from itertools import permutations, combinations, product, combinations_with_replacement

data = ['A', 'B', 'C']

perm = list(permutations(data, 3))
[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

comb = list(combinations(data, 3))
[('A', 'B', 'C')]

prod = list(product(data, repeat = 2))
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

comb_w = list(combinations_with_replacement(data, 2))
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
```



### bisect

- **정렬된 배열**에서 특정 원소 찾을때

  → O(logN)에 동작

- `bisect_left(a, x)`

  : 정렬된 순서를 유지하면서 리스트 a에 데이터 x 삽입할 가장 왼쪽 인덱스 찾기

- `bisect_right(a, x)`

  : 정렬된 순서를 유지하면서 리스트 a에 데이터 x 삽입할 가장 오른쪽 인덱스 찾기

  → 값이 특정 범위에 속하는 원소의 개수

```python
from bisect import bisect_right, bisect_left

a = [1,2,3,4,4,8]
x = 4

print(bisect_left(a,x))
print(bisect_right(a,x))
```

    if something in arr:
    # something이 배열이 안에 있는가?
    
    if something not in arr:
    # something이 배열안에 없는가?
    
    sth = [(idx, i) for idx, i in enumerate arr]
    # 증가하는 인덱스를 같이 넣은 튜플을 원소로 하는 배열생성
    # 예를 들어 arr=[5,6,8,10] 이면
    # [(0, 5), (1, 6), (2, 8), (3, 10)] 형태의 배열이 만들어짐
    
    sth = max(arr, key=lambda x: x[0])[0]
    # 2차원 배열에서 열의 첫번째 값이 가장 큰 원소를 찾고,
    # 그 값의 1번째 값 리턴
    # 예시 arr = [[1,2,3],[4,5,6],[7,8,9]]
    # sth = max(arr, key=lambda x: x[0])[0]
    # sth = 7
    
    sth = [i for i in range(10)]
    # Comprehension 기법
    # [0,1,2,3,4,5,6,7,8,9]의 배열 생성
    # sth = [0 for i in range(10)]하면
    # [0,0,0,0,0,0,0,0,0,0]의 배열 생성
    
    # BOJ에서 코드 입력받도록 하는 방법
    # 1줄에 여러 숫자
    sth = list(map(int, input().split(' ')))
    
    # Dictionary
    # 모든 키 출력
    print(dic.keys())
    # 모든 값 출력
    print(dic.values())
    # 값이 있으면 리턴 없으면 None 리턴
    dic.get(key)
    
    # 람다
    # 먼저 기본함수
    def add_sth(x):
        return x+10
    # 람다
    add_sth = lambda x: x+10
   	# 사용법
    # 함수 호출과 동일하게
    add_sth(1)
    # 해주면 함수로 호출한 것과 동일한 결과가 나옴
    
    # 람다 표현식 자체 호출
    (lambda x: x+10)(1)
    # 위 식은 아래와 동일
    add_sth = lambda x: x+10
    add_sth(1)
    
    # 주의할 점
    # 람다 표현식 안에서는 변수 생성 불가
    # 변환값 부분은 변수 없이 식 한줄로 보통 표현하고 변수가 필요하면 그냥 def 사용
    
    # 다음 처럼은 가능
    y = 10
    (lambda x: x+y)(1)
    # 위처럼 작성하면 11출력
    
    # Map + Lambda
    def add_sth(x):
        return x+10
    # 다음식을 map에 적용해보고자함
    list(map(add_sth, [1,2,3]))
    # 결과값 [11, 12, 13]
    # map(p1, p2)는 p1에 들어오는 함수에 맞게 p2를 커스터마이징 해서 변경시킴
    
    # Lambda 적용
    list(map(lambda x: x+10, [1,2,3]))
    # 결과값 [11, 12, 13]
    # 위 방식대로 하면 3줄에 끝날게 1줄로 끝남
    
