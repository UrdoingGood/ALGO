import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, sm, add, sub, mul, div):
    global mn, mx

    if n == N:
        mn = min(sm, mn)
        mx = max(sm, mx)
        return

    if sm < int(-1e8) or sm > int(1e8):
        return

    if add > 0:
        dfs(n+1, sm+A[n], add-1, sub, mul, div)
    if sub > 0:
        dfs(n+1, sm-A[n], add, sub-1, mul, div)
    if mul > 0:
        dfs(n+1, sm*A[n], add, sub, mul-1, div)
    if div > 0:
        if sm < 0:
            dfs(n + 1, -(abs(sm)//A[n]), add, sub, mul, div - 1)
        else:
            dfs(n + 1, int(sm//A[n]), add, sub, mul, div - 1)

N = int(input())
A = list(map(int, input().split(' ')))
add, sub, mul, div = map(int, input().split(' '))
mn = int(1e8)
mx = int(-1e8)

dfs(1, 3, add, sub, mul, div)
print(mx)
print(mn)