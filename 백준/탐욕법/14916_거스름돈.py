import sys

def 거스름돈():
    n = int(input())

    if n==1 or n ==3:
        answer = -1
    else:
        answer = n // 5
        n %= 5
        print(n)
        if n == 1 or n == 4 :
            answer += 2
        elif n == 2 :
            answer += 1
        elif n == 3 :
            answer += 3

    print(answer)


if __name__ == "__main__":
    거스름돈()