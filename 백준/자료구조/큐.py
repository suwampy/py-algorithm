##https://www.acmicpc.net/problem/18258
import sys

## 큐:선입선출
## 롤러코스터 타는 것을 기다리는 사람들의 줄~
def queue() :
    ## input 대신 sys.stdin.readline() 으로 !!
    N = int(sys.stdin.readline())
    queue = list()

    for i in range(N):
        cmd = sys.stdin.readline().split()

        if cmd[0] == "push":
            queue.append(int(cmd[1]))

        elif cmd[0] == "pop":
            if not queue:
                print('-1')
            else:
                print(queue[0])
                queue.pop(0)

        elif cmd[0] == "size":
            print(len(queue))

        elif cmd[0] == "empty":
            if not queue:
                print(1)
            else:
                print(0)

        elif cmd[0] == "front":
            if not queue:
                print(-1)
            else:
                print(queue[0])

        elif cmd[0] == "back":
            if not queue:
                print(-1)
            else:
                print(queue[-1])



if __name__ == "__main__":
    queue()