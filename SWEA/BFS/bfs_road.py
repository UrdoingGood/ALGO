# 전체 공간을 복사해서 각 공간의 좌표마다 시작 지점에서 얼마나 이동했는지를 저장하는 방식으로 구현
# 장점 : 모든 목적지의 최단거리를 알 수 있음
# 단점 : 메모리를 2배로 차지한다.
from collections import deque


def get_road_move_time(road, n, m):
    # 4 방향 탐색
    # 하, 우, 상, 좌
    # dxy를 for loop로 돌면서 현재 좌표에 dx, dy를 더해주면, 상하좌우로 이동할 수 있음
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # BFS는 큐로 구현 => deque
    # 문제에서는 [1,1] => [n,m]
    # 입력값을 [0,0] => [n-1,m-1]
    queue = deque([(0, 0)])

    # 복사하고, 각 좌표까지 걸리는 최단 이동거리를 저장해야 함
    # 노드가 한 번 방문한 적이 있는지 확인하는 용도로도 사용
    # 해당 좌표까지의 이동거리
    distance = [['-'] * m for _ in range(n)]
    distance[0][0] = 0 # 문제에서, 처음 시작 부분은 0으로 하기로 함
    while queue: # 큐가 빌 때까지 원소를 꺼내고 방문하는 행위를 반복
        x, y = queue.popleft()

        for dx, dy in dxy: # dxy = [[1,0], [0,1], [-1,0], [0,-1]]
            nx, ny = x + dx, y + dy # 현재 위치에서 각 방향으로 이동

            # [nx, ny]가 갈 수 있는 곳인지를 체크해야함
            # 1. 도로 범위 안에 포함될 것
            # 2. 방문한 적이 없을 것 (내가 갈 곳이 '-'이어야 함)
            # 3. 갈 수 있는 곳일 것 (길이어야 한다. 1이어야 함)
            if 0 <= nx < n and 0 <= ny < m and distance[nx][ny] == '-' and road[nx][ny] == 1:
                # 위 조건을 다 만족했으므로, 이동할 수 있는 좌표
                queue.append((nx, ny))
                # 현재 위치까지 오는 데 걸린 이동 횟수 + 1 값을, 다음에 이동해야할 좌표에 넣는다
                distance[nx][ny] = distance[x][y] + 1

                if nx == n-1 and ny == m-1: # 목적지에 도착했다면
                    return distance[nx][ny]

    # while문을 빠져 나왔다는 것은, 결국 목적지에 도착하지 못했다는 뜻!
    # 목적지를 찾지 못하면 어떤 것을 출력하라고 문제에서 제시할 것임. 그걸로 써주면 됨!
    return '-'


n, m = map(int, input().split()) # 도로의 크기 n * m 입력 받기
road = [list(map(int, input().split())) for _ in range(n)]

# BFS를 이용해서 이동시간 구하기
result = get_road_move_time(road, n, m)
print(result)