import sys
sys.stdin = open('input.txt', 'r')

# n : j열
# selected_honey : 선택된 꿀의 합계
# sum_honey : 한 경우의 수(일꾼1 + 일꾼2)에 대한 총 합계
# ci, cj : 선택하는 현재 위치
def dfs(n, selected_honey, sum_honey, ci, cj):
    global max_honey

    if selected_honey > C: # 선택한 꿀의 합계가 C를 넘으면 바로 종료
        return

    if n == M: # 종료 조건
        max_honey = max(max_honey, sum_honey) # 최댓값으로 갱신
        return max_honey

    # 다른 일꾼이 다음 꿀을 포함하는 경우
    dfs(n+1, selected_honey + arr[ci][cj+n], sum_honey + (arr[ci][cj+n])**2, ci, cj)

    # 다른 일꾼이 다음 꿀을 포함하지 않는 경우
    dfs(n+1, selected_honey, sum_honey, ci, cj)

T = int(input())
for test_case in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_honey = 0

    res = 0
    max_honey = 0
    sum1 = 0

    # 첫 번째 일꾼이 선택
    for i1 in range(N):
        for j1 in range(N-M+1): # M개를 골라야하므로, N(벌통 끝)에서 M만큼 전에 1 더한만큼까지만 선택할 수 있음
            max_honey = 0
            dfs(0, 0, 0, i1, j1)
            sum1 = max_honey # 일꾼 1의 최댓값
            # 두 번째 일꾼이 선택
            for i2 in range(i1, N):
                if i1 == i2: # 같은 줄에 있는 걸 선택하는 경우엔
                    sj = j1 + M # M만큼 뒤에서부터 선택해야 함
                else:
                    sj = 0
                for j2 in range(sj, N-M+1):
                    max_honey = 0
                    dfs(0, 0 ,0, i2, j2)
                    res = max(res, sum1 + max_honey) # 일꾼 2까지의 최댓값

    print(f"#{test_case} {res}")