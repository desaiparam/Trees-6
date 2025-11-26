# Time Complexity : O(N) where N is the length of the tree nodes
# Space Complexity : O(N) for the output list
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach:
# I am using a breadth-first search (BFS) approach to traverse the tree level by level.
# I maintain a queue to keep track of nodes along with their corresponding column indices.
# I also maintain a dictionary to store the nodes at each column index.
# As I traverse the tree, I update the minimum and maximum column indices encountered.
# Finally, I construct the output list by iterating through the column indices from minimum to maximum
# and appending the corresponding node values from the dictionary.  
# I return the output list containing the vertical order traversal of the tree.

from collections import defaultdict, deque
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque([(root,0)])
        min_col = 0
        max_col = 0
        cols = defaultdict(list)
        while q:
            node , col = q.popleft()
            min_col = min(min_col,col)
            max_col = max(max_col,col)
            cols[col].append(node.val)
            if node.left:
                q.append((node.left,col-1))
            if node.right:
                q.append((node.right,col+1))
        return [cols[i] for i in range(min_col,max_col+1)]
        