import sys
# 전위표기법 : 연산자가 피연산자 앞에 나오는 방식
# 1 + 2 * 3 + 1 + 2 / 2
# ((1+(2*3))+(1+(2/2)))
# +((+1*(23))(+1(/(22)))
# ++1*23+1/22

# 후위표기법 : 연산자가 뒤에 오는 수식
# 1 + 2 * 3 + 4 + 2 / 2
# ((1+(2*3))+(4+(2/2)))
# ((1(23)*)+((42)+2)/))+
# 123*+42+2/+


def 후위표기식():
   n = int(sys.stdin.readline())
   s = sys.stdin.readline().rstrip()
   num =[]

   for i in range(0,n):
       num.append(int(sys.stdin.readline()))

   res=[]

   for x in s:
       if x in "+-*/":
           a = res.pop()
           b = res.pop()
           if x == '+':
               res.append(b+a)
           elif x=='-':
               res.append(b-a)
           elif x== '*':
               res.append(b*a)
           elif x == '/':
               res.append(b/a)
       else:
           ## 문자열일떄
           res.append(num[ord(x)-ord('A')])
   print('%.2f' % (res[0]))



if __name__=="__main__":
    후위표기식()