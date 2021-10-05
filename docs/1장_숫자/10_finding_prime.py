import math
import random

## 소수
## 소수 : 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수
## 약수로 1과 자기 자신만을 가지는 수

## 무차별 대입법
def finding_prime(number):
    ## abs : 절대값
    num = abs(number)
    if num < 4 : return True
    for x in range(2, num):
        if num % x == 0 :
            return False
    return True

## 저곱근
def finding_prime_sqrt(number):
    num = abs(number)
    if num < 4 : return True
    ## sqrt : 제곱근
    for x in range(2, int(math.sqrt(num)) + 1):
        if number % x == 0:
            return False
    return True

## 확률론적 테스트와 페르마의 소정리
def finding_prime_fermat(number):
    if number <= 102:
        for a in range(2,number):
            if pow(a,number-1,number) !=1:
                return False
        return True
    else:
        for i in range(100):
            a = random.randint(2, number - 1)
            if pow(a, number-1 ,number) != 1:
                return False
        return True

def test_finding_prime():
    number1 = 17
    assert(finding_prime(number1) is True)
    assert (finding_prime_sqrt(number1) is True)
    assert (finding_prime_fermat(number1) is True)

if __name__ == "__main__":
    test_finding_prime()