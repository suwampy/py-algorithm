def 문자열():
    n=int(input())
    m=input()

    cnt = 0
    for i in m:
        cnt+=int(i)

    print(cnt)
if __name__ == "__main__":
    문자열()