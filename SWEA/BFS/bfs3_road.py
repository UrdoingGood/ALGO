# 강사님의 코드 작성 스타일 보자
# early return
# 한 if 문에 하나의 조건만 있으므로 디버깅도 편해서 이런 방식을 선호하신다고 함

from collections import deque


def get_road_move_time(road, n, m):
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = deque([(0, 0)])
    distance = [['-'] * m for _ in range(n)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            # early return
            # 조건 처리를 바로바로 하는 것
            # 안쪽으로 깊게 코드가 파고드는 것을 막을 수 있음

            # 도로 범위를 벗어난 경우
            if 0 > nx or nx >= n or 0 > ny or ny >= m:
                continue

            # 방문한 적이 있는 경우
            if distance[nx][ny] != '-':
                continue

            # 도로가 아닌 경우
            if road[nx][ny] == 0:
                continue

            queue.append((nx, ny))
            distance[nx][ny] = distance[nx][ny] + 1
            if nx == n - 1 and ny == m - 1:
                return distance[nx][ny]

    return '-'


n, m = map(int, input().split()) # 도로의 크기 n * m 입력 받기
road = [list(map(int, input().split())) for _ in range(n)]

# BFS를 이용해서 이동시간 구하기
result = get_road_move_time(road, n, m)
print(result)