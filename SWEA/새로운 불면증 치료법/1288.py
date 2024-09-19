import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    digits = set()
    count = 0
    cnt_N = N

    while len(digits) < 10:
        count += 1
        cnt_N = count * N
        digits.update(str(cnt_N))

    print(f"#{test_case} {cnt_N}")