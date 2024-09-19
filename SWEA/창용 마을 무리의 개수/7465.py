import sys
sys.stdin = open("input.txt", "r")

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union_set(x, y):
    px = find_set(x)
    py = find_set(y)

    if px > py:
        p[py] = px
    else:
        p[px] = py

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    p = [i for i in range(N+1)]

    for i in range(M):
        union_set(arr[i][0], arr[i][1])

    p_count = set()
    for i in range(1, N+1):
        parent = find_set(i)
        p_count.add(parent)

    print(f"#{test_case} {len(p_count)}")