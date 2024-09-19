import sys
import itertools
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # 벌통 크기, 벌통 개수, 꿀 채취할 수 있는 최대 양
    N, M, C = list(map(int, input().split()))
    honey_matrix = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0 # 총 수익을 저장할 변수

    # 숫자 리스트가 들어오면 각 인자를 제곱해서 더한 값을 반환
    def cal_square_sum(num_list):
        # 넘어온 num_list(꿀의 조합), 이 조합이 최대 용량 C를 넘으면 안 된다.
        if sum(num_list) > C:
            return 0
        # 각 꿀을 제곱해서 더하는 부분
        return sum(num**2 for num in num_list)

    def cal_max_honey(honey_list):
        max_honey = 0
        for select_cnt in range(1, M + 1):
            comb = itertools.combinations(honey_list, select_cnt)
            comb_list = list(map(cal_square_sum, comb))
            max_honey = max(max_honey, max(comb_list))
        return max_honey

    # 일꾼 1이 전체적으로 순회를 돈다
    # 대신 벌통의 개수(M) 직전까지만 순회를 해야함 (M은 연속되게 설치해야하기 때문)
    for fst_i in range(N):
        for fst_j in range(N - M + 1):
            # 일꾼 1이 선택한 인덱스(fst_i, fst_j)로부터 M개를 선택한 꿀의 리스트를 가져오자
            fst_select_honey_list = honey_matrix[fst_i][fst_j:fst_j+M] # M개의 벌통만큼 가져온 걸 나타냄
            # 위에서 선택한 꿀 목록에서 부분집합을 구하고, 이 부분집합 중 최대 이익을 구해야 함
            fst_select_honey_max = cal_max_honey(fst_select_honey_list)
            # # 부분 집합을 구하는 코드
            # # 주어진 리스트(fst_select_honey_list)에서 1개, 2개, ..., 전부를 선택한 조합
            # for select_cnt in range(1, M + 1):
            #     # 부분 집합의 조합을 구한다.
            #     comb = itertools.combinations(fst_select_honey_list, select_cnt)  # 꿀 목록에서 1개를 선택하는 예시, 2개를 선택하는 예시, ...
            #     # 각각의 부분 집합들의 이익을 구한다.
            #     # comb의 각 인자를 제곱해서 더한 값을 반환하는 함수를 만들어서 map으로 각자 적용
            #     fst_comb_list = list(map(cal_square_sum, comb))  # map : 왼쪽에 있는 내장함수를 오른쪽에 있는 인자에게 적용하는 것임
            #     # 여태까지 조합 중, 가장 이익이 높은 것들로 계속 갱신 됨
            #     fst_select_honey_max = max(fst_select_honey_max, max(fst_comb_list))

            for snd_i in range(fst_i, N):
                for snd_j in range(0, N - M + 1):
                    # 첫 번째 일꾼과 두 번째 일꾼이 같은 행을 골랐을 때
                    # 두 번째 일꾼이 첫 번째 일꾼보다 앞을 선택한 경우에는 skip
                    if fst_i == snd_i and fst_j + M > snd_j:
                        continue

                    snd_select_honey_list = honey_matrix[snd_i][snd_j:snd_j + M]
                    snd_select_honey_max = cal_max_honey(snd_select_honey_list, C)
                    max_sum = max(max_sum, fst_select_honey_max + snd_select_honey_max)

    print(f"#{test_case} {max_sum}")