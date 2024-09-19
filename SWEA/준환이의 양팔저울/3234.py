import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    weight = list(map(int, input().split()))


    print(f"{test_case} {res}")