import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

N = int(input())
input_list = list(map(int, input().split()))
remove_node = int(input())

# 트리 만들기
tree = {}
root = -1
for child in range(N):
    parent = input_list[child]
    if parent == -1:
        root = child
    else:
        if parent not in tree:
            tree[parent] = []
        tree[parent].append(child)


# 노드 삭제하기
# append는 한 개의 값만 추가, extend는 여러 개를 추가
# 딕셔너리 key 삭제할때는 del 사용하기
def remove_bfs(node):
    queue = deque()
    queue.append(node)
    while queue:
        rm_node = queue.popleft()
        if rm_node in tree:
            queue.extend(tree[rm_node]) # 자식 노드를 큐에 추가
            del tree[rm_node] # 본인은 삭제되기
    for child in tree.values(): # 트리의 모든 values(== 자식 노드)
        if node in child: # 삭제하는 노드 번호도 포함되어 있다면
            child.remove(node) # 그것을 삭제
            break


remove_bfs(remove_node)


# 리프 노드 개수 세기
def count_bfs(root):
    queue = deque()
    queue.append(root) # root부터 보기
    count = 0
    while queue:
        node = queue.popleft()
        if node not in tree or len(tree[node]) == 0: # 트리의 key에 없거나 자식 노드 없으면 리프노드!
            count += 1
        else:
            queue.extend(tree[node])
    return count


print(count_bfs(root))