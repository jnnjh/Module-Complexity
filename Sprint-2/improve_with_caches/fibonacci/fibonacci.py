def fibonacci(n):
    if n <= 1:
        return n
    nums = [0, 1]
    i = 0
    while i < n:
        nums.append(nums[len(nums) - 1] + nums[len(nums) - 2])
        i += 1
    return nums[n]
