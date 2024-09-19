test_case = 10

def chk_cnt(matrix):
    for x in range(n):
        for y in range(n-1, 1, -1):
            cur = matrix[y][x]
            next_block = matrix[y-1][x]
            if cur == 0 or next_block == 0:
                continue

            matrix[y-1][x] += cur

def down(matrix, block, x):

    y = block-1
    block_num = block
    while y < n-1:
        n_block = matrix[y+1][x]
        if block <= n_block:
            break
        if n_block == 0:
            block *= 1.9
            for y_i in range(block_num):
                matrix[y-y_i+1][x] = matrix[y-y_i][x]
            matrix[y-(block_num-1)][x] = 0
            y += 1
        block += n_block
        y += n_block
        block_num += n_block


def simulation(matrix):
    for x, block in enumerate(matrix[0]):
        if block == 0:
            continue
        down(matrix, block, x)


    # 90도 회전
    matrix = [[1 if matrix[y][x] else 0 for y in range(n)] for x in range(n)]

    chk_cnt(matrix)


    for x, block in enumerate(matrix[0]):
        if block == 0:
            continue
        down(matrix, block, x)

    cnt1 = 0
    for row in matrix:
        if row[-1] == 0:
            continue
        cnt1 += 1
    cnt2 = 0
    for block in matrix[-1]:
        if block == 0:
            continue
        cnt2 += 1

    return cnt1, cnt2

for t in range(test_case):
    n = int(input())

    matrix = [list(map(int, input().split())) for _ in range(n)]
    cnt_matrix = matrix

    chk_cnt(matrix)

    result1, result2 = simulation(matrix)

    print(f"#{t+1} {result1} {result2}")