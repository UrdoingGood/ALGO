import sys
sys.stdin = open('input.txt', 'r')

# 입력을 처리하고 게임판에서 사이클을 탐색하는 알고리즘을 작성합니다.

# 방향 벡터 설정 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, start_x, start_y, color, count):
    # 현재 점을 방문했다고 표시
    visited[x][y] = True

    # 4방향으로 탐색 (상, 하, 좌, 우)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 게임판 범위를 벗어나지 않도록 체크
        if 0 <= nx < N and 0 <= ny < M:
            # 같은 색의 점일 경우에만 탐색
            if board[nx][ny] == color:
                # 아직 방문하지 않은 점이라면 DFS 탐색을 계속
                if not visited[nx][ny]:
                    if dfs(nx, ny, start_x, start_y, color, count + 1):
                        return True
                # 이미 방문한 점인데, 시작점으로 돌아왔고, 탐색 길이가 4 이상이라면 사이클 발견
                elif (nx, ny) != (start_x, start_y) and count >= 4:
                    return True
    return False


# 입력 받기
N, M = map(int, input().split())  # N은 행, M은 열
board = [list(input().strip()) for _ in range(N)]  # 게임판 상태 입력
visited = [[False] * M for _ in range(N)]  # 방문 여부 체크

# 게임판을 순회하며 DFS로 사이클을 탐색
for i in range(N):
    for j in range(M):
        if not visited[i][j]:  # 아직 방문하지 않은 점에 대해
            # 해당 점에서 사이클을 찾기 시작
            if dfs(i, j, i, j, board[i][j], 1):
                print("Yes")
                exit()  # 사이클을 찾으면 바로 종료

# 끝까지 탐색했는데 사이클이 없다면 "No" 출력
print("No")
