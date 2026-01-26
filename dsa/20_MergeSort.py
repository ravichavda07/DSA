def MergeSort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    MergeSort(arr, low, mid)
    MergeSort(arr, mid+1, high)
    Merge(arr, low, mid, high)

def Merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    while left <= high:
        temp.append(arr[left])
        left += 1
    
    while right <= high:
        temp.append(arr[right])
        right += 1
    
    for i in range(low, high+1):
        arr[i] = temp[i-low]

arr = [64, 32, 25, 45, 20, 15, 2]
MergeSort(arr, 0, len(arr)-1)
print(arr)