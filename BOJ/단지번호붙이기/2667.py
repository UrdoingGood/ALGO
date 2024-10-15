import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs(si, sj):
    queue = deque()
    queue.append((si, sj))
    visited[si][sj] = True
    count = 1
    while queue:
        ci, cj = queue.popleft()
        for dx, dy in dxy:
            ni, nj = ci + dx, cj + dy
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == False and arr[ni][nj] == 1:
                queue.append((ni, nj))
                visited[ni][nj] = True
                count += 1
    return count

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
res = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == False:
            res.append(bfs(i, j))

# 오름차순 정렬
res.sort()

print(len(res))
for i in range(len(res)):
    print(res[i])
# print(len(res), *res, sep='\n')