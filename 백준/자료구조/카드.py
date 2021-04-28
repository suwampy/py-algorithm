##https://www.acmicpc.net/problem/2164
import sys
import collections
def card() :
    ## 시간초과함..... ㅠㅠ씌발
    # N = int(sys.stdin.readline())
    # arr = list(range(1, N+1))
    #
    # while len(arr)!=1:
    #     arr.pop(0)
    #     arr.append(arr.pop(0))
    #
    # print(arr[0])

    ## 디큐써서풀으라함함

    N = int(sys.stdin.readline())
    card_deque = collections.deque([i for i in range(1, N +1)])

    while len(card_deque) != 1:
        card_deque.popleft() # 맨 앞 숫자를 뺀다
        card_deque.rotate(-1) # 맨 앞 숫자를 맨 뒤로 보내고 뺀다.

    print(card_deque[0])
if __name__ == "__main__":
   card()