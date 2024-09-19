T = 10
for test_case in range(1, T + 1):
    length = int(input())
    infix = input()

    stack = []
    postfix = ''
    for i in infix:
        if i != '+':
            postfix += i
        else:
            if stack:
                postfix += stack.pop()
            stack.append(i)
            
    postfix += '+'
    calc = []
    for p in postfix:
        if p != '+':
            calc.append(int(p))
        else:
            a = calc.pop()
            b = calc.pop()
            calc.append(a + b)
            
    print(f"#{test_case} {calc.pop()}")