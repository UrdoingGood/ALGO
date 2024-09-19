# BFS

import sys
sys.stdin = open("input.txt", "r")

from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    K = int(input()) # 회전 수
    N = 4 # 자석의 개수를 변수로 활용
    RIGHT_POS, LEFT_POS, ARROW_POS = 2, 6, 0
    magnet_list = [deque(list(map(int, input().split()))) for _ in range(N)]
    rotate_info_list = [list(map(int, input().split())) for _ in range(K)]
    score_sum = 0  # 획득한 점수의 총 합을 저장할 변수

    # 주어진 회전 정보를 순회한다.
    # 주어진 회전 정보를 queue에 삽입하고, queue에서 꺼낸 후에,
    # 꺼낸 자석에 인접한 자석을 다시 queue에 넣는다.
    # 이때, visited를 활용해서 방문 여부 확인

    for rotate_info in rotate_info_list:
        magnet_num, rotate_dir = rotate_info
        # 회전을 진행하기 위해 queue에 자석의 인덱스와 방향을 삽입
        queue = deque([magnet_num, rotate_dir])
        visited = [False] * N
        visited[magnet_num - 1] = True

        while queue:
            mag_idx, rotate = queue.popleft() # 인덱스와 방향

            # 가장 오른쪽 자석이 아니라면, 항상 오른쪽과 비교해야 함
            if mag_idx != N -1:
                if magnet_list[mag_idx][RIGHT_POS]!= magnet_list[mag_idx + 1][LEFT_POS]:
                    if not visited[mag_idx + 1]:
                        queue.append([mag_idx + 1, -rotate])
                        visited[mag_idx + 1] = True

            # 가장 왼쪽 자석이 아니라면, 항상 왼쪽과 비교해야 함
            if mag_idx != 0:
                if magnet_list[mag_idx][LEFT_POS]!= magnet_list[mag_idx - 1][RIGHT_POS]:
                    if not visited[mag_idx - 1]:
                        queue.append([mag_idx - 1, -rotate])
                        visited[mag_idx - 1] = True

            # 이미 본인은 할 일을 끝낸 상태임
            # 재귀도 아니고, 양 옆의 자석을 큐에 집어넣었고
            # visited == True라서 다시 방문할 일도 없기 때문
            if rotate == 1:
                magnet_list[mag_idx].rotate(1)
            else:
                magnet_list[mag_idx].rotate(-1)

    for idx, magnet in enumerate(magnet_list):
        # S극이 아닌 경우
        if not magnet[ARROW_POS]:
            continue

        # S극인 경우
        score_sum += (2 ** idx)

    print(f"#{test_case} {score_sum}")