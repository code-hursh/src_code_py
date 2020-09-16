class Stack:
    def __init__(self,*args):
        self.val = list(args)
        self.update()

    def __repr__(self):
        return(str(self.val))

    def push(self,*args):
        self.val += list(args)
        self.update()

    def pop(self):
        if not self.state():
            t = self.top
            del self.val[-1]
            self.update()
            return t

    def state(self):
        if not len(self.val):
            return 'underflow' 
        return True
    
    def update(self):
        self.top = self.val[-1]


e = list(input('enter expression') +')')
precedence = {        # operands with their precedence 
        '^': 3,
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1,
        }
y = '' # output expression
stack = Stack('(') # my stack
while stack.state != 'overflow':
    scan = e.pop(0)
    if scan in precedence.keys(): # if an operator is encountered 
        while stack.top != '(':
            if precedence[stack.top] >= precedence[scan]:
                y += stack.pop()
            else:
                break
        stack.push(scan)
    elif scan == '(':
        stack.push(scan)
    elif scan == ')':
        while stack.top != '(':
            y += stack.pop() # to pop the '('
        stack.pop()
    else:
        y += scan # if an operand is encountered
print(y)
