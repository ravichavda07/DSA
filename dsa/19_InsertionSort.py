def insertionSort(nums):
    n = len(nums)
    for i in range(1,n):
        key = nums[i]
        j = i-1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j = j - 1
        nums[j+1] = key
        
nums = [64, 32, 25, 45, 20, 15, 2]
insertionSort(nums)
print(nums)