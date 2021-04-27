## https://www.acmicpc.net/problem/1158
def josephus(N,K) :
    # 배열
    arr = list(range(1,N+1))

    answer = []
    num = 0

    for t in range(N):
        num += K-1
        if num>=len(arr):
            print("num : ",num)
            print("len(arr) : ",len(arr))
            num = num % len(arr)
            print("나눔 : ",num)
            print("---------------")
        answer.append(str(arr.pop(num)))


    print("<", ", ".join(answer)[:], ">", sep='')

if __name__ == "__main__":
    josephus(7,3)