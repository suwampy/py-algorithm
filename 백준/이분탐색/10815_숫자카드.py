# 이분 탐색으로 풀기
n = int(input())
c1 = list(map(int, input().split()))

m = int(input())
c2 = list(map(int, input().split()))

# 정렬
c1.sort()

# 
for i in range(m):
  lt = 0 # 최소값
  rt = n # 최대값

  while lt <= rt :
    mid = (lt + rt) // 2
    
    if c1[mid] == c2[i]:
      print(1, end=" ")
      break
    elif c1[mid] < c2[i]:
      lt = mid + 1
    else:
      rt = mid -1

    if lt > rt:
      print(0, end =" ")
      break;



# set 써서 풀기
# 상근이가 가지고있는카드
# n = int(input())
# c1 = set(map(int, input().split()))

# # 상근이가 갖고있는지 확인
# m = int(input())
# c2 = list(map(int, input().split()))

# for i in c2:
#   if i in c1:
#     print(1, end=' ')
#   else:
#     print(0, end=' ')
  


