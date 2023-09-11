# This problem is also known as LONGEST BLOODLINE PROBLEM
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
                     \
                      6
'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)

class Solution:
    def lca(self, root, node1, node2):
        '''This function takes root node and two nodes and return lowest common ancestor of the two nodes'''
        if not root:
            return None
        if root.val == node1 or root.val == node2:
            return root
        left = self.lca(root.left, node1, node2)
        right = self.lca(root.right, node1, node2)
        if left and right:
            return root
        if left:
            return left
        if right:
            return right
        return None
    
obj = Solution()
ans = obj.lca(root, 4, 6)
print(ans.val)