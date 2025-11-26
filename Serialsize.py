# Time Complexity : O(N) where N is the length of the input list
# Space Complexity : O(N) for the output list
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach:
# I am using a breadth-first search (BFS) approach to serialize and deserialize the binary tree.
# In the serialize method, I use a queue to traverse the tree level by level, appending the values to the output list.
# I use a special marker for null nodes to ensure the structure of the tree is preserved.
# In the deserialize method, I split the input string and reconstruct the tree using a queue to keep track of parent nodes.
# I create left and right children based on the values in the list, using the special marker to identify null nodes.

from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    SEP = ','
    NIL = '#'
    def serialize(self, root):
        if not root:
            return self.NIL
        out = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node is None:
                out.append(self.NIL)
                continue
            out.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        i = len(out) - 1
        while i >= 0 and out[i] == self.NIL:
            i -= 1
        return self.SEP.join(out[:i+1]) if i >= 0 else self.NIL


    def deserialize(self, data):
        if not data or data == self.NIL:
            return None 
        vals = data.split(self.SEP)
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1
        while q and i < len(vals):
            parent = q.popleft()
            if i < len(vals):
                if vals[i] != self.NIL:
                    left = TreeNode(int(vals[i]))
                    parent.left = left
                    q.append(left)
                i += 1
            if i < len(vals):
                if vals[i] != self.NIL:
                    right = TreeNode(int(vals[i]))
                    parent.right = right
                    q.append(right)
                i += 1
        return root

