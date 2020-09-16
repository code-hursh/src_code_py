
x1, v1, x2, v2 = map(int, input().split())

def kangaroo(x1,v1,x2,v2):
    if v2 > v1:
        v1,v2 = v2,v1 # make v1 faster
        x1,x2 = x2,x1 
    x1 += v1
    x2 += v2
    while x1 <= x2:
        x1 += v1
        x2 += v2
        if x1 == x2:
            return "YES"
    return "NO"

def kangaroo(x1,v1,x2,v2):
    if v1 <= v2:
        return "NO"
    if (x2-x1)%(v1-v2) == 0:
        return "YES"
    return "NO"

