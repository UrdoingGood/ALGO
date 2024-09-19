from collections import deque


def find_island(island, x, y):
    # 상하좌우 + 대각선
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    queue = deque([(x, y)])
    island[x][y] = 0 # 방문 했으므로, 0(바다) 바꾸기

    while queue:
        cx, cy = queue.popleft()

        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 범위 벗어난 경우
                continue

            if island[nx][ny] == 0: # 바다인 경우
                continue

            queue.append((nx, ny))
            island[nx][ny] = 0 # 방문했으므로 0으로 바꿔주기


n, m = map(int, input().split()) # 섬의 크기 입력
arr = [list(map(int, input().split())) for _ in range(n)] # 섬의 상태 입력 받기
island_cnt = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1: # 1이 땅이므로, 땅이면 BFS 실행
            find_island(arr, i, j)
            island_cnt += 1
