def bubbleSort(nums):
    n = len(nums)
    
    for i in range(0,n):
        for j in range(i,n):
            if (nums[i] >= nums[j]):
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp

nums = [64, 32, 25, 45, 40, 51, 2]
bubbleSort(nums)
print(nums)