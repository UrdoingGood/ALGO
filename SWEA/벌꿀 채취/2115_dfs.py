import sys
import itertools
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # 벌통 크기, 벌통 개수, 꿀 채취할 수 있는 최대 양
    N, M, C = list(map(int, input().split()))
    honey_matrix = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0 # 총 수익을 저장할 변수

    def dfs(honey_idx, honey_benefit, honey_sum, x, y):
        global part_sum

        # 가지치기
        # 이미 C를 넘었으면, 부분 집합이 늘어나면 무조건 C를 넘음으로 중단
        if honey_sum > C:
            return

        # 가리키는 꿀의 인덱스가 M에 도달하면 중단
        if honey_idx == M:
            part_sum = max(part_sum, honey_benefit)

        cnt_benefit = honey_matrix[x][y + honey_idx] ** 2
        cnt_sum = honey_matrix[x][y + honey_idx]
        # 부분 집합을 구하는 것과 같이 진행
        # 현재 꿀을 선택하거나
        dfs(honey_idx + 1, honey_benefit + cnt_benefit, honey_sum + cnt_sum, x, y)
        # 현재 꿀을 선택하지 않거나
        dfs(honey_idx + 1, honey_benefit, honey_sum, x, y)

    # 처음 로직은 똑같음
    # 부분 집합을 구해서, 최대 이익을 구하는 부분을 DFS로 구현할 거다.
    # DFS가 더 이득적인 부분 : C를 넘는 경우, 부분 집합을 만들지 않으므로 경우의 수를 줄일 수 있음
    # 가지치기
    for fst_i in range(N):
        for fst_j in range(N - M + 1):
            part_sum = 0 # 아래 DFS를 통해 얻은 최대 이익을 저장할 변수
            # 부분집합을 최대 이익을 구할 것임
            # 중간에 부분집합의 합이 C를 넘으면 가지치기 가능
            # DFS 함수 호출 시 필요한 것
                # 1) 재귀를 중단할 파라미터 => 선택할 벌통 인덱스(M에 도달하면 중단)
                # 2) 우리가 누적해서 원하는 결과값 => 각 꿀의 제곱을 합한 꿀의 이익
                # 3) 시작 위치
                # 4) 가지치기를 위해, 여태까지 합한 꿀의 양
                # => 선택할 벌통 인덱스, 꿀의 누적 이익, 꿀의 누적 합, 현재 시작 좌표

            dfs(0, 0, 0, fst_i, fst_j)
            fst_max = part_sum

            for snd_i in range(fst_i + 1, N):
                for snd_j in range(0, N - M + 1):
                    if fst_i == snd_i and snd_j < fst_j + M:
                        continue
                    part_sum = 0
                    dfs(0, 0, 0, snd_i, snd_j)
                    snd_max = part_sum
                    max_sum = max(max_sum, fst_max + snd_max)

    print(f"#{test_case} {max_sum}")