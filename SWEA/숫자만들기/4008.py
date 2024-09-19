# 순열 문제
# N이 12까지 주어짐 => 12! 이므로 순열로 풀기 어려움
# dfs로 순열 문제를 풀어야 함

# 순서
# 1. 숫자를 하나 고르고
# 2. 연산자를 고르고
# 3. 다음 숫자를 골라라

# DFS에서 필요한 조건들
# 1. 재귀 호출을 중단시킬 파라미터
    # 숫자 개수만큼 하면 될 것임. 모든 숫자를 다 선택한 것이기 때문
# 2. 누적해서 결과를 가져갈 파라미터
    # res
# 3. 연산자 개수 담은 리스트
    # 연산자 사용할 때마다 해당 연산자에 해당하는 값을 줄여주기
# 4. 다른 경우의 수도 봐야하니 다시 되돌려주기

import sys
sys.stdin = open("input.txt", "r")


# DFS 구현에 있어서 중요한 것
# 1. 재귀호출을 중단할 파라미터 (어떤 숫자를 선택하고 있는지, 인덱스) => idx
# 2. 누적해서 가져갈 결과 파라미터 (지금까지 수식해서 나온 결과) => res
# 연산자 목록 => visited 리스트와 같은 역할임. 연산자 다 쓰면 끝나는 것이므로. => op_list
def create_num(op_list, idx, res):
    global max_num, min_num
    if idx == N: # 내가 선택한 숫자(idx)가 N에 도달하면, 끝나는 것임
        max_num = max(max_num, res)
        min_num = min(min_num, res)
        return

    # cp_cnt == 남은 연산자 개수
    for op_idx, op_cnt in enumerate(op_list):
        if op_cnt == 0:
            continue

        tmp_res = res
        if op_idx == 0:
            tmp_res += num_list[idx]
        elif op_idx == 1:
            tmp_res -= num_list[idx]
        elif op_idx == 2:
            tmp_res *= num_list[idx]
        elif op_idx == 3:
            tmp_res = int(tmp_res / num_list[idx])

        op_list[op_idx] -= 1
        create_num(op_list, idx + 1, tmp_res) # 모든 경우의 수가 끝나면,
        # 다른 것을 선택했을 경우의 수도 봐야하므로, 아래와 같이 원복 시켜주는 것임
        op_list[op_idx] += 1

T = int(input())
# 모든 연산자의 조합을 찾아주면 될듯?
for test_case in range(1, T + 1):
    N = int(input())  # 테케 개수
    op_input_list = list(map(int, input().split()))  # 연산자 +, -, *, / 개수 담긴 목록
    num_list = list(map(int, input().split()))

    # 문제에서 원하는 수식 결과의 최솟값과 최댓값을 구해야 함
    max_num = -1000000000
    min_num = 1000000000

    init_num = num_list[0]
    init_idx = 1

    # 문제에서 숫자 한 개는 고르고 들어갈 수 있음. 숫자 순서는 못 바꿈
    create_num(op_input_list, init_idx, init_num)
    print(f'{test_case} {max_num - min_num}')