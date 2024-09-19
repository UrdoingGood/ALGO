# 제한시간 초과... 뭐가 문제지???

import sys
sys.stdin = open("input.txt", "r")


from collections import deque


def bfs():
    global ans
    queue = deque()

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                queue.append((i, j))
                visited[i][j] = 0

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = cx + dx, cy + dy
            if 0 > nx or N <= nx or 0 > ny or M <= ny:
                continue
            if visited[nx][ny] != '-':
                continue
            visited[nx][ny] = visited[cx][cy] + 1
            queue.append((nx, ny))

    for i in range(N):
        for j in range(M):
            ans += visited[i][j]

    return ans


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    ans = 0
    visited = [['-'] * M for _ in range(N)]
    print(f"#{test_case} {bfs()}")