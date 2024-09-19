# dfs
# ci,cj: 현재 좌표 / bent: 꺽은 수 / v: 방문 저장 배열
def dfs(ci, cj, bent, v):
    global ans

    if bent == 2:
        if len(v) * 2 < ans:
            return

    if bent == 4:
        return

    # 3에서 리턴되면 x, 3번 꺽고 직진해야 시작 좌표 만남
    if bent == 3:
        # 시작 좌표와 동일한지 확인
        if ci == si and cj == sj:
            # 중복 값 없는지 확인
            if len(v) == len(set(v)):
                ans = max(ans, len(v))

    ni, nj = ci + dij[bent][0], cj + dij[bent][1]

    if 0 <= ni < N and 0 <= nj < N:
        dfs(ni, nj, bent + 1, v + [lst[ci][cj]])  # 방향 꺽음
        dfs(ni, nj, bent, v + [lst[ci][cj]])  # 킵 고잉


# main
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    dij = [(1, 1), (1, -1), (-1, -1), (-1, 1)]  # 대각선 이동 방향 인덱스: 우하, 좌하, 좌상, 우상

    for si in range(N - 2):
        for sj in range(1, N - 1):
            dfs(si, sj, 0, [])

    print(f'#{tc}', ans)
