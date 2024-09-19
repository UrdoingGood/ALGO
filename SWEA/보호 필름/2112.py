import sys
sys.stdin = open('input.txt', 'r')
from itertools import combinations


# 성능 검사 하는 함수
def inspect():
    pass

# depth : 약품 투입 횟수
# depth == 0 : 첫 번째로 투입할 막을 선택하는 idx
def dfs(depth):
    # 종료 조건
    if depth == len(selected_layers):
        return inspect()

    # 맨 처음 조건을 주어진 matrix에 접근
    layer_depth = selected_layers[depth]

    # 우리가 선택한 레이어 색상 바꾸면서 dfS 진행
    # 바꾼 다음엔 무조건 되돌려야 함
    temp_arr = matrix[layer_depth]

    # 우리가 바꿔야 하는 레이어를 선택할 것임
    # 이 친구를 모두 0으로 바꿔준다
    matrix[layer_depth] = [0]
defd


D, W, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(D)]
min_inject_cnt = -1 # 최소 약품 투입 횟수

# 약품 투입횟수를 0부터 D번까지 늘려나가면서 테스트
for inject_cnt in range(D+1):
    # 투입을 안 한다고 하면, 바로 검사하면 된다
    if inject_cnt == 0:
        # 주어진 셀들을 검사하는 함수
        # 검사 성공하면 True
        if inspect():
            min_inject_cnt = 0
            break

    # 조합적으로 D개 중 1개를 선택을 하고
    # 두께 D까지 있으면,
    for selected_layers in combinations(range(D), inject_cnt)

        # 우리가 조합적으로 선택한 레이어에 약품을 투입한 경우가
        # 성공적으로 성능 검사 통과했다면, 최소 약품 횟수 갱신하고 종료
        # DFS
        # 파라미터
        # 1. 재귀호출을 종료할 파라미터
            # 우리가 선택한 레이어 개수 (selected_layers 개수 & 통역사님 센스)
            # 여태까지 약품을 투입한 횟수 (초기값 0, depth)
        # 2. 누적해서 가져가고 싶은 값
        if dfs():
            min_inject_cnt = inject_cnt
            break
    if inject_cnt == 2:
         break