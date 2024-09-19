import sys
sys.stdin = open("input.txt", "r")

# si, sj : 시작 위치
# ei, ej : 끝 위치
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def bfs(si, sj, ei, ej):
    q = []
    v = [[10000]*N for _ in range(N)]

    q.append((si, sj))
    v[si][sj] = arr[si][sj]

    while q:
        ci, cj = q.pop(0)
        for dx, dy in dxy:
            ni, nj = ci+dx, cj+dy
            if 0 <= ni < N and 0 <= nj < N and v[ci][cj] + arr[ni][nj] < v[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + arr[ni][nj]
    return v[ei][ej]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    res = bfs(0, 0, N-1, N-1)

    print(f"#{test_case} {res}")