import sys
sys.stdin = open('input.txt', 'r')

H, W = map(int, input().split())
block = list(map(int, input().split()))
world = [[False] * W] * H

# 블록 쌓기
for i in range(H):
    for j in range(W):
