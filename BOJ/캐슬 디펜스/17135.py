import sys
sys.stdin = open('input.txt', 'r')

N, M, D = map(int, input().split(' '))
arr = [list(map(int, input().split(' '))) for _ in range(M)]

# 궁수 세 명 위치 정하기 => combination 함수 구현하기
# 공격 시도
    # 거리가 D 이하인 범위 내에 적이 있는지 확인 => 적의 위치 저장
    # 적의 위치가 같은 것이 있다면, 가장 왼쪽에 있는 것을 공격하기로 선택
    # 공격한 적 제거, 공격 카운트 세기
    # 살아남은 적은 아래로 한 칸 이동
        # 이때, 성이 있는 칸으로 이동했으면 제거
# 격자판에 남은 적이 없으면 종료
    # 공격 카운트가 가장 적은 것으로 카운트 갱신