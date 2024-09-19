import sys
sys.stdin = open("input.txt", "r")

def dfs(n, a_list, b_list):
    global res
    # 종료 조건 : 재료 번호 다 탐색한 경우
    if n == N:
        if len(a_list) == len(b_list): # a와 b 둘다 선택 완료
            asum = bsum = 0
            for i in range(N//2): # 선택한 재료 번호로 만들 수 있는 모든 조합의 합 구하기
                for j in range(N//2):
                    asum += arr[a_list[i]][a_list[j]]
                    bsum += arr[b_list[i]][b_list[j]]
            res = min(res, abs(asum-bsum))
        return

    dfs(n+1, a_list+[n], b_list) # a 음식에 재료 추가
    dfs(n+1, a_list, b_list+[n]) # b 음식에 재료 추가

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = float('inf')

    # 선택할 재료 번호 => n
    # a 음식 만들기 => a_list
    # b 음식 만들기 => b_list
    dfs(0, [], [])

    print(f"#{test_case} {res}")