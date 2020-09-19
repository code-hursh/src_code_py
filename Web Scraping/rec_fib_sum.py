"""
sum(3)
sum(2) + fib(3)
sum(1) + fib(2)
fib(0) + fib(1)
"""
def fib(n,S = 0):
    if n == 1:
        return(0,0)
    elif n == 2:
        return(1,1)



def array_print(L):
    length = len(L)
    if length == 1:
        return(L)

    return(array_print(L[1:])+L[0])


def pal(L,_ = 0):
    length = len(L)
    if length == 1:
        return(L)

    temp = (pal(L[1:],_+1)+L[0])
    if not _:
        if L == temp:
            return(True)
        else:
            return(False)
    return(temp)

def powr(n,m): # n.n.n.n...m times
    if m == 1:
        return(n)

    return(n*powr(n,m-1))
print(powr(2,10))


def sfib(n,S = 0):
    if n <= 2:
        return(n-1)

    return(sfib(n-1) + sfib(n-2) +1)


print(sfib(5))

def sfact(n,S=0): # n.n.n.n...m times
    if m == 1:
        return(n)
    S += fact(n-1)
    return(S)
print(powr(2,10))
