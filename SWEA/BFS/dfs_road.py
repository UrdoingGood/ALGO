# 미로 같은 문제는 BFS로 푸는 것이 맞음
# DFS는 모든 경로를 탐색해야함 => O(2^(N*M)
# 하지만 미로를 DFS로 풀어야할 때가 있음
# 목적지까지 도달하는 "경로"에서 특정 조건을 구해야 하는 경우

def dfs(x, y, count):
    global min_count

    if x == N - 1 and y == M - 1:
        min_count = min(min_count, count)
        return

    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx < N or ny < 0 or ny >= M:
            continue
        if visited[nx][ny]:
            continue
        if not road[nx][ny]:
            continue

        visited[nx][ny] = True
        dfs(nx, ny, count + 1)
        # 깊이 끝까지 방문한다음, 다시 원래 포지션으로 돌려놓아야 함
        # False로 초기화해주지 않는다면, 이전으로 되돌아 갈 때, 방문하지 않았던 방향으로만 탐색해서 가게 됨
        visited[nx][ny] = False

N, M = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(n)]

# 방문 여부를 확인하기 위한 변수
visited = [[False] * M for _ in range(N)]

# 최소 이동 횟수를 저장하기 위한 변수
min_count = float('inf') # min_count = N * M 도 상관없음
visited[0][0] = True

# dfs 파라미터 무엇으로?
# 1. 종료 조건이 될 수 있는 변수 : 이동 좌표 => 목적지에 도달하면 DFS 중단
# 2. 우리가 얻으려는 누적값 : 이동 거리
dfs(0, 0, 0)