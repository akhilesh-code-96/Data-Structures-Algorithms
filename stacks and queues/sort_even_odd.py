from typing import *

def sortEvenOdd(nums: List[int]):
    nums.sort()

    stk_odd = []

    for i in range(len(nums)-1, -1, -1):
        if nums[i]%2 != 0:
            ele = nums.pop(i)
            stk_odd.append(ele)

    while len(stk_odd) != 0:
        odd = stk_odd.pop()
        nums.insert(0, odd)
    

# Example:
nums = [5, 2, 3, 6]
sortEvenOdd(nums)
print(nums)
