import sys
sys.stdin = open("input.txt", "r")

def dfs(idx, score_sum, cal_sum):
    global result

    # 제한 칼로리를 널기면 끝
    if cal_sum > L:
        return

    # 재료 개수만큼 돌았으면 끝
    if idx == N:
        result = max(result, score_sum)
        return

    # 인덱스 추가해가면서 dfs 돌리기
    dfs(idx + 1, score_sum + ingre[idx][0], cal_sum + ingre[idx][1])
    dfs(idx + 1, score_sum, cal_sum)

T = int(input())
for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    ingre = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    # 해당 재료를 선택한 경우
    # 시작 인덱스, 점수 합, 칼로리 합
    dfs(0, 0, 0)
    print(f"#{test_case} {result}")