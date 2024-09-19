import sys
sys.stdin = open("input.txt", "r")

from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    dxy = [(1, 0), (0, 1), (0, -1), (-1, 0)]

    queue = deque()
    for n in range(N):
        for m in range(M):
            if arr[n][m] == 0: # 죽은 세포
                continue
            # 살아 있으면
            # 생명력, 위치 x, 위치 y, 살아 있는 시간
            queue.append([arr[n][m], n, m, 0])

    cell_set = set() # 이미 존재하는 좌표 파악
    for k in range(K):
        tmp_queue = [] # 임시로 저장해둘 것
        spread_cell_dict = {} # 분열하는

        while queue:
            life, cx, cy, t = queue.pop()
            cell_set.add((cx, cy)) # 현재 좌표 추가

            # 아직 비활성화 상태
            # 살아있는 시간이 아직 생명력 보다 작은 상황
            if t < life:
                # 일단 임시에 넣어둠
                # 다음 시간 갈 수 있으니까 t+1로 넣어둠
                tmp_queue.append([life, cx, cy, t + 1])
                continue

            # 분열해야 하는 경우
            if t == life:
                for dx, dy in dxy:
                    nx, ny = cx + dx, cy + dy

                    # 분열할 위치에 이미 세포가 존재하면 못감
                    if (nx, ny) in cell_set:
                        continue

                    # 분열 하는데,
                    # 동시에 같은 위치에 분열하려고 하면
                    # 생명력 높은 것으로 함
                    if (nx, ny) not in spread_cell_dict:
                        spread_cell_dict[(nx, ny)] = life
                    else:
                        spread_cell_dict[(nx, ny)] = max(spread_cell_dict[(nx, ny)], life)

            # while문 돌았는데도 아직 안 죽었으면(아직 살아있음)
            if t + 1 < 2 * life:
                tmp_queue.append([life, cx, cy, t + 1])

        # tmp_queue에서 중복 셀 제거 작업 후, 다시 queue에 집어 넣기
        queue = tmp_queue[:]
        for cell_pos, cell_life in spread_cell_dict.items():
            queue.append([cell_life, cell_pos[0], cell_pos[1], 0])

    print(f"#{test_case} {len(queue)}")