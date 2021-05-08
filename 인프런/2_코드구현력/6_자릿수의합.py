import sys

def 자릿수의합():
    n=int(input())
    a=list(map(int, input().split()))
    def digit_sum(x):
        sum=0
        while x>0:
            sum += x%10
            x=x//10
        return sum

    max = -2147000000
    for x in a:
        tot=digit_sum(x)
        if tot>max:
            max=tot
            res=x
    print(res)



# def 자릿수의합():
#     n = int(sys.stdin.readline())
#     a = list(map(int, input().split()))
#
#     b =[]
#     for i in a:
#         b.append(digit_sum(i))
#
#     max = -2147000000
#
#     for i, x in enumerate(b):
#         if x>max:
#             max=i
#
#     print(a[max])
#
# def digit_sum(x):
#     s =0
#     for i in str(x):
#         s += int(i)
#
#     return s

if __name__ == "__main__":
    자릿수의합()