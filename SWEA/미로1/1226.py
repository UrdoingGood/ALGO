import sys
from collections import deque
sys.stdin = open("input.txt", "r")


def find_maze(maze, x, y):
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * MAZE_SIZE for _ in range(MAZE_SIZE)]
    queue = deque([(x, y)])

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy

            if 0 > nx or nx >= MAZE_SIZE or 0 > ny or ny >= MAZE_SIZE: # 배열 크기를 넘어가면 안 됨
                continue
            if visited[nx][ny]: # 방문 했으면 가면 안 됨
                continue
            if maze[nx][ny] == 1: # 1이면 벽이라서 안 됨
                continue

            queue.append((nx, ny))
            visited[nx][ny] = True
            if maze[nx][ny] == 3: # 도착점
                return 1
    return 0


T = 10
for test_case in range(T):
    MAZE_SIZE = 16
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(MAZE_SIZE)]

    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2: # 출발점
                result = find_maze(arr, i, j)

    print(f"#{tc} {result}")