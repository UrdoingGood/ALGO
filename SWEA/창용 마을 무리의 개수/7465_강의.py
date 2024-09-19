import sys
sys.stdin = open("input.txt", "r")
from collections import deque

def f(i, N): # i번 사람부터 무리를 탐색하는 함수
    visited[i] = 1
    for j in arr[i]: # i와 아는 관계인 j가 속한 무리가 없으면
        if visited[j] == 0:
            f(j, N)

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N+1)] # 알고 있는 관계를 표시하는 인접리스트
    for _ in range(M):
        a, b = map(int, input().split())
        arr[a].append(b) # a, b 아는사이, 같은 관계는 반복해서 주어지지 않는다.
        arr[b].append(a) # b, a가 양방향인가?

    cnt = 0
    visited = [0] * (N+1) # 관계가 확인된 사람
    for i in range(1, N+1):
        if visited[i] == 0: # 아직 확인 전 이면(무리에 속하지 않은 사람이면)
            cnt += 1 # 새로운 무리 추가
            f(i, N)

    print(f"#{test_case} {cnt}")