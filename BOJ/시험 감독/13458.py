import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

# 시험장 개수만큼 총 감독관 필요
super_count = N
for i in range(N):
    # 총 감독관이 볼 수 있는 수(B)만큼 빼주고 남은 학생 수 확인
    A[i] -= B

    # 감독할 학생 없으면 넘어가기
    if A[i] <= 0:
        continue

    # 감독 가능한 수보다 학생 수가 적게 남으면 부감독 추가하면 됨
    if A[i] <= C:
        super_count += 1

    # 남은 학생 수에서 부 감독관이 볼 수 있는 수(C)만큼 나눠주고 올림
    elif A[i] > C:
        if A[i] % C != 0:
            super_count += A[i] // C + 1
        else:
            super_count += A[i] // C

print(super_count)
