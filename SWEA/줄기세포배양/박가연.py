import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

T = int(input())
for test_case in range(1, T+1):
    N, M, K = list(map(int, input().split(' ')))
    arr = [list(map(int, input(' '))) for _ in range(M)]

    dxy = [(1,0), (0, 1), (-1, 0), (0, -1)]

    queue = deque()
    cell_set = {}
    for n in range(N):
        for m in range(M):
            # 만약 이미 죽은 세포이면 넘어감
            if arr[n][m] == 0:
                continue

            # 살아있으면, 큐에 넣어줌 (돌아야하니까)
            # [x좌표, y좌표, 생명력, 살아있는시간]
            queue.append([n, m, arr[n][m], 0])

    # K시간 만큼 분열
    for k in range(K):
        while queue:
            cx, cy, life, time = queue.pop()

            # 아직 비활성화면 다음 시간을 보면 됨
            if time < life:
                queue.append([cx, cy, life, time+1])

            # life만큼 지나면 활성 상태됨 => 분열
            if time == life:
                for dx, dy in dxy:
                    nx, ny = cx+dx, cy+dy

                    # 세포가 이미 존재하는 경우



    # 큐에 남아있는게 살아있는 세포 => len(queue)
    print(f"#{test_case} {len(queue)}")