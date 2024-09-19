import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    n = len(arr)
    for i in range(N-1):
        if i % 2 == 0:
            max_idx = i
            for j in range(i+1, n):
                if arr[j] > arr[max_idx]:
                    max_idx = j
            arr[i], arr[max_idx] = arr[max_idx], arr[i]

        else:
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print(f"#{test_case} {' '.join(map(str, arr[:10]))}")
