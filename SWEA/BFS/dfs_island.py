def dfs(x, y):
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    island[x][y] = 0

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        # 범위를 벗어난 경우
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        # 방문 못하는 곳 (바다)
        if not island[nx][ny]:
            continue

        # dfs는 끝까지 파고 드는 것이므로, 따로 종료 조건을 넣을 필요 없음
        # 단순하게 다음에 갈 위치인 (nx, ny)를 넣어주면 됨
        dfs(nx, ny)


n, m = map(int, input().split()) # 섬의 크기 입력
island = [list(map(int, input().split())) for _ in range(n)] # 섬의 상태 입력 받기
island_cnt = 0

for i in range(n):
    for j in range(m):
        if island[i][j] == 1: # 방문하려는 곳이 땅이어야 함
            dfs(i, j)
            island_cnt += 1