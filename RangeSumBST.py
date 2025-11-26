# Time Complexity : O(N) where N is the length of the input list
# Space Complexity : O(H) where H is the height of the tree (due to recursion stack)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach:
# I am using a recursive approach to traverse the binary search tree (BST).
# I check if the current node's value is within the given range [low, high].
# If it is, I add its value to the total sum and recursively call the function
# for both left and right subtrees. If the current node's value is less than low,
# I only traverse the right subtree, and if it's greater than high, I only traverse
# the left subtree. This way, I efficiently calculate the sum of all node values
# within the specified range.

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0
        if not root:
            return 0
        # print(root.val)
        if root.val < low:
            return  self.rangeSumBST(root.right,low,high)
        if root.val > high:
            return self.rangeSumBST(root.left,low,high)
        return (root.val + self.rangeSumBST(root.right,low,high)+self.rangeSumBST(root.left,low,high))
        