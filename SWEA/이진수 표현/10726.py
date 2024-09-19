import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split(' ')))
    for _ in range(N):
        if M % 2 == 0:
            res = 'OFF'
            break
        else:
            res = 'ON'
        M //= 2

    print(f"#{test_case} {res}")