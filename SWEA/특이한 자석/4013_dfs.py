# DFS

import sys
sys.stdin = open("input.txt", "r")

from collections import deque

def dfs(mag, rot, visited):
    # 맨 오르쪽이 아닌 경우에는, 무조건 오르쪽과 비교함
    if mag!= N - 1:
        if magnet_list[mag][RIGHT_POS]!= magnet_list[mag + 1][LEFT_POS]:
            if not visited[mag + 1]:
                visited[mag] = True
                dfs(mag + 1, rot * (-1), visited)

    # 맨 왼쪽이 아닌 경우에는, 무조건 오르쪽과 비교함
    if mag != 0:
        if magnet_list[mag][LEFT_POS] != magnet_list[mag - 1][RIGHT_POS]:
            if not visited[mag - 1]:
                visited[mag] = True
                dfs(mag - 1, rot * (-1), visited)

    # dfs 끝까지 오면 여기가 실행되고, 이때 모든 자석을 탐방하면서 빠져나오면서 회전 시키는 것임
    # 빠져나오면서 회전하므로, 다른 자석에 영향을 주지 않음
    if rot == 1:
        magnet_list[mag].rotate(1)
    else:
        magnet_list[mag].rotate(-1)

T = int(input())
for test_case in range(1, T + 1):
    K = int(input()) # 회전 수
    N = 4 # 자석의 개수를 변수로 활용
    RIGHT_POS, LEFT_POS, ARROW_POS = 2, 6, 0
    magnet_list = [deque(list(map(int, input().split()))) for _ in range(N)]
    rotate_info_list = [list(map(int, input().split())) for _ in range(K)]
    score_sum = 0  # 획득한 점수의 총 합을 저장할 변수

    for rotate_info in rotate_info_list:
        magnet_num, rotate_dir = rotate_info
        visited = [False] * N

        # DFS 파라미터
        # 1. 재귀호출을 끝내기 위한 파라미터
        # => 완전 탐색에 가까움 => 탐색할 곳이 업승ㄹ 때 끝남
        # => 현재 자석과 방향, 방문 여부를 넘겨야 함
        # 얻어내려는 결과값 => 이 결과값도 없죠? 우리가 누적하는 건 없다
        dfs(magnet_num - 1, rotate_dir, visited)

    for idx, magnet in enumerate(magnet_list):
        # S극이 아닌 경우
        if not magnet[ARROW_POS]:
            continue

        # S극인 경우
        score_sum += (2 ** idx)

    print(f"#{test_case} {score_sum}")