with open('a.txt') as f:
    i = f.read()
    for j in i:
        if j.isdigit():
            print(j)
f = open('a.txt','w')
f.write('bye')
f.close()
print(r'hello world\a for i in range() \n')
