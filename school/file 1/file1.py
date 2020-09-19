'''
hello what is up this is a quick example text
sairam
'''

'''
okay goodbye see you tomorrow then
sairam
'''
def op1():
    with open("sairam.txt") as f:
        a = f.read()
        print(a)

#writing
def op2():
    with open("sairam.txt",'a') as f:
        f.write('to all of you')

#iterating over the text
def op3():
    for line in open('sairam.txt'):
        print(line,end = '')

def op4():
    pass
