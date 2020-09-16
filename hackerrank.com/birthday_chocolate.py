n = int(input())
s = list(map(int, input().rstrip().split()))
d = int(input())
m = int(input())

def birthday(s, d, m):
    count = 0
    for i in range(0,len(s)-m+1):
        if sum(s[i:i+m]) == d:
            count += 1
    return count
