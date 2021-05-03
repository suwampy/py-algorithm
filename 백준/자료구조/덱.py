from collections import deque
import sys

def dequeue():
    N = int(sys.stdin.readline())
    dequeue = deque([])
    for i in range(N):
        cmd = sys.stdin.readline().split()

        if cmd[0]=='push_front':
            dequeue.appendleft(int(cmd[1]))
        elif cmd[0]=='push_back':
            dequeue.append(int(cmd[1]))
        elif cmd[0] == 'pop_front':
            if not dequeue:
                print('-1')
            else:
                print(dequeue.popleft())
        elif cmd[0] == 'pop_back':
            if not dequeue:
                print('-1')
            else:
                print(dequeue.pop())
        elif cmd[0] == 'size':
            print(len(dequeue))
        elif cmd[0] == 'empty':
            if not dequeue:
                print(1)
            else:
                print(0)
        elif cmd[0]=='front':
            if not dequeue:
                print(-1)
            else:
                print(dequeue[0])
        elif cmd[0]=='back':
            if not dequeue:
                print(-1)
            else:
                print(dequeue[len(dequeue)-1])

if __name__ == "__main__":
    dequeue()