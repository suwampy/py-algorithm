
## 2. 문자열
## join() : A.join(B) 는 리스트 B에 있는 모든 문자열을 하나의 단일 문자열 A로 결합한다/
slayer = ["버피", "앤", "아스틴"]
def string():
    print(" ".join(slayer)) ## 버피 앤 아스틴
    print("-<>-".join(slayer)) ## 버피-<>-앤-<>-아스틴
    print("".join(slayer)) ## 버피앤아스틴

## ljust(), rjust()
## A.ljust(width, fillchar) 는 문자열 A '맨 처음'부터 문자열을 포함한 길이 width만큼 문자 filchar를 채운다
## A.rjust(width, filchar)는 문자열 A'맨 끝' 부터 문자열을 포함한 길이 width만큼 문자 fillchar를 채운다
name ="스칼렛"
def just():
    print(name.ljust(50,'-')) ## 스칼렛------------------------
    print(name.rjust(50,'-')) ## ------------------------스칼렛


## format()
## A.format() 은 문자열 A에 변수를 추가하거나 형식화하는데 사용된다
def fm():
    print("{0} {1}".format("안녕", "파이썬!")) ## 안녕, 파이썬!

## split()
## A.split(t, n) 은 문자열 A에서 문자열 t를 기준으로 정수 n번만큼 분리한 문자열 리스트를 반환한다.
## n을 지정하지 않으면 대상 문자열을 t로 최대한 분리한다
def sp():
    slayers = "버피*크리스-메리*16"
    fields = slayers.split("*")
    print(fields) ## ['버피', '크리스-메리', '16']

## strip()
## A.strip(B) 는 문자열 A 앞뒤의 문자열 B를 제거한다.
## 인수 B가 없으면 공백 문자를 제거한다.
def strips():
    slayers = "로미오 & 줄리엣999"
    print(slayers.strip("999")) ## 로미오 & 줄리엣

## index(), find()
## A.index(sub, start, end) : 문자열 A에서 부분 문자열 sub의 인덱스 위치를 반환
## 실패하면 Value Error 예외를 일으킴
## A.find(sub, start, end) : 문자열 A에서 부분 문자열 sub의 인덱스 위치를 반환
## 실패하면 -1를 반환
## 인덱스 start와 end는 문자열 범위이며, 생략할 경우 전체 문자열에서 부분 문자열 sub를 찾음
def indexfind():
    slayers = "Buffy and Faith"
    print(slayers.find("y")) ## 4
    print(slayers.find("k")) ## -1
    print(slayers.index("k")) ##에러!!
    print(slayers.index("y")) ## 4

## count()
## A.count(sub, start, end)는 문자열 A에서 인덱스 start, end 범위 내의
## 부분 문자열 sub가 나온 횟수를 반환
def counts():
    slayer="Buffy is Buffy is Buffy"
    print(slayer.count("Buffy",0,-1)) ## 2
    print(slayer.count("Buffy")) ## 3

## replace()
## A.replace(old, new, maxreplace)는 문자열 A에서 문자열 old를 대체 문자열 new로
## maxreplace로만큼 변경한 문자열의 복사본을 반환한다.
## maxreplace를 지정하지 않으면 모든 old를 new로 변경한다.
def replaces():
    slayer = "Buffy is Buffy is Buffy"
    print(slayer.replace("Buffy","who",2)) ## who is who is Buffy


if __name__ == "__main__":
    replaces()