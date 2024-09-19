import sys
sys.stdin = open("input.txt", "r")

def dfs(arr, cx, cy, res, chk):
    dxy = [(1,0),(0,1),(-1,0),(0,-1)]
    global max_res
    visited[cx][cy] = True # 방문 체크

    for dx, dy in dxy:
        nx, ny = cx + dx, cy + dy

        # 범위 넘어가는지 확인
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue

        if visited[nx][ny]:
            continue

        # 높이가 더 낮으면 이동
        if arr[cx][cy] > arr[nx][ny]:
            dfs(arr, nx, ny, res+1, chk)

        # 깎고 이동
        # 현재 위치에서 목표 위치로 이동하기 위해, 목표 위치를 최대한 깎은 후에도 여전히 현재 위치가 높아야 한다는 것을 확인해야함 ..
        elif not chk and arr[cx][cy] > arr[nx][ny] - K:
            original_height = arr[nx][ny]
            arr[nx][ny] = arr[cx][cy] - 1
            dfs(arr, nx, ny, res+1, True)
            arr[nx][ny] = original_height # 높이 원상복구하기

    visited[cx][cy] = False
    max_res = max(max_res, res)

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)] # 산
    max_res = 0 # 최대 길이 저장할 변수

    visited = [[False]*N for _ in range(N)] # 방문한 곳 표시

    # 가장 높은 높이 찾기
    max_point = 0
    for i in range(N):
        for j in range(N):
            if mountain[i][j] > max_point:
                max_point = mountain[i][j]

    # 가장 높은 봉우리라면 스타트
    for i in range(N):
        for j in range(N):
            if mountain[i][j] == max_point:
                dfs(mountain, i, j, 1, False)

    print(f'#{test_case} {max_res}')