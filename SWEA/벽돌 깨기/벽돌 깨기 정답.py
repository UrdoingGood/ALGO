from collections import deque

T = int(input())


def copy_list(temp):
    return [arr[:] for arr in temp]


def bomb_brick(before_brick, start_x, start_y):
    bomb_que = deque()
    bomb_que.append((start_x, start_y, before_brick[start_x][start_y]))
    brick_temp = copy_list(before_brick)

    while bomb_que:
        x, y, bomb_range = bomb_que.popleft()
        if bomb_range == 0:
            continue
        brick_temp[x][y] = 0
        for d in range(4):
            nx, ny = x, y
            for n in range(1, bomb_range):
                nx += dx[d]
                ny += dy[d]
                if 0 <= nx < W and 0 <= ny < H:
                    if brick_temp[nx][ny]:
                        bomb_que.append((nx, ny, brick_temp[nx][ny]))
                else:
                    break
    return brick_temp


def sort_brick(before_bomb, after_shoot):
    for i in range(W):
        if before_bomb[i] == after_shoot[i]:
            continue
        for zero in range(H):
            if after_shoot[i][zero]:
                continue
            for num in range(zero, H):
                if after_shoot[i][num]:
                    after_shoot[i][zero], after_shoot[i][num] = after_shoot[i][num], after_shoot[i][zero]
                    break


def shoot(count_try, brick_temp):
    global ans
    if count_try == N:
        cnt = 0
        for a in brick_temp:
            for b in a:
                if b: cnt += 1
        if ans > cnt:
            ans = cnt
        return
    for i in range(W):
        if sum(brick_temp[i]) == 0:
            continue
        before_bomb = copy_list(brick_temp)
        for j in range(H - 1, -1, -1):
            if brick_temp[i][j] != 0:
                start_x = i
                start_y = j
                break
        after_shoot = bomb_brick(before_bomb, start_x, start_y)
        sort_brick(before_bomb, after_shoot)
        shoot(count_try + 1, after_shoot)
    if ans == float('inf'): ans = 0


for test_case in range(1, T + 1):
    N, W, H = map(int, input().split())
    brick = [list(map(int, input().split())) for _ in range(H)]
    rotate_brick = []
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    ans = float('inf')
    for i in range(W):
        rotate_brick.append([brick[j][i] for j in range(H - 1, -1, -1)])
    shoot(0, rotate_brick)
    print(f'#{test_case} {ans}')