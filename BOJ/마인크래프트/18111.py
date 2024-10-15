import sys
sys.stdin = open('input.txt', 'r')

n, m, b = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]

# 최소, 최대 높이 구하기
min_height, max_height = min(map(min, ground)), max(map(max, ground))
result_time = float('inf')
result_height = 0

for target_height in range(min_height, max_height + 1):
    add = 0
    remove = 0

    # 모든 땅을 확인해가면서 블록 추가 & 제거
    for i in range(n):
        for j in range(m):
            height_diff = ground[i][j] - target_height
            if height_diff > 0:
                remove += height_diff  # 높이가 더 높다면, 그 차이만큼 블록 제거
            else:
                add -= height_diff  # 높이가 더 낮다면, 그 차이만큼 블록 추가

    # 필요한 블록 수가 인벤토리 블록 수와 맞는지 확인
    if remove + b >= add:
        time = remove * 2 + add  # 시간 계산 => 지우기 2초, 추가하기 1초
        if time <= result_time: # 최소 걸린 시간으로 갱신해주기
            result_time = time
            result_height = target_height

print(result_time, result_height)
