import sys
from collections import deque
sys.stdin = open("input.txt", "r")

# 1. 종료 조건을 위한 파라미터 => 위치 정보
# 2. 누적되는 결과값 파라미터 => 딱히 필요 없을 듯
def dfs(x, y):
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * MAZE_SIZE for _ in range(MAZE_SIZE)]

    global result

    if (x, y) == END_POS:
        result = 1
        return

    if result == 1:
        return

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if 0 > nx or nx >= MAZE_SIZE or 0 > ny or ny >= MAZE_SIZE:  # 배열 크기를 넘어가면 안 됨
            continue
        if visited[nx][ny]:  # 방문 했으면 가면 안 됨
            continue
        if dfs[nx][ny] == 1:  # 1이면 벽이라서 안 됨
            continue

        visited[nx][ny] = True
        dfs(nx, ny)

    return


T = 10
for test_case in range(T):
    MAZE_SIZE = 16
    START_POS = (1, 1)
    END_POS = (13, 13)
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(MAZE_SIZE)]
    result = 0
    dfs(*(START_POS))

    print(f"#{tc} {result}")