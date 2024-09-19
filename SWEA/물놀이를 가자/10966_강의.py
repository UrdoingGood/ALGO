import sys
sys.stdin = open('input.txt', 'r')
from collections import deque


def bfs(N, M):
    ans = 0 # 최단 거리의 합
    q = deque()
    visited = [[-1] * M for _ in range(N)]

    for i in range(N): # 출발점(모든 물) 인덱스 인큐
        for j in range(M):
            if arr[i][j] == 'W':
                q.append([i, j]) # 출발점 인큐 표시
                visited[i][j] = 0

    while q:
        i, j = q.popleft() # 인접한 땅을 조사할 격자칸 인덱스 디큐
        for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] != 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
                ans += visited[ni][nj]

    return ans


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    res = bfs(N, M) # 모든 땅에서 물까지의 최단거리
    print(f"#{test_case} {res}")