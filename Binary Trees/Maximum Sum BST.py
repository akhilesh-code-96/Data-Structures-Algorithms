# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.max_sum = float('-inf')

    def helper(self, root: Optional[TreeNode]) -> tuple[float, float, int]:
        if not root:
            return float('inf'), float('-inf'), 0

        left = self.helper(root.left)
        right = self.helper(root.right)

        if left[1] >= root.val or right[0] <= root.val:
            return float('-inf'), float('inf'), 0

        curr_sum = left[2] + root.val + right[2]
        self.max_sum = max(self.max_sum, curr_sum)

        return min(root.val, left[0]), max(root.val, right[1]), curr_sum


    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return max(self.max_sum, 0)

# takeinput of nodes and convert that into root, right, left with the help of a TreeNode class and then return the root.
BST = Solution()
ans = BST.maxSumBST(root)
print(ans)
