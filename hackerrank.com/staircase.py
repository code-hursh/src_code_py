def staircase(n):
    for i in range(n+1):
        print(' '*(n-i)+'#'*i)
if __name__ == '__main__':
    n = int(input())
    
    staircase(n)
