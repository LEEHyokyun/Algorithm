#피보나치수열
#DP의 가장 대표적인 예시
result = [0] * 100

def dp(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        result[n] = dp(n-1) + dp(n-2)
    return result[n]

print(dp(30))