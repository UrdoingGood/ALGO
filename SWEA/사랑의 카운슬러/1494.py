import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    worm = [list(map(int, input().split())) for _ in range(N)]


    res = 0
    print(f"{test_case} {res}")