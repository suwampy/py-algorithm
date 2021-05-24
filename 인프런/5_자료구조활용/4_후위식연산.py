def 후위식연산():
    s = input()
    stack = []

    for x in s:
        if x.isdecimal():
            stack.append(int(x))
        else:
            if x == '+':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1+n2)
            if x == '-':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2-n1)
            if x == '/':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2//n1)
            if x =='+':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1*n2)
    print(stack[0])


if __name__ == "__main__":
    후위식연산()