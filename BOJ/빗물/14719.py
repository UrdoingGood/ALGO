import sys
sys.stdin = open('input.txt', 'r')

H, W = map(int, input().split())
block = list(map(int, input().split()))
rain = 0

# block의 맨 양 끝에는 블록이 있어야 함 => left [1:] / right [:i]
# 탐색한 곳의 양 옆은, 자신보다 더 많은 블록이 있어야 함
    # 만약 양 옆에 자신보다 적은 개수의 블록이 있으면 물이 고일 수 없음
# right 옆으로 가면서, 더 많은 빗물을 담으면 rain에 추가
# 한 번 right 다 돌았으면 이제 left 옮겨서 계속 반복
    # right 끝까지 가거나, block 높이만큼 다 채워진 블록을 만나면(벽) 다음 left로 넘어가서 계속 탐색

