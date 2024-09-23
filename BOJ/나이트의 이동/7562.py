import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

dxy = [(-2,-1), (-1,-2), (-2,1), (-1,2), (1,-2), (2,-1), (2,1), (1,2)]
def bfs(x, y):
    global visited
    count = 0
    queue = deque()
    queue.append((x, y))
    while queue:
        cx, cy = queue.popleft()
        if (cx, cy) == (ex, ey):
            return count
        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
                count += 1
                queue.append((nx, ny))
                visited[nx][ny] = True
    return count

T = int(input())
for test_case in range(T):
    N = int(input())
    visited = [[False] * N for _ in range(N)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    print(bfs(sx, sy))