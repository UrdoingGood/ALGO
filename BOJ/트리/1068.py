import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
node_list= list(map(int, input().split()))
remove_num = int(input())
tree = {}

for node_num in range(N):
    tree[node_list[node_num]].append(node_num)

print(tree)