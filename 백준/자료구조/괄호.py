## https://www.acmicpc.net/problem/9012
import sys

def vps() :
    ## input 대신 sys.stdin.readline() 으로 !!
    N = int(sys.stdin.readline())
    arr = list()
    sum =0

    for i in range(N+1):
        s = sys.stdin.readline().rstrip()
        sList = list(s)

        for j in sList:
            if j == '(':
                sum += 1
            elif i == ')':
                sum -= 1
            if sum < 0 : # (뒤에)가오지않았을때
                print('NO')
                break
        if sum > 0 :
            print('NO')
        elif sum == 0 :
            print('YES')



if __name__ == "__main__":
    vps()