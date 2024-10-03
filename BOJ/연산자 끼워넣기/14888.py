import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, total, add, sub, mul, div):
    global mn, mx

    if n == N:
        mn = min(total, mn)
        mx = max(total, mx)
        return

    if add > 0:
        dfs(n+1, total+A[n], add-1, sub, mul, div)
    if sub > 0:
        dfs(n+1, total-A[n], add, sub-1, mul, div)
    if mul > 0:
        dfs(n+1, total*A[n], add, sub, mul-1, div)
    if div > 0:
        if total < 0:
            dfs(n + 1, -(-total // A[n]), add, sub, mul, div - 1)
        else:
            dfs(n + 1, total // A[n], add, sub, mul, div - 1)

N = int(input())
A = list(map(int, input().split(' ')))
add, sub, mul, div = map(int, input().split(' '))
mn = int(1e9)
mx = int(-1e9)

dfs(1, A[0], add, sub, mul, div)
print(mx)
print(mn)