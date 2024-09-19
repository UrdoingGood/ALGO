import sys
sys.stdin = open('input.txt')
from collections import deque

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
T = int(input())
for tc in range(1, T + 1):
    # 지도 행과 열의 크기
    N, M = map(int, input().split())
    # 지도 ( W: 물, L: 땅)
    # strip() 은 좌우공백 제거, 없으면 안돌아갈걸요 ?
    grid = [input().strip() for _ in range(N)]
    result = 0
    visited = [[-99] * M for _ in range(N)]

    queue = deque()
    # 모든 물('W') 위치를 큐에 추가 ( 물-물 거리는 0으로 초기화)
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'W':
                queue.append((i, j))
                visited[i][j] = 0

    # BFS
    # 물의 위치를 모두 큐에 넣고
    # 물 근처에 있는 땅을 모두 체크해준다.
    # 처음 큐에는 물만 들어있기 때문에, 물 근처(거리가 1만큼 가까운) 땅의 물에 접근하는 데 걸리는 시간을 갱신한다.
    # 이 후에 물 근처에서 거리가 갱신된 땅들의 근처 땅들의 거리를 갱신한다. ( 기존 땅까지의 거리 + 1)
    # (이미 거리가 갱신된 적 있는 땅은 갱신 X => 다른 땅에 의해서 최소거리가 갱신됐으니까 => BFS 접근 )
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy
            # 범위 벗어난 경우
            if 0 > nx or nx >= N or 0 > ny or ny >= M: continue
            # 이미 갱신된 적 있는 땅이라면 ( 다른 인접 땅이나 물에 의해서 이미 거리가 갱신됨)
            if visited[nx][ny] != -99: continue

            # 이전 땅을 기준으로 +1 만큼의 거리로 저장
            # ( 물이라면 0으로 시작하기 때문에 바로 옆은 1)
            visited[nx][ny] = visited[cx][cy] + 1
            queue.append((nx, ny))

    # 모든 요소들의 값을 합한다.
    for i in range(N):
        for j in range(M):
            result += visited[i][j]

    print(f"#{tc} {result}")