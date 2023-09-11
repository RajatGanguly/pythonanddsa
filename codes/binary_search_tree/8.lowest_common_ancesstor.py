class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Constructing a bst manually

'''
                    4
                   / \
                  2   5
                 / \
                1   3
'''
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

class Solution:
    def lca(self, root, n1, n2):
        '''This function takes root node and two nodes and returns lowest common ancestor of them'''
        if not root:
            return None
        if root.val > n1 and root.val > n2:
            return self.lca(root.left, n1, n2)
        elif root.val < n1 and root.val < n2:
            return self.lca(root.right, n1, n2)
        else:
            return root
    
obj = Solution()
node = obj.lca(root, 3, 5)
print(node.val)