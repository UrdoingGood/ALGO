import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = -1

    # 0:오른쪽 아래 대각선, 1:왼쪽 아래 대각선, 2:왼쪽 위 대각선, 3:오른쪽 위 대각선
    dxy = [[1,1], [1,-1], [-1,-1], [-1,1]]
    def dfs(cx, cy, mv_dir, visited_dessert):
        global res


        """
        재귀 종료 지점
        시작 지점(s_i, s_j) = 현재 지점(cx, cy) 이고, 방향이 3
        => 최고 방문 가게 수를 갱신하면 됨
        """
        if [si, sj] == [cx, cy] and mv_dir == 3:
            res = max(res, len(visited_dessert))
            return


        """
        백트래킹 할 만한 것 하나 더!
        
        res에는 현재까지 돈 최대 디저트 개수가 저장되어 있다
        내가 가게의 절반을 돌았는데, 현재까지 저장된 최대 디저트 개수의 절반도 못 먹었다? 그렇다면 굳이 나머지 절반을 돌아야 하나?
        """
        # 절반을 온 것은 방향으로 알 수 있음 (방향이 2라는 건, 왼쪽 상향 대각선인데,)
        if mv_dir == 2 and res >= len(visited_dessert) * 2:
            return


        # 좌표 범위를 벗어 났는지 확인
        if cx < 0 or cx >= N or cy < 0 or cy >= N:
            return


        # 지금 방문한 가게의 디저트를 섭취한 경우
        if arr[cx][cy] in visited_dessert:
            return


        # 어차피 뒤로 가는 경우가 없음 => 방문 여부는 굳이 확인하지 않겠습니다..


        # 현재 위치 방문 처리
        visited_dessert.add(arr[cx][cy])


        # 현재 방향에 따라서 이동한다
        nx, ny = cx + dxy[mv_dir][0], cy + dxy[mv_dir][1]
        dfs(nx, ny, mv_dir, visited_dessert) # 현재 방향을 유지한 채로 보내고
        if mv_dir < 3: # 오른쪽 윗 대각선이 아니라면, 방향을 꺾어서 진행한다. 오른쪽 윗 대각선이면, 사각형이 끝나는 지점임 => 시작 지점에 도달했는지 확인해야하므로, 오른쪽 윗 대각선일때는 굳이 방향을 꺾어서 내려갈 필요가 없음
            dfs(nx, ny, mv_dir + 1, visited_dessert) # 현재 방향에서 꺾은 채로 보낸다


        # 현재 위치의 방문 처리를 취소해야 함
        visited_dessert.remove(arr[cx][cy])

    """
    모든 좌표를 시작점으로 dfs 시작
    첫 번째 열은 돌지 않는다
    밑에서 2번째 행까지는 돌지 않는다
    => 사각형을 만들어야하는데, 제일 작은걸 생각해보면 !!
    """
    for si in range(N -2): # 행을 나타내고, 마지막 2개의 행은 돌지 않는다
        for sj in range(1, N-1): # 열을 나타내고, 첫 번째 열은 돌지 않는다
            """
            DFS 파라미터
            1. 재귀호출을 중단할 파라미터 => 끝났는지 안 끝났는지 확인할 좌표, 방향 필요
                => (시작 좌표, 방향)
                => 현재 좌표랑 시작 좌표가 같아야 하고, 방향은 우상향(3번)이어야 끝나는 것임
            2. 우리가 원하는 누적값(정답으로 쓸 것) => 디저트 개수(디저트 리스트 필요)
                => 중복 섭취 확인을 위해 여태까지 먹었던 디저트를 저장하는 set를 넘겨주자
                => (디저트 섭취 개수, set())
            """
            dfs(si, sj, 0, set())


    print(f"#{test_case} {res}")