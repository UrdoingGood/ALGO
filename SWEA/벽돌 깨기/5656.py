import sys
sys.stdin = open('input.txt', 'r')

# 구슬 쏠 위치 선택

# 구슬 명중한 벽돌 + 주변 벽돌 파괴

# 파괴된 벽돌 제거, 남은 벽돌 아래로 떨어뜨리기

# 위 과정 반복, 남은 벽돌 수 계산


# 연쇄적으로 부수기
def bfs():
    pass

# N번 수행
def dfs(arr, depth, col, row):
    global min_blocks
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    cx, cy = col, row

    for dx
    for dx, dy in dxy:
        nx, ny = cx + dx, cy + dy

    # 맨 윗 줄에 있으면
    # 그것이 현재 dfs
    # 그것을 0으로 바꾸고 그 옆에 있는 것으로 dfs, count 값은 최솟값으로 갱신


T = int(input())
for test_case in range(1, T+1):
    N, M, H = list(map(int, input().split(' ')))
    arr = [list(map(int, input(' '))) for _ in range(H)]
    total_broken = 0

    total_block_cnt

    for col in range(H):
        for row in range(M):
            dfs(arr, N, col, row)

    print(f"{test_case} {min_blocks}")


'''
def copy_board(board):
    return [row[:] for row in board]

def bomb_brick(board, x, y):
    queue = [(x, y, board[x][y])]
    board[x][y] = 0  # 벽돌 파괴

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        cx, cy, range_ = queue.pop(0)
        for i in range(4):
            nx, ny = cx, cy
            for _ in range(range_ - 1):
                nx += dx[i]
                ny += dy[i]
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] > 0:
                    queue.append((nx, ny, board[nx][ny]))
                    board[nx][ny] = 0

def drop_bricks(board):
    for col in range(len(board[0])):
        empty_row = len(board) - 1
        for row in range(len(board) - 1, -1, -1):
            if board[row][col] > 0:
                board[empty_row][col], board[row][col] = board[row][col], board[empty_row][col]
                empty_row -= 1

def dfs(board, depth):
    if depth == 0:
        return sum(cell > 0 for row in board for cell in row)

    min_bricks = float('inf')
    for col in range(len(board[0])):
        for row in range(len(board)):
            if board[row][col] > 0:
                new_board = copy_board(board)
                bomb_brick(new_board, row, col)
                drop_bricks(new_board)
                min_bricks = min(min_bricks, dfs(new_board, depth - 1))
                break

    return min_bricks

T = int(input())

for t in range(1, T + 1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    result = dfs(board, N)
    print(f"#{t} {result}")

'''