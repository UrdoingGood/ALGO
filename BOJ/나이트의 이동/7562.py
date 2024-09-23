import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

dxy = [(-2,-1), (-1,-2), (-2,1), (-1,2), (1,-2), (2,-1), (2,1), (1,2)]
def bfs(x, y, cnt):
    global visited
    global count
    queue = deque()
    queue.append((x, y, cnt))
    visited[x][y] = True
    while queue:
        cx, cy, count = queue.popleft()
        if (cx, cy) == (ex, ey): # 이동하려는 칸에 도달하면 끝
            return count
        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
                # 레벨 단위로 계산하기 때문에 count도 함께 넘겨주기!
                # 처음에는 count += 1을 따로 작성해버렸음.
                queue.append((nx, ny, count + 1))
                visited[nx][ny] = True
    return count

T = int(input())
for test_case in range(T):
    N = int(input())
    visited = [[False] * N for _ in range(N)]
    count = 0
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    print(bfs(sx, sy, count))