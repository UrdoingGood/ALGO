import sys
sys.stdin = open("input.txt", "r")

from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    K = int(input())
    arr = [deque(list(map(int, input().split()))) for _ in range(1, 5)]
    rotate_info_list = [list(map(int, input().split())) for _ in range(K)]
    score_sum = 0

    for rotate_info in rotate_info_list:
        mag_idx, rotate = queue.popleft()

        if mag_idx != 4:
            if arr[mag_idx][2] != arr[mag_idx][6]:


