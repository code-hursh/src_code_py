N = int(input('enter no.'))
x = N
num = []
while x:
    num.append(x % 10)
    x = x // 10
print(num)


