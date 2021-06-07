import sys

def 포켓몬마스터():
  n , m = map(int, input().split()) # n : 도감에 수록되어있는 포켓몬의 개수 , m : 내가 맞춰야 하는 문제의 개수
  # n개의 줄에 포켓몬 입력
  poketmon = dict()
  bb = dict()
  for i in range(1,n+1):
    ## str(sys.stdin.readline()).strip() 꼭하자...^_^안하면 시간초과남. . . .. ^^
    tmp = str(sys.stdin.readline()).strip()
    poketmon[i] = tmp
    bb[tmp]=i

  for _ in range(m):
    tmp = str(sys.stdin.readline()).strip()
    if tmp.isalpha():
      print(bb.get(tmp))
      # 포켓몬 번호를 말해야함
    else:
      print(poketmon.get(int(tmp)))
      # 포켓몬 번호에 해당하는 문자 출력


if __name__ == "__main__":
  포켓몬마스터()