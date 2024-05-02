from typing import *

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                subStr = ""
                while stack[-1] != "[":
                    subStr = stack.pop() + subStr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                stack.append(subStr*int(k))

        return "".join(stack)

if __name__ == '__main__':
    testcases = ["3[bba2[c]]", "2[abc]3[cd]ef", "100[leetcode]"]
    newStr = Solution()
    for case in testcases:
        ans = newStr.decodeString(case)
        print(ans)
