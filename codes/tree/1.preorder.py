class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Constructing a tree manually

'''
                    1
                   / \
                  2   3
                 / \
                4   5
'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

class Solution:
    def preorder(self, root):
        '''This function takes root node and returns an array of preorder traversal'''
        ans = []
        def dfs(root):
            if not root:
                return
            ans.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ans
    
obj = Solution()
ans = obj.preorder(root)
print(ans)