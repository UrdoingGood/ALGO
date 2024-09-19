"""
DP라는 생각을 먼저 해야 함
부분을 구해서 결과를 도출하기 때문

해당 타일(2*1 2*2 2*3)을 포함하냐 안하냐?
"""

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    dp = [0] * (N + 1) # 1부터 하니까 N+1 만큼

    dp[1] = 1
    dp[2] = 3
    dp[3] = 6

    # dp 배열 채우기
    for i in range(4, N + 1):
        dp[i] = dp[i - 1] + 2 * dp[i - 2] + dp[i - 3] # 점화식

    print(f"#{test_case} {dp[N]}")