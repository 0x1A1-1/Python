# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ans = {}
    
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ans = {}
        depth = 0
        self.traverse(root, depth)
        vals = []
        for i in self.ans:
            vals.append(self.ans[i])
        return vals
    
    def traverse(self, node, depth):
        
        if node == None:
            return
        
        if depth in self.ans:
            if self.ans[depth]<node.val:
                self.ans[depth] = node.val
        else:
            self.ans[depth] = node.val
    
        self.traverse(node.left, depth+1)
        self.traverse(node.right, depth+1)
        
        
        
        
    
