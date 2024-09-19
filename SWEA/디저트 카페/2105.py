import sys
sys.stdin = open("input.txt", "r")


def dfs(stores, cx, cy, start_x, start_y, count, chk_num, direction):
    dxy = [(1,1), (1,-1), (-1,-1), (-1,1)] # 상우, 하우, 하좌, 상좌 => 시계방향 사각형으로 돌도록 함
    global max_count

    # 현재 방향(direction)부터 탐색하도록
    # 한번 수행했던 방향은 탐색하지 않게 됨
    for i in range(direction, 4):
        nx, ny = cx + dxy[i][0], cy + dxy[i][1]

        # 범위 넘어가면 다음 방향으로 틀도록
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue

        # 처음 위치로 돌아오면 종료
        # 사각형이 되려면 최소 4방향을 돌아야 함
        if (nx, ny) == (start_x, start_y) and count >= 3:
            max_count = max(max_count, count + 1) # 디저트 개수 갱신
            return

        # 아직 방문하지 않았으면 갈 수 있음
        if stores[nx][ny] not in chk_num:
            chk_num.add(stores[nx][ny]) # 방문한 가게의 디저트 숫자 담기
            dfs(stores, nx, ny, start_x, start_y, count + 1, chk_num, i)
            chk_num.remove(stores[nx][ny]) # 방문 복구


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)] # N*N 크기 디저트 카페

    max_count = -1 # 디저트 최대 종류 수, 만들 수 없으면 -1이므로

    for i in range(N):
        for j in range(N):
            dfs(arr, i, j, i, j, 0, set([arr[i][j]]), 0)

    print(f"#{test_case} {max_count}")