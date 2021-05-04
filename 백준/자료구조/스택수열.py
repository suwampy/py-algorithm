import sys
def 스택수열():
    n = int(input())
    count = 0
    stack = []
    seq = []
    result = []
    no_message = True

    for i in range(0, n):
        x = int(input())

        while count < x:
            count += 1
            stack.append(count)
            print("+",stack)
            result.append("+")

        if stack[-1] == x:
            seq.append(stack.pop())
            print("-",stack)
            result.append("-")
        else:
            no_message = False
            exit(0)  # a clean exit without any errors / problems

    if no_message == False:
        print("NO")
    else:
        print(seq)
        print("\n".join(result))

if __name__ == "__main__":
    스택수열()
