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
    def height(self, root):
        '''This function takes root node and returns height of the tree'''
        return max(self.height(root.left), self.height(root.right)) + 1 if root else 0
    
obj = Solution()
ans = obj.height(root)
print(ans)