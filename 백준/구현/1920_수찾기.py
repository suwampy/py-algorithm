def 수찾기():
    n = int(input())
    numbers = set(map(int,input().split()))

    m = int(input)
    numbers_2 = list(map(int,input().split()))

    for i in numbers_2:
        if i not in numbers:
            print('0')
        else:
            print('1')

if __name__ == "__main__":
    수찾기()