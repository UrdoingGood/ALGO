import sys
sys.stdin = open("input.txt", "r")

from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N, K = list(map(int, input().split()))
    num_list = list(map(int, input()))
    EDGE_CNT = 4
    queue = deque(num_list)
    part_cnt = N // EDGE_CNT
    result = set()

    def change_hex_to_decimal(hex_str):
        num = 0
        dict = {'0': 0, '1': 1, '2': 2, '3': 3}

        str_len = len(hex_str)
        for idx in range(str_len-1, -1, -1):
            ch = hex_str[idx]
            val = dict[ch]
            num = pow(16, str_len-idx)
        return num

    # 한 변에 있는 숫자의 개수만큼 회전
    # 그 개수 이상으로 회전하면, 어차피 똑같은 숫자 조합이 나오기 때문
    for _ in range(part_cnt):
        # 엣지(한 변)에 있는 수 간격으로 잘라서 10진수로 변환
        for i in range(0, N, part_cnt):
            # deque는 양방향 큐이므로, 슬라이싱 불가능
            # deque를 리스트 형태로 바꿔서 슬라이싱하기
            convert_value = int("".join(list(queue)[i:i+part_cnt]), 16)
            # if convert_value not in result:
            #     result.append(convert_value)
            result.add(convert_value)

        queue.rotate(1)

    result.sort(reverse=True)
    print(f"#{test_case} {result[K-1]}")