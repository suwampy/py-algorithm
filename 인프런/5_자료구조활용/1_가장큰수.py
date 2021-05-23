import sys

# stack
# Last In First Out (선 입 선 출)

def 가장큰수():
    num , m = map(int,input())

    num= list(map(int, str(num))) #string으로 바꿔서 한 개 한 개 접근하게
    stack=[]

    for x in num:
        #앞에자료가 나보다 작으면 지워
        # stack : 스택이 비워져있지 않을 떄
        # m>0 : 뽑아낼게 있을 때
        # stack[-1]<x : 가장나중에넣어진 자료가 x보다 클때
        while stack and m>0 and stack[-1]<x:
            stack.pop() # 스택의 제일 뒷자료 뽑아내기
            m-=1
        #스택넣기
        stack.append(x)

    if m !=0 :
        stack=stack[:-m]

    res =''.join(map(str,stack))

    print(res)

if __name__ == "__main__":
    가장큰수()