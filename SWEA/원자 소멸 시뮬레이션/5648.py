import sys
sys.stdin = open("input.txt", "r")

def comb(arr, n):
    result = []  # 결과를 저장할 빈 리스트 초기화

    if n == 1:  # 선택할 요소의 수가 1인 경우
        # n이 1이면 더 이상 조합할 요소가 필요 없음
        # 각 요소 자체가 하나의 조합이므로, 각 요소를 리스트로 감싸서 반환
        return [[i] for i in arr]

    # 배열의 각 요소에 대해 반복
    for i in range(len(arr)):
        elem = arr[i]  # 현재 요소를 선택
        # 현재 요소 이후의 나머지 요소들로 n-1개의 조합을 재귀적으로 생성
        for rest in comb(arr[i + 1:], n - 1):  # arr[i+1:]는 현재 요소 이후의 모든 요소를 포함
            result.append([elem] + rest)  # 현재 선택한 요소와 재귀 호출을 통해 얻은 조합을 합침

    return result  # 최종 조합 결과 반환

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    sum_energy = 0
    meeting_x = 0
    meeting_y = 0
    atom_dict = {}

    # 상(0), 하(1), 좌(2), 우(3)
    for _ in range(N): # 원자 다 돌기
        x, y, arrow, energy = list(map(int, input().split()))
        atom_dict[(x, y)] = (arrow, energy)

    time_to_energy = {}

    # 모든 원자를, 두 개씩 조합하여, 만날 수 있는지 확인
    for key, value in comb(list(atom_dict.items()), 2):
        time = None

        # 1. x 좌표가 같고, y는 부호만 다르면 만날 수 있을 것임
        # => 단, 방향이 서로 반대여야 함
        if key[0][0] == key[1][0]: # x 같음
            if (value[0][1] == 0 and value[1][1] == 1) or (value[0][1] == 1 and value[1][1] == 0):
                time = (max(value[0][1], value[1][1]) - min(value[0][1], value[1][1]))/2
        elif key[0][1] == key[1][1]:  # y 같음
            if (value[0][0] == 3 and value[1][0] == 4) or (value[0][0] == 4 and value[1][0] == 3):
                time = (max(value[0][0], value[1][0]) - min(value[0][0], value[1][0]))/2

        # 2. x 좌표끼리, y 좌표끼리의 차이값이 같으면, 만날 수 있을 것임(|x1 - x2| == |y1 - y2|)
        # => 단, 방향이 상이면 좌우의 y축이 더 높아야 하고, 방향이 하이면 좌우의 y축이 더 낮아야 함
        # |x1 - x2| 초 후에 충돌
        if abs(key[0][0] - key[1][0]) == abs(key[0][1] - key[1][1]):
            if value[0][0] == 0 and key[0][1] < key[1][1]: # 상 방향인 y가 더 낮게 있고,
                    if value[1][0] == 4 and key[1][0] < key[0][0]: # 우 방향인 x가 더 적어야 함
                        time = abs(key[0][0] - key[1][0])
                    elif value[1][0] == 3 and key[1][0] > key[0][0]: # 좌 방향인 x가 더 커야 함
                        time = abs(key[0][0] - key[1][0])

            elif value[1][0] == 0 and key[1][1] < key[0][1]:  # 상 방향인 y가 더 낮게 있고,
                    if value[0][1] == 4 and key[0][0] < key[1][0]:  # 우 방향인 x가 더 적어야 함
                        time = abs(key[0][0] - key[1][0])
                    elif value[0][1] == 3 and key[0][0] > key[1][0]:  # 좌 방향인 x가 더 커야 함
                        time = abs(key[0][0] - key[1][0])

            elif value[0][0] == 0 and key[0][1] > key[1][1]:  # 하 방향인 y가 더 위에 있고,
                    if value[1][0] == 4 and key[1][0] < key[0][0]:  # 우 방향인 x가 더 적어야 함
                        time = abs(key[0][0] - key[1][0])
                    elif value[1][0] == 3 and key[1][0] > key[0][0]:  # 좌 방향인 x가 더 커야 함
                        time = abs(key[0][0] - key[1][0])

            elif value[1][0] == 0 and key[1][1] > key[0][1]:  # 상 방향인 y가 더 위에 있고,
                    if value[0][1] == 4 and key[0][0] < key[1][0]:  # 우 방향인 x가 더 적어야 함
                        time = abs(key[0][0] - key[1][0])
                    elif value[0][1] == 3 and key[0][0] > key[1][0]:  # 좌 방향인 x가 더 커야 함
                        time = abs(key[0][0] - key[1][0])

        if time is not None:
            if time not in time_to_energy:
                time_to_energy[time] = 0
            time_to_energy[time] += value[0][1] + value[1][1]

    sum_energy = sum(time_to_energy.values())

    # 그럼 여러 개 만나는 경우는 어떻게 하지?
    # 만나게 될 좌표에 해당하는 리스트 위치에, 만나게 되는 원소들의 값 누적합해서 넣기

    # 충돌 후에는 해당 원소는 조합에서 제외
    # 먼저 만나게 되는 원소가 무엇인지도 처리해야할듯.........

    print(f"#{test_case} {sum_energy}")
