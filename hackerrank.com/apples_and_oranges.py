# The first line contains two space-separated integers denoting the respective values of 's' and 't' .
# The second line contains two space-separated integers denoting the respective values of 'a' and 'b' .
# The third line contains two space-separated integers denoting the respective values of 'm' and 'n'.
# The fourth line contains m space-separated integers denoting the respective distances that each apple falls from point a .
# The fifth line contains n space-separated integers denoting the respective distances that each orange falls from point b.

def countApplesAndOranges(s,t,a,b,oranges,apples):
    if s > t:
        t,s = s,t
    def count(entities,loc):
        global s,t

        count = 0
        for entity in entities:
            if (entity + loc) in range(s,t+1):
                count += 1
        print(count)
    count(apples,a)
    count(oranges,b)
        
s,t = map(int, input().split())
a,b = map(int, input().split())
m,n = map(int, input().split())

apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))

countApplesAndOranges(s,t,a,b,oranges,apples)
