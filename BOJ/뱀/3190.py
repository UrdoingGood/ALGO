import sys
sys.stdin = open('input.txt', 'r')

from collections import deque


def rotate(dxy, ci, cj):
    if dxy == 0:
        return ci, cj+1
    elif dxy == 1:
        return ci+1, cj
    elif dxy == 2:
        return ci, cj-1
    else:
        return ci-1, cj


def bfs(i, j):
    global count, apple, direct

    # 뱀의 현재 방향
    # dxy가 0(j 증가), 1(i 증가), 2(j 감소), 3(i 감소)
    dxy = 0

    queue = deque()
    queue.append((i, j))

    # 이동한 시간
    time = 0

    while queue:
        time += 1

        # 뱀 현재 머리 위치
        # 머리 위치는 계속 변하니까 deque 끝으로 새롭게 들어감 => 인덱스가 -1
        ci, cj = queue[-1]

        # 뱀 다음 머리 위치
        ni, nj = rotate(dxy, ci, cj)

        # 벽에 부딪히는 경우
        if ni <= 0 or ni > N or nj <= 0 or nj > N:
            return time

        # 뱀 자신의 몸에 부딪히는 경우
        if (ni, nj) in queue:
            return time

        # 다음 위치로 이동
        queue.append((ni, nj))

        # 만약 사과가 있는 곳에 도착하면
        if (ni, nj) in apple:
            apple.remove((ni, nj)) # 사과 먹기
        else: # 사과가 없으면 popleft 해서 꼬리 줄이기
            queue.popleft()

        # direct가 존재하는지 여부도 함께 확인해야함
        # time == int(direct[0][0]) 이것만 봤더니 계속 IndexError가 났음
        if direct and time == int(direct[0][0]):
            if direct[0][1] == 'D':  # 오른쪽 회전
                dxy = (dxy + 1) % 4
            else:  # 왼쪽 회전
                dxy = (dxy + 3) % 4
            direct.pop(0) # 회전 다 했으면 해당 정보 없애주기


N = int(input())

K = int(input())
apple = []
for k in range(K):
    apple.append(tuple(map(int, input().split())))

L = int(input())
direct = []
for l in range(L):
    direct.append(tuple(input().split()))

time = 0
res = bfs(1, 1)
print(res)