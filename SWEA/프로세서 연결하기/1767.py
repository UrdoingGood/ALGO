# 어떤 core 선택? => 모든 core 다 돌기
# core 선택 하느냐 vs 안 하느냐

# 선택한 core에서 어느 방향으로 전선을 뻗어 갈지(상, 하, 좌, 우)
# 한 방향으로 전선을 설치
# 전선 설치되는 경우는 계속 변경될 값이므로, dfs로 넘겨주기
# dfs 나오면, 설치했던 전선을 다시 회수해야 함!
# 전선/core/벽을 만나면 멈춤

# 프로세서 연결 할 때, 순서는 상관 없다! => 조합
# 무엇을 먼저 고르던, 안 될 조합은 어차피 안되기 때문 (e.g. 전선이 교차되는 경우)

# 종료 조건
# if 내가 선택한 core 개수 > 최대 core
# if core == 최대 core
# 선택했을 때의 길이 < 최대였을 때의 길이

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_wire_len_sum = float('INF') # 연결한 전선의 길이 합 (최소값)
    max_connect_cnt = 0 # 최대로 연결한 프로세서의 개수 (최대값)

    # 모서리에 있는 코어들은 선택할 필요없음. 이미 연결된 것이기 때문
    # 따라서 모서리에 있는 코어들 제외하여, 탐색할 코어만 따로 리스트로 만들어주기
    core_list = []
    for i in range(1, N-1): # 모서리가 아닌 인덱스 1~N-1
        for j in range(1, N-1):
            if arr[i][j]:
                core_list.append((i, j))

    # 재귀 종료할 파라미터
        # 선택해야 하는 core의 인덱스가 core 개수에 도달하면 종료
    # 누적해서 가져가고 싶은 값
        # 선택한 프로세서의 개수(최대 개수를 구해야 함)
        # 선택한 프로세서의 전선 길이 합(최소 길이)
    def dfs(idx, connect_cnt, wire_len):
        """
        :param idx: 선택하려는 코어 인덱스
        :param connect_cnt: 여태까지 선택한 코어 개수
        :param wire_len: 설치한 전선 길이의 합
        :return:
        """
        global max_connect_cnt, min_wire_len_sum

        # 현재까지 연결된 코어의 개수(connect_cnt) + 남은 코어의 개수 => 최대 코어의 개수보다 적으면, 굳이 진행 X
        # 남은 코어의 개수 = 전체 코어의 개수(core_list) - 현재 선택해야 하는 코어(idx)
        # 남은 개수 다 선택해도, 어차피 최대 코어의 개수를 못 넘기면 궅이 할 필요가 없기 때문
        if connect_cnt + (len(core_list) - idx) < max_connect_cnt:
            return

        # 모든 코어를 선택한 경우
        if idx == len(core_list):
            # 연결된 코어의 수가 기존 최대로 선택한 코어의 수보다 크면 갱신
            # 연결된 코어의 수가 최대 코어 수와 같다면, 연결 길이가 작을 때 갱신
            if connect_cnt > max_connect_cnt or connect_cnt == max_connect_cnt and wire_len < min_wire_len_sum:
                max_connect_cnt = max(connect_cnt, max_connect_cnt)
                min_wire_len_sum = min(min_wire_len_sum, wire_len)

        # 해당 코어를 선택하지 않는 경우
        # 그냥 다음 코어 살펴보면 됨
        dfs(idx + 1, connect_cnt, wire_len)

        # 해당 코어를 선택하는 경우
        # 선택한 코어의 좌표 가져오면 됨
        cx, cy = core_list[idx]
        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy # 다음에 이동할 좌표
            # 이동할 떄마다 전선 설치할거임
            # dfs 빠져나올 때, 전선 설치 원복 해줘야 함
            # 전선을 설치했던 좌표를 저장할 임시 변수를 하나 만들어서, 거기에 전선 좌표를 저장해야 한다.
            tmp_connect_pos_list = []

            # 벽 or 코어 or 전선 만날 때까지 전선을 이어준다
            while 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
                # 전선 설치하고 이동하기
                # 전선 설치할 좌표를 임시 공간에 저장
                tmp_connect_pos_list.append((nx, ny))
                nx, ny = nx + dx, nx + dy # 계속 이동

            # while문 끝났는데도 벽까지 도달 못하고, 중간에 코어 or 전선을 만났다면?
            # 이 경우, 굳이 dfs 진행할 필요 없음
            # 범위를 벗어났다는 건 부딪히지 않고 무사히 벽에 도달했다는 것이고,
            # 만약 아직도 범위 안에 있다면? 장애물 어딘가에 부딪혀서 범위 내에 있는 것임임
            if 0 <= nx < N and 0 <= ny < N:
               continue

            # 전선 설치할 좌표 꺼내와서, 그곳에 설치해주기
            # (0과 1이 아닌 것으로만 바꿔주면 됨!)
            for tx, ty in tmp_connect_pos_list:
                arr[tx][ty] = 2

            # 선택한 코어 개수 + , 연결한 전선 개수 +
            dfs(idx + 1, connect_cnt + 1, wire_len + len(tmp_connect_pos_list))

            # 전선 연결했던거 원복
            for tx, ty in tmp_connect_pos_list:
                arr[tx][ty] = 0


    dfs(0, 0, 0)
    print(f"#{test_case} {res}")