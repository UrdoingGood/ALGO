import sys
sys.stdin = open("input.txt", "r")

# 왼쪽 괄호 만나면 막대기 개수(= 스택 개수) += 1, 결과 += 1
# () 레이저가 되면, 막대기 개수(= 스택 개수)만큼 결과 += n
# 막대 끝을 나타내는 오른쪽 괄호 만나면 => 결과 += 1

T = int(input())
for test_case in range(1, T + 1):
    p = input()
    stack = []
    res = 0

    for i in range(len(p)):
        if p[i] == '(':
            stack.append(p[i])
        if p[i] == ')':
            if p[i-1] == '(':
                stack.pop()
                res += len(stack)
            else:
                stack.pop()
                res += 1

    print(f"#{test_case} {res}")
