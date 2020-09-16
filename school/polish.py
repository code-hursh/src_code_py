e = list(input('enter expression') + ")")
precedence = {        # operands with their precedence 
        '^': 3,
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1,
        }

stack = ['('] # my stack
y = '' # output expression

while stack != []:
    scanned = e.pop(0) # scanned variable
    if scanned in precedence.keys(): # if an operator is encountered
        if scanned == '^' and stack[-1] == '^':
            stack.append(scanned)
            continue
        while stack[-1] != '(':
            if precedence[stack[-1]] >= precedence[scanned]:
                y += stack.pop()
            else:
                break
        stack.append(scanned)
    elif scanned == '(':
        stack.append(scanned)
    elif scanned == ')':
        while stack[-1] != '(':
            y += stack.pop()
        stack.pop() # to pop the '('
    else:
        y += scanned # if an operand is encountered

print(y)    
e = list(y)   
e = ['3','5','+','6','4','-','*','4','1','-2','^','+']
stack = []
while e:
    scanned = e.pop(0)
    if scanned in precedence.keys():
        temp = (stack.pop()+scanned+stack.pop())
        stack.append(temp) 
    else:
        stack.append(scanned)
print(stack[0])
