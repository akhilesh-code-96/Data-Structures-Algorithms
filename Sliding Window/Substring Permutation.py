from collections import *

# Compare the count of substrings if they exists in the subString array.
def compare(orgCounter, subString, n):
    subArr = []
    for i in range(0, len(subString), n):
        subArr.append(subString[i : n + i])

    subArrCounter = dict(sorted(Counter(subArr).items()))

    for key, val in subArrCounter.items():
        if (key in orgCounter and orgCounter[key] != val) or key not in orgCounter:
            return False
        
    return True

# This function returns the count of sub-strings where the concatenation of all the strings in arr is same in some order.
def stringPermutation(s, arr):
    count = 0
    left = 0
    sumOfLengthArr = len(arr[0]) * len(arr)
    arrCounter = dict(sorted(Counter(arr).items()))

    for right in range(sumOfLengthArr, len(s)+1):
        subString = s[left : right]

        if compare(arrCounter, subString, len(arr[0])):
            count += 1

        left += 1
      
    return count

# Example:
s = "abcaabca"
arr = ["abc", "bca"]
ans = 1 # As only one sub-string in s i.e., "bcaabc" is equal to the concatenation of all the strings in arr in some order.
