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
    def boundary_traversal(self, root):
        '''This function takes root node and returns an array of boundary traversal'''
        ans = []
        if not root:
            return ans

        def left_traversal(root):
            if not root or (not root.left and not root.right):
                return
            ans.append(root.val)
            if root.left:
                left_traversal(root.left)
            else:
                left_traversal(root.right)
        
        def leaf_traversal(root):
            if not root:
                return
            if not root.left and not root.right:
                ans.append(root.val)
            leaf_traversal(root.left)
            leaf_traversal(root.right)

        def right_traversal(root):
            if not root or (not root.left and not root.right):
                return
            if root.right:
                right_traversal(root.right)
            else:
                right_traversal(root.left)
            ans.append(root.val)

        ans.append(root.val)
        #  Travelling left
        left_traversal(root.left)
        #  Travelling left side's leaf nodes
        leaf_traversal(root.left)
        #  Travelling right side's leaf nodes
        leaf_traversal(root.right)
        #  Travelling right
        right_traversal(root.right)

        return ans

obj = Solution()
ans = obj.boundary_traversal(root)
print(ans)