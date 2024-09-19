# 기존(bfs_road.py)에서는 큐에, 다음에 방문할 좌표를 집어넣었음
# 이번에는 방문할 좌표 + 여태까지 이동한 횟수를 같이 큐에 넣을 것임
# 이렇게 풀어도 방문 여부를 확인하는 변수는 있어야 함
# 문제에서, 큐에 좌표를 집어넣을 때, 부가 데이터를 넣어달라고 하는 문제들이 있음!
from collections import deque


def get_road_move_time(road, n, m):
    # 아래, 오른쪽, 위, 왼쪽 방향으로 탐색
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 방문 여부만 확인
    visited = [[False] * m for _ in range(n)]

    # 아까는 시작좌표만 넣었는데, 여기서는 현재까지 이동한 거리도 넣어주자
    queue = deque([(0, 0, 0)])

    while queue:
        x, y, dist = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 아까는 좌표만 구했지만, 이번에는 다음 좌표까지의 이동거리도 구해 놓는 것임
            next_dist = dist + 1

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and road[nx][ny] == 1:
                queue.append((nx, ny, next_dist))
                visited[nx][ny] = True
                if nx == n-1 and ny == m-1: # 목적지에 도착했으면
                    return next_dist

    return '-'


n, m = map(int, input().split()) # 도로의 크기 n * m 입력 받기
road = [list(map(int, input().split())) for _ in range(n)]

# BFS를 이용해서 이동시간 구하기
result = get_road_move_time(road, n, m)
print(result)