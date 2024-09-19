# 1) 각 좌표에 모인 원자들을 저장 : 주어진 좌표에 한해서만 저장
# 2) 모인 원자 수가 2 이상인 경우, 에너지 방출
#   {(1,1) : [(1,10), (2,20), (3,30)], (2,2) : [(3, 40)] ... } 이런식으로 저장
#   (1,1)에는 세 개 모였다는 뜻
# 3) 단일 원자인 경우 => 방향에 따라 이동
#   이동 후 위치에 따른 원자 정보 저장
#   - 서로 한 칸 사이로 두고 마주보고 있으면 충돌 안 됨
#         해결 1) 이동을 0.5씩
#         해결 2) 좌표계를 2배로 늘린다
#     - 종료 범위?
#         해결 1) 원자의 범위를 벗어나면 안됨
# 4) 임시 공간 => 원본에 복사

import sys

sys.stdin = open("input.txt", "r")

# 2씩 이동하는 풀이
# 상(0), 하(1), 좌(2), 우(3)
dxy = [(0, 1), (0, -1), (-1, 0), (1, 0)]
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    boom_sum = 0
    atom_dict = {}

    # 입력값
    # [x, y, direction, energy]
    # 주어진 원자들에서 좌표별로 원자들을 모은다.
    for _ in range(N):
        x, y, dir, energy = map(int, input().split())
        c_pos = (x * 2, y * 2)  # 현재 위치

        # 처음 들어가는 키 값이면 리스트로 초기화, 이후부터는 초기화 안하고 append
        # if c_pos not in atom_dict:
        #     atom_dict[c_pos] = []
        # c_pos라는 키 값이 dict에 들어가 있지 않으면, []로 초기화
        # 들어가 있지 안으면 그냥 append 진행
        atom_dict.setdefault(c_pos, []).append((dir, energy))

    # 원자의 집합이 존배하면 계속 아래 과정 반복
    while atom_dict:
        tmp_dict = {}

        # 원자들의 집합 순회
        for (cx, cy), atoms in atom_dict.items():
            # 모인 원자 수가 2개인 경우, 에너지 방출
            if len(atoms) >= 2:
                boom_sum += sum(k for d, k in atoms)
                continue

            # 좌표에 혼자 있는 경우
            # 다음에 움직여야 하는 위치를 얻음
            d, k = atoms[0]  # 여기는 원자가 1개이기 때문에, 첫 번째 원소를 가져온다
            dx, dy = dxy[d]
            nx, ny = cx + dx, cy + dy

            # 범위를 벗어난 경우에는 임시 dict에 추가하지 않는다
            if nx <= -2000 or nx >= 2000 or ny <= -2000 or ny >= 2000:
                continue

            # 문제 없고, 이동한 좌표에 따라 라시 임시공간에 저장
            # 임시 공간이 원본과 똑같은 구조로 저장
            n_pos = (nx, ny)
            tmp_dict.setdefault(n_pos, []).append((d, k))

        # 충돌한 원자는 임시 공간에 저장하지 않고
        # 혼자인 친구는 방향에 따라 이동을 하고, 범위를 벗어나면 제외를 하고
        # 기존 dict에 저장하는 과정을 반복
        atom_dict = tmp_dict

    print(f"#{test_case} {boom_sum}")