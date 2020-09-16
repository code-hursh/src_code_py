def miniMaxSum(arr):
    arr.sort()
    S = 0
    for i in range(1,len(arr)-1):
        S += arr[i]
    print(arr[0]+S,arr[-1]+S)
