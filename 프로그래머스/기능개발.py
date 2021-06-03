from collections import deque

# 처음에 이렇게품..
# 시간초과 ^^
def solution1(progresses, speeds):
    answer = []

    l = []
    
    for i in range(len(progresses)):
      t1 = 100 - progresses[i]
      l.append(t1 // speeds[i])
    
    stack = []
    for i in range(len(l)) :
      if i == 0 :
        stack.append(1)
      elif l[i]<= l[i-1]:
        stack[-1] = stack[-1]+1
      else:
        stack.append(1)

    print(stack)

    return answer

def solution2(progresses, speeds):
  answer =[]
  time = 0
  count = 0

  while len(progresses) > 0:
    if (progresses[0] + time * speeds[0]) >= 100:
      progresses.pop(0)
      speeds.pop(0)
      count +=1 
    else :
      if count >0 :
        answer.append(count)
        count = 0
      time += 1
  
  print(count)

  answer.append(count)

  return answer

if __name__ == "__main__" :
  progresses = [95, 90, 99, 99, 80, 99] # 배포되어야 하는 순서대로 작업의 진도가 적힌 정수배열
  speeds = [1, 1, 1, 1, 1, 1] # 각 작업의 개발 속도가 적힌 정수 배열
  print(solution2(progresses,speeds))