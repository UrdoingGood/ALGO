import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

dxy = [(1,0), (0,1), (-1,0), (0,-1)]
def bfs():
    count = 0
    queue = deque()

    # 익어 있는 토마토부터 시작
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                queue.append((i, j))

    while queue:
        # 익어 있는 토마토 꺼내서 다음 위치로 이동
        cx, cy = queue.popleft()
        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy

            # 배열 크기 넘지 않도록
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # -1이면 비어 있는 것이므로 넘어가기
            if tomato[nx][ny] == -1:
                continue

            # 0이면 익어야 함
            # 현재 위치에 +1을 해서 며칠 지났는지 표시
            # 다음 위치를 큐에 넣기
            if tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[cx][cy] + 1
                queue.append((nx, ny))

    # 익히는 과정 다 끝낸 후에도 안 익은 것(0)이 있으면 -1 반환
    # 안 익은 것이 없다면, 가장 큰 값(총 걸린 일수)을 반환
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 0:
                return -1
            count = max(count, tomato[i][j])

    # 처음 익었을 때는 0일차이므로, 1을 빼줘야 함
    return count - 1


M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

# 처음부터 토마토가 다 익은 상태라면 0 출력하고 끝내기
tmp_count = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            tmp_count += 1

if tmp_count == N*M:
    print(0)
    exit()

res = bfs()
print(res)