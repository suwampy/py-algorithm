def 쇠막대기():

    s = list(input())
    stack=[]
    cnt=0

    for i in range(len(s)):
        if s[i]== '(': #여는괄호일때 스택에넣음
            stack.append(s[i])
        else: #닫는괄호일때
            stack.pop() #스택뺌
            if s[i-1]=='(': # 앞에것이 여는괄호일때 () : 레이저발사
                cnt+=len(stack)
            else:
                cnt+=1
    print(cnt)

if __name__ == "__main__":
    쇠막대기()