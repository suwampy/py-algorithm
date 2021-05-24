def 후위표기식만들기():
    a = input()
    stack = []
    res = ''
    for x in a:
        if x.isdecimal(): #숫자인지?
            res+=x #누적
        else:
            if x=='(': #여는괄호
                stack.append(x)
            elif x=='*' or x=='/':
                while stack and (stack[-1]=='*' or stack[-1]=='/'): #곱하기나누기면 연산 우선순위가 같다
                    res+=stack.pop()
                stack.append(x)
            elif x=='+' or x=='-':
                while stack and stack[-1]!='(': # 더하기 빼기가 여는 괄호가 만나면 멈춘다..
                    res+=stack.pop()
                stack.append(x)
            elif x==')':
                while stack and stack[-1]!='(':
                    res+=stack.pop()
                stack.pop()

    # 남아있을떄
    while stack:
        res+=stack.pop()

    print(res)

if __name__ == "__main__":
    후위표기식만들기()