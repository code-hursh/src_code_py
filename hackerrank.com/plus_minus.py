def plusMinus(arr):
    t = len(arr)
    p = z = n = 0
    for i in arr:
        if i > 0:
            p += 1
        elif i == 0:
            z += 1
        else:
            n += 1
    def prnt(x):
        print("%1.6f"%(x))
    prnt(p / t)
    prnt(n / t)
    prnt(z / t)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().rstrip().split()))
    plusMinus(arr)
