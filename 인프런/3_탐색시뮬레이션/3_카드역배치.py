import sys

def 카드역배치():
    print()
    a=list(range(21)) #0부터 20까지 리스트 생략
    # _ : 변수 없이 반복
    for _ in range(10):
        s,e = map(int, input().split())
        for i in range((e-s+1)//2):
            a[s+i],a[e-i]=a[e-i],a[s+i]

    #제일 앞에거 빼기
    a.pop(0)

    for x in a:
        print(x,end=' ')

if __name__ =="__main__":
    카드역배치()