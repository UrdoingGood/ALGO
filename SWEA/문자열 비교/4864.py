import sys
sys.stdin = open("input.txt", "r")

# 문자열 알고리즘으로 풀어보자
def bruteforce_match(p, t):
    M = len(p)
    N = len(t)

    i = j = 0

    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1

    if j == M:
        return 1
    else:
        return 0

T = int(input())
for test_case in range(1, T + 1):
    match = input()
    chars = input()

    res = bruteforce_match(match, chars)

    print(f"#{test_case} {res}")

'''
T = int(input())
for test_case in range(1, T + 1):
    match = input()
    chars = input()

    if match in chars:
        res = 1
    else:
        res = 0

    print(f"#{test_case} {res}")
'''