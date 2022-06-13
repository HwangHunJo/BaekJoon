oper = input()
stack = []

def high(ch):
    if ch == '(' or ch == ')':
        return 0
    
    elif ch == '+' or ch == '-':
        return 1
    
    elif ch == '*' or ch == '/':
        return 2
    
    else:
        return -1

def isEmpty():
    if(len(stack) == 0):
        return True
    return False

def push(e):
    stack.append(e)

def pop():
    return stack.pop()

def peek():
    if(not isEmpty()):
        return stack[-1]
    else:
        return False

def size():
    return len(stack)

def clear():
    stack.clear()

out = []

for ch in oper:
    if ch in '(':
        push('(')
        
    elif ch in ')':
        while not isEmpty():
            op = pop()

            if op == '(':
                break
            else:
                out.append(op) 

    elif ch in "+-/*":
        while not isEmpty():
            op = peek()
            if(high(ch) <= high(op)):
                out.append(op)
                pop()
            else:
                break
        push(ch)
    else:
        out.append(ch)


while not isEmpty():
    out.append(pop())

print(''.join(out))