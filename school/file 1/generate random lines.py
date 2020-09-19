
#i/o
# N = int(input("enter no. of lines:"))
N = 30
R = range(30,40)
import random
#generate random lines
def generateLine(length):
    string = ''
    a = 0
    for i in range(length):
        a += 1
        string += chr(random.randint(48,123))
        if a >=2 and random.choice([0,1]):
            string += ' '
            a = 0
    return (string)

line_lengths = [a for a in R]
with open('a.txt','w') as f:
    for i in range(N):
        f.write(generateLine(random.choice(line_lengths))+'\n')


