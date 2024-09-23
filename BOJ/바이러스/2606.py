import sys
sys.stdin = open("input.txt", 'r')
from collections import deque

def bfs(n):
    global nums
    count = 0
    queue = deque()
    queue.append(n)
    nums[n] = True
    while queue:
        node = queue.popleft()
        for q in graph.get(node, []): # 큐에 있는 것을 key로 가지는 것의 value 값들을
            if nums[q] != True: # 방문한 적이 없다면
                queue.append(q) # 모두 큐에 넣어주고
                nums[q] = True # 방문 처리
                count += 1 # 바이러스 걸린 노드 개수 추가
    return count

N = int(input())
graph = {} # 그래프 만들 딕셔너리
nums = [False] * (N+1) # 방문한 노드 표시할 리스트
M = int(input())
for m in range(M):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = [] # key에 없으면 새로 만들어주고,
    graph[a].append(b)  # 있는 key면 value로 추가해주기
    if b not in graph:
        graph[b] = []
    graph[b].append(a)

print(bfs(1))