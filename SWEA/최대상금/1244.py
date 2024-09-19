import sys
sys.stdin = open("input.txt", "r")


def dfs(n):
    global ans
    L = len(num_arr)

    # 종료 조건
    if n == int(N):
        ans = max(ans, int(''.join(map(str, num_arr))))
        return

    for i in range(L-1):
        for j in range(i+1, L):
            num_arr[i], num_arr[j] = num_arr[j], num_arr[i] # 교환
            chk = int(''.join(map(str, num_arr)))

            if (n, chk) not in v:
                dfs(n+1)
                v.append((n, chk))

            num_arr[i], num_arr[j] = num_arr[j], num_arr[i] # 원상복구


T = int(input())
for test_case in range(1, T + 1):
    nums, N = input().split()
    num_arr = []
    ans = 0
    v = []

    for num in nums:
        num_arr.append(int(num))

    dfs(0) # 0번째부터 시작
    print(f"#{test_case} {ans}")