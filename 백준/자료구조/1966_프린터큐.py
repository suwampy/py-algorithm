def 프린터큐():
    test_case = int(input())

    for _ in range(test_case):
        n, m = list(map(int,input().split(' ')))
        queue = list(map(int, input().split(' ')))
        ## 인덱스와 함께 넣어준다
        ## [(2,0), (1,1), (4,2), (3,3)]
        queue = [(i, idx) for idx, i in enumerate(queue)]

        count = 0

        while True:
            ## key=lambda x : x[0] => x[0] 순서대로 정렬
            print("queue", queue)
            print("if", max(queue, key=lambda x: x[0])[0])

            print("")

            '''
                sth = max(arr, key=lambda x: x[0])[0]
                sth = max(arr, key=lambda x: x[0]) : 2차원 배열에서 열의 첫번째 값이 가장 큰 원소를 찾고,
                [0] : 값의 1번째 값 리턴
            '''
            ## 맨앞의 queue가 같다면 젤 큰넘이랑 같다면 ( 우선순위가 제일 큰 놈
            if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
                ## q가 뺴졋다 넣어지니깐....
                count +=1

                ## index가 같다면
                if queue[0][1] == m:
                    print(count)
                    break
                else:
                    queue.pop(0)
            else:
                queue.append(queue.pop(0))

if __name__ == "__main__":
    프린터큐()

