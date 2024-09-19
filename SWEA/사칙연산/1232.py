def evaluate(node):
    if node not in tree:
        return float(tree_values[node])

    left = evaluate(tree[node][0])
    right = evaluate(tree[node][1])
    operation = tree_values[node]

    if operation == '+':
        return left + right
    elif operation == '-':
        return left - right
    elif operation == '*':
        return left * right
    elif operation == '/':
        return left / right


# 10개의 테스트 케이스를 처리합니다.
for test_case in range(1, 11):
    N = int(input())
    tree = {}
    tree_values = {}

    for _ in range(N):
        data = input().split()
        node = int(data[0])
        value = data[1]

        if len(data) == 4:  # 연산자 노드인 경우
            left_child = int(data[2])
            right_child = int(data[3])
            tree[node] = (left_child, right_child)
            tree_values[node] = value
        else:  # 숫자 노드인 경우
            tree_values[node] = value

    result = int(evaluate(1))  # 루트 노드부터 계산 시작
    print(f"#{test_case} {result}")
