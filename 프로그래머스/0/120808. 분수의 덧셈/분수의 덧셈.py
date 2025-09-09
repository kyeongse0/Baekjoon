import math
def solution(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2
    numer1 = numer1 * denom2
    numer2 = numer2 * denom1
    numer = numer1 + numer2
    # 약수로 나누는 로직이 필요
    gcd = math.gcd(numer, denom)
    numer = numer /gcd
    denom = denom /gcd
    answer = [numer, denom]
    return answer