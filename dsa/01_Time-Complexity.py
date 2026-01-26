# Compare
# 1 < loglogn < logn < n < n^2 < n^3 < n^4 < ... < 2^n

nums = [1,2,3,4,5]
n = len(nums)

for i in nums:
    print(i)
print("\n")

for i in range(n):
    print(nums[i])
    for j in range(i+1):
        print("Hii")
print("\n")
        
while (n > 0):
    print("Divide")
    n = n//2
    
# Time Complexity = O(n) + O(n^2) + O(logn) = O(n^2)