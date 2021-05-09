import sys

# sol1
def 회문문자열검사():
    print()
    n = int(sys.stdin.readline())

    for i in range(0,n):
        s = input()
        # 대소문자를 구별하지않으므로..
        s = s.upper()
        size=len(s)
        for j in range(size//2):
            if s[j]!=s[-1-j]:
                # index 마이너스로 접근
                print("#%d NO" %(i+1))
                break
        else:
            print("#%d YES" %(i+1))

# sol2
def 회문문자열검사2():
    print()
    n = int(sys.stdin.readline())
    for i in range(0,n):
        s = input()
        s = s.upper()
        if s==s[::-1]:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))

if __name__ == "__main__":
    회문문자열검사()