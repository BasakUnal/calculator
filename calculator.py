cal = "12+3*7"

def calculate(inputs):
    stack = []
    oper = []
    n = 0
    for i in inputs:
        if i in "0123456789":
            stack.append(int(i))
            n = n+1
        elif i in "/*-+":
            oper.append(i)
       
    for i in range(n-2):
        num1 = stack.pop()
        num2 = stack.pop()
        a = oper.pop()
        
        if a == '+':
            stack.append(num1 + num2)
        elif a == '-':
            stack.append(num1 - num2)
        elif a == '*':
            stack.append(num1 * num2)
        elif a == '/':
            stack.append(num1 / num2)

    return stack.pop()

result = calculate(cal)
print(result)

