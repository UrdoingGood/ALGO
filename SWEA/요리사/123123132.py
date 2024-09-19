import sys
sys.stdin = open("input.txt", "r")


def dfs(idx, num_sum):
    global result

    # 여태까지 누적의 합의 K인 경우, 결과에 +1
    if num_sum == K:
        result += 1

    # 누적의 합이 K보다 크거나 같으면 중단 (가지치기)
    # 문제에서 주어진 숫자들이 0보다 무조건 큼
    if num_sum >= K: return

    # 마지막 숫자까지 모두 선택한 경우 => 중단
    if idx == N: return

    # 선택한 경우
    dfs(idx + 1, num_sum + arr[idx])
    # 선택하지 않은 경우
    dfs(idx + 1, num_sum)


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 0

    # DFS 파라미터
    # 1. 재귀호출을 중단시킬 파라미터 => 현재 선택하냐마냐 를 정하는 인덱스
    # 2. 우리가 원하는 누적값 => 여태까지 선택한 숫자들의 합

    dfs()

    print(f"#{test_case} {result}")