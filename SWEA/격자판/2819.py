import sys
sys.stdin = open("input.txt", "r")


def dfs(i, j, count, nums):
    dx = [1, -1, 0, 0]  # x축으로 움직일 좌표
    dy = [0, 0, 1, -1]  # y축으로 움직일 좌표
    nums += matrix[i][j]  # 방문하는 요소를 문자열에 추가
    if count == 6:  # count가 6이되면, 7자리가 된 것이므로
        res.add(nums)  # 그 문자열을 set에 추가해서 반환
        return
    for k in range(4):  # x,  y축 이동 상하좌우 총 4번
        if 0 <= i+dx[k] < 4 and 0 <= j+dy[k] < 4:  # 행렬 범위 내에서 움직이기
            dfs(i+dx[k], j+dy[k], count+1, nums)  # count 증가시키면서, 이동한 좌표를 시작점으로 dfs 수행


T = int(input())
for test_case in range(1, T + 1):
    count = 0
    res = set()  # 중복 제거하기 위해 set() 타입으로 정의
    nums = ''  # 7자리 문자를 만들어낼 문자열
    matrix = [list(input().split()) for _ in range(4)]  # 행렬 입력 받기

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            dfs(i, j, count, nums)  # 행렬 요소 하나하나씩 방문하여(시작점으로 하여) dfs 수행

    print(f"#{test_case} {len(res)}")