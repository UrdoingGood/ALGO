import sys
sys.stdin = open("input.txt", "r")


def find_set(a):
    if p[a] != a:
        p[a] = find_set(p[a])
    return p[a]


def union_set(a, b):
    px = find_set(a)
    py = find_set(b)

    if px == py:
        return False

    if px != py:
        if px > py:
            p[py] = px
        else:
            p[px] = py
        return True


T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(E)]
    p = [i for i in range(V+1)]
    graph.sort(key=lambda g: g[2])
    res = 0

    for x, y, w in graph:
        if union_set(x, y):
            res += w
    print(f"#{test_case} {res}")
