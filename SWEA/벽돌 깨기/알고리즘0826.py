"""
가장 단순하게 접근
- 주어진 모든 열에 블럭을 쏘자
- N<=4, W<=12 이므로 시간복잡도는 최대 12^4 = 약 2만개 일 것임 => 괜춘!

1. 구슬을 다 쏘면 STOP (N == depth)
2. 블럭 터뜨리기 (연쇄적으로 터뜨리므로 BFS)
    => 큐에서 한 사이클 (큐가 빌 때까지)
    => 한 번에 터진다!
3. 모든 열에 대해 블럭 내리기기
"""

import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

dxy = [[-1,0], [1,0], [0,-1], [0,1]]

# depth : 던진 블록 개수 숫자
# broken_cnt : 현 시점까지 부순 블럭의 개수
# matrix : 현 시점까지 깨지고 남은 블럭 matrix
def dfs(depth, broken_cnt, matrix):
    global total_broken_block_cnt

    # 구슬을 다 쏜 경우
    if depth == N:
        total_broken_block_cnt = max(total_broken_block_cnt, broken_cnt)
        return

    # 가지치기 로직 필요할 것 같은데?

    # 모든 열에 블럭 던지기
    for w in range(W):
        """
        기존에 입력 받은 블록판에 있는 벽돌을 깨야 함.
        dfs로 진행 시 생각해야 하는 것 => 어떤 행위를 했을때, 그 행위를 복구해야 함
        
        1. 기존 블록판에 있는 블록을 쿨하게 부수고, DFS로 넘긴다. 그리고 부순 블럭을 다시 복귀함다
        2. 기존 블록판을 하나 복사해서 복사판을 부수고, 복사판을 dfs로 넘긴다.
            => 2번 방법이 나을듯
        """
        # 원본 배열 복사하기 deepcopy
        arr = [x[:] for x in matrix]

        # 이제 이 arr를 부셔보자!
        # 부수는 과정은 BFS로 진행해보자
        queue = deque()

        # 이번 회차에서 부순 벽돌의 개수를 저장할 변수
        tmp_broken_cnt = 0

        # 블록을 놓는 열에서 가장 맨 위 있는 블록을 큐에 집어넣음
        for h in range(H):
            if arr[h][w]: # 블럭이 존재하면, 큐에 집어넣고 for loop 탈출
                queue.append((h, w))
                break

        """
        큐가 빌 때까지 큐 안에 있는 벽돌을 하나씩 꺼내서, 그 안에 있는 숫자만큼 사방으로 부순다
        그 다음에 부서진 블럭은 다시 큐에 들어간다. 이 과정(한 사이클을 완수)하면 '동시에' 블럭을 터트린다.
        """
        while queue:
            x, y = queue.popleft()
            boom_cnt = arr[x][y] # 벽돌의 수
            arr[x][y] = 0 # 꺼낸 벽돌이 부셔졌으니, 0으로 빈공간 만들기
            tmp_broken_cnt += 1 # 터진 벽돌 개수 추가
            for dx, dy in dxy:
                for dist in range(boom_cnt):
                    nx, ny = x + (dx * dist), y + (dy * dist) # boom_cnt가 1이면, 자기 자신만 터져야 하기 때문에 dist를 곱해주는 것임

                    # 좌표 검사
                    # 범위 벗어나면 같은 방향으로는 더 탐색하지 않음
                    if 0 > nx or H <= nx or 0 > ny or W <= ny:
                        break

                    # 빈 곳인 경우에는 queue에 추가하지 않을 것임
                    if arr[nx][ny] == 0:
                        continue

                    # 이미 큐에 들어있는 경우에는 추가하지 않을 것임
                    if (nx, ny) in queue:
                        continue

                    queue.append((nx, ny))

        """
        모든 열에 대해 블럭 내리기
        1. 맨 위에서 내려오면서 블럭을 스택에 쌓고
        2. 맨 아래에서 올라오면서 블럭을 스택에서 pop
        => 모든 열에 대해서 진행해야 함
        """
        for j in range(W): # 모든 열에 대해서
            stack = []

            """
            1번 진행 => 맨 위에서 내려가면서 블럭을 스택에 추가
            """
            for i in range(H):
                if not arr[i][j]:
                    continue
                stack.append(arr[i][j])
                arr[i][j] = 0


T = int(input())
for test_case in (1, T+1):
    N, W, H = map(int, input().split()) # 던질 수 있는 블럭 수, 주어진 사각형 너비/높이
    matrix = [list(map(int, input().split())) for _ in range(H)] # 주어진 2차원 배열
    # 결과값
    """
    최대한 많은 벽돌을 부셔야 한다.
    점답은 최소로 남은 벽돌 개수
    
    주어진 총 벽달 개수 - 최대한 많은 벽돌 개수
    => 결과로 출력
    """
    total_broken_block_cnt = 0

    # 주어진 매트릭스의 총 벽돌 개수 카운트
    total_block_cnt = 0
    for r in range(H):
        for c in range(W):
            if matrix[r][c]: # 0이 아니면 == 1이면 == 블럭이라면!
                total_block_cnt += 1

    """
    dfs 파라미터
    1. 재귀를 중단할 파라미터 (몇 번 공을 던졌는지, 여태까지 공을 던진 횟수)
        => depth
    2. 누적해서 가져가고 싶은 파라미터 (여태까지 부신 블럭의 개수)
    """
    dfs(0, 0, matrix)

    res = total_block_cnt - total_broken_block_cnt
    print(f"#{test_case} {res}")