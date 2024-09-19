import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc = int(input())
    arr = list(map(int, input().split()))
    minus = 1
    while arr[-1] > 0:
        for i in range(len(arr)):
            arr[i] -= minus
            minus += 1
            if minus > 5:
                minus = 1
            if arr[i] <= 0:
                arr[i] = 0
                arr.append(arr.pop(0))
                break

    print(f"#{test_case}", *arr)