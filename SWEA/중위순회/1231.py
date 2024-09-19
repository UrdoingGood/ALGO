import sys
sys.stdin = open("input.txt", "r")

def in_order(node):
    if node:
        in_order(data[node][2])
        print(data[node][1], end='')
        in_order(data[node][3])

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    # map 첫 번째 파라미터 => function
    # 두 번째 파라미터 => each object
    data = [list(map(lambda x: int(x) if x.isdecimal() else x, input().split())) for _ in range(N)]
    # data = [list(input().split()) for _ in range(N)]
    # for i in range(N):
    #     for j in range(len(data[i])):
    #         if data[i][j].isdecimal():
    #             data[i][j] = int(data[i][j])

    # 0 넣어서 길이 맞춰주기
    # 길이 맞춰주지 않으면, data[node][2]나 data[node][3]이 비어있는 경우에는 out of range가 뜨기 때문!
    for arr in data:
        while len(arr) != 4:
            arr.append(0)

    # 첫 번째 인덱스가 0번에 들어가 있는 상황
    # 1번 인덱스부터 보도록 하기 위해, 0번 인덱스를 0으로 채워줌
    data.insert(0, [0, 0, 0, 0])
    print(f"#{test_case}", end=' ')
    in_order(1)
    print()
