class Solution(object):
   def diameterOfBinaryTree(self, root):
      """
      :type root: TreeNode
      :rtype: int
      """
      self.ans = 0
      self.dfs(root)
      return self.ans
   def dfs(self, node):
      if not node:
         return 0
      left = self.dfs(node.left)
      right = self.dfs(node.right)
      self.ans =max(self.ans,right+left)
      return max(left+1,right+1)
