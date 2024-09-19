import sys
sys.stdin = open('input.txt', 'r')

def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if px > py:
        parent[py] = px
    else:
        parent[px] = py

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    paper = list(map(int, input().split()))

    parent = list(range(N+1)) # 부모 노드 적어둘 리스트
    group_count = 0

    for n in range(0, len(paper), 2):
        a, b = paper[n], paper[n+1]
        union(a, b)

    for i in range(1, N+1):
        if parent[i] == i:
            group_count += 1

    print(f"#{test_case} {group_count}")
