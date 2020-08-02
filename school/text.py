"""a = 20

def add(b = 35):
    def m():
        print(1)
    global a
    print(a,b)


#local
#then enclosed
# then local
# then available built in function
c = 40
def funct():
    a = 20
    print(a,c)
    def func2():
        print(2)
# funct()

def swap(x,y):
    global x,y
    x,y = y,x
    print(x,y)
x = 5
y = 7
swap(x,y)
print(x,y)
"""

