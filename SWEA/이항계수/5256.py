import sys
sys.stdin = open("input.txt", "r")

def fact(n):
    if (n > 1):
        return n * fact(n-1)
    else:
        return 1

def comb(n, k):
    # 전체를 정렬하는 경우의 수 : fact(n)
    # 두 개를 선택한 경우의 수 : fact(k)
    # 나머지를 정렬하는 경우의 수 : fact(n-k)
    return fact(n) // (fact(k) * fact(n-k))

T = int(input())
for test_case in range(1, T + 1):
    n, a, b = map(int, input().split())
    coefficient = comb(n, a)
    print(f"#{test_case} {coefficient}")