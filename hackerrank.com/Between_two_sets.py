def getTotalX(a, b):
    _max = min(b)
    _min = max(a)
    count = 0
    for number in range(_min,_max + 1):
        condition = True
        for scan in b:
            if scan % number != 0:
                condition = False
                break
        for scan in a:
            if number % scan != 0:
                condition = False
                break
        if condition:
            count += 1
    return count
                
n,m = map(int, input().split())

a = list(map(int,input().rstrip().split()))
b = list(map(int,input().rstrip().split()))

result = getTotalX(a, b)
print(result)

