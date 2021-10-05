from collections import deque


def solution(priorities, location):

    deq = deque([(p, i) for (i, p) in enumerate(priorities)])  # 인덱스 묶어줌
    answer = 0  # 인쇄가 완료된 문서 개수

    while deq:
        target = deq.popleft()  # 맨앞에 있는 요소 빼내기

        if deq and max(deq)[0] > target[0]:  # 뒤에 최고우선순위가 있다면
            deq.append(target)  # 맨 뒤로보내기

        else:
            answer += 1  # 최고 우선순위라면 문서 인쇄됨
            if target[1] == location:  # 현재 target의 인덱스가 내가 요청한문서 위치(location)라면
                break

    return answer

if __name__ =="__main__":
    print(solution([1],0))