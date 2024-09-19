import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
population = list(map(int, input().split(' ')))
node_map = {}

# 조합 구현
def comb(arr, n):
    result = []
    if n > len(arr):
        return result
    if n == 1:
        for i in arr:
            result.append(i)
    elif n > 1:
        for i in range(len(arr)-n+1):
            for j in comb(arr[i+1:], n-1):
                result.append([arr[i]] + j)
    return result

# bfs
def bfs(i, visited, node_map):
    pass

for node in range(N):
    node_input = list(map(int, input().split(' ')))

    # 노드 번호와, 해당 노드와 인접한 노드의 번호를 map에 담기
    node_map[node] = node_input[1:]

    # 방문 여부 확인
    visited = [False for _ in range(N)]

    for i in range(N):
        dfs(i, visited, node_map)

print(node_map)