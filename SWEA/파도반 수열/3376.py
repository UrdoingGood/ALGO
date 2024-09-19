import sys
sys.stdin = open("input.txt", "r")

def pado(n):
    if n==1 or n==2 or n==3:
        return 1

    p[1], p[2], p[3] = 1, 1, 1
    for i in range(4, n+1):
        p[i] = p[i-2] + p[i-3]

    return p[n]

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    p = [0] * (n+1)
    print(f"#{test_case} {pado(n)}")

