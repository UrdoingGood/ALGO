# 탐욕 알고리즘 문제
# 주어진 목록을 한 번 정렬 ->

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    candies = list(map(int, input().split()))
    min_diff = float('inf')

    # 정렬을 해야함
    # 정렬을 하면 어디서 시작하던, 연속적으로 K개를 선택함녀하면 앱 앞은
    candies.sort()
    for i in range(N - K + 1):
        # 맨앞은 최소값, 맨뒤는 최대값이 정렬되므로 이 값만 처리하면 됨
        diff = candies[i + K - 1] - candies[i]
        min_diff = min(min_diff, diff)

    print(f"#{test_case} {min_diff}")
