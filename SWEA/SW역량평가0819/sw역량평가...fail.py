import sys
sys.stdin = open('sample_input.txt', 'r')

def dfs(arr, cx, cy, pre_power, next_power, count):
    dxy = [(1,1)] # 아래로 내려가기
    for dx, dy in dxy:
        nx, ny = cx + dx, cy + dy
        pre_power = count_list[cy].pop()

        # 첫 번째 행이 0인 경우엔 못감
        if arr[0][cy] == 0:
            continue

        # 맨 아래까지 가면 그 행의 하강 끝
        if arr[nx][cy] >= N:
            return arr

        # 범위 내에 있는 경우 계속 진행
        if 0 <= nx < N and 0 <= ny < N:
            # 아래로 이동하는데 0을 만나면 count + 1
            # 다음 1 만나기 전까지 pre_power은 count * 1.9
            if arr[nx][cy] == 0:
                count += 1
            else:
                pre_power += count * 1.9
                if pre_power > next_power:
                    next_power += pre_power
                    pre_power = next_power
                dfs(arr, nx, ny, pre_power, next_power, count)
    return arr


T = 10
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    count_list = {}
    tmp = []
    tmp_count = 0
    for j in range(N):
        for i in range(N):
            if arr[i][j] == 1:
                tmp_count += 1
            else:
                tmp.append(tmp_count)
                tmp_count = 0
        count_list[j] = tmp

    res_arr = dfs(arr, 0, 0, 1, 0, 0)

    # 회전시켜서 dfs 한 번 더 돌리기
    newnew_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            newnew_arr[j-N-1][i] = res_arr[i][j]
    res_arr = dfs(newnew_arr, 0, 0, 1, 0, 0)

    res_bottom = 0
    res_right = 0
    for j in range(N):
        if res_arr[N-1][j] == 1:
            res_bottom += 1

    for i in range(N):
        if res_arr[i][0] == 1:
            res_right += 1

    print(f"#{test_case} {res_bottom} {res_right}")
