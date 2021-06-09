def solution(numbers):
  answer = ''
  
  numbers = list(map(str,numbers))
  # numbers 원소는 0 이상 1000 이하이므로
  numbers.sort(key = lambda x : x*3, reverse=True)

  answer = str(int(''.join(numbers)))
  return answer

if __name__ == "__main__":
  #numbers = [6,10,2]
  numbers = [3,30,34,5,9]
  print(solution(numbers))