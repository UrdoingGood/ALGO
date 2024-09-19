import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, p_sum):
    global res
    if n >= N:
        res = max(res, p_sum)
        return res
    if n + T[n] <= N:
        dfs(n+T[n], p_sum+P[n])
    dfs(n+1, p_sum)


N = int(input())
T = [0] * N
P = [0] * N
for i in range(N):
    T[i], P[i] = map(int, input().split())

res = 0
dfs(0, 0)
print(res)