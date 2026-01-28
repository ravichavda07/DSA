def Max_min_diff(arr):
    arr.sort()
    n = len(arr)
    mid = n//2
    maxi = 0
    mini = 0
    j = n-1
    
    for i in range(mid):
        maxi = maxi + abs(arr[i] - arr[j])
        j = j-1
        mini = mini + abs(arr[2*i] - arr[2*i-1])
    
    print("Maximum diff: ",maxi)
    print("Minimum diff: ",mini)

arr = [12, 5, 25, 10, 2, 15, 8, 30]
Max_min_diff(arr)