def SelectionSort(nums):
    n = len(nums)
    for i in range(n):
        min = i
        for j in range(i,n):
            if nums[min] > nums[j]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]

nums = [64, 32, 25, 45, 20, 15]
SelectionSort(nums)
print(nums)
