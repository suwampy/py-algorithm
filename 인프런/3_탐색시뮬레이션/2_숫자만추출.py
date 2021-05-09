import sys

def 숫자만추출1():
    s=input()
    res=0
    for x in s:
        ## isdecimal = 0~9까지숫자
        ## isdigit = 알파벳이 아닌 모든 숫자 형태
        if x.isdecimal():
            res=res*10+int(x)
    print(res)
    cnt =0
    for i in range(1, res+1):
        if res%i==0:
            cnt+=1
    print(cnt)


def 숫자만추출():
    s = input()
    temp=""
    for i in s:
        if not i>='A' and i<='Z':
            temp+=i

    # 약수의 개수
    temp=int(temp)
    num =0
    for i in range(1,temp+1):

        if temp%i==0:
            num+=1

    print(temp)
    print(num)


if __name__ == "__main__":
    숫자만추출()