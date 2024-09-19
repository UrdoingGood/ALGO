import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    count = 0
    print(f"#{test_case} {count}")

"""
1. 각 칸마다 주위에 폭탄이 몇 개있는지?
2. 아무곳이나 한군데 누르고, 만약 주변에 폭탄이 없다면, 8방향으로 뻗쳐 나가면서 오픈됨. 그 오픈 된 것을 QUEUE에 넣기 => BFS
3. 지뢰가 있는 칸, 숫자가 있는 칸은 넘어가기
4. 전체를 또 훝으면서 숫자 하나하나 누르면서 열어주기
"""
