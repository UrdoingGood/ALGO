def build(line):
    for i in range(1, N):
        if line[i] != line[i+1]:
            if abs(line[i] - line[i-1]) > 1: # 높이가 1차이 나는지 확인
                return False
            if line[i] < line[i-1]: # 왼쪽이 더 높은 경우 => 내리막
                for d in range(i, i+X): # 경사로 길이만큼 살펴보기
                    if d >= N or line[d] != line[i]: # 범위 넘어가는 경우 안 됨
                        return False
            else: # 오른쪽이 더 높은 경우 => 오르막
                for d in range(i-1, i-1-X, -1): # 경사로 길이만큼 역순으로 살펴보기
                    if d < 0 or line[d] != line[i-1]: # 범위 넘어가는 경우 안 됨
                        return False
        return True


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = 0

    for i in range(N):
        # 가로 세로 한 줄 단위로 봐야함
        row = arr[i]
        col = [arr[j][i] for j in range(N)]

        if build(row):
            res += 1
        if build(col):
            res += 1

    print(f"\n#{test_case} {res}")