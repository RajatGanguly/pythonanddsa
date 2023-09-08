class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Constructing a tree manually

'''
                    1
                   / \
                  2   3         The diameter/longest path will be 4 (4 -> 2 -> 1 -> 3)
                 / \
                4   5
'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

class Solution:
    def diameter_brutforce(self, root):
        '''This function takes root node and returns diameter of the tree'''
        def height(root):
            return max(height(root.left), height(root.right)) + 1 if root else 0
        
        def dia(root):
            if not root:
                return 0
            left = dia(root.left)
            right = dia(root.right)
            slf = height(root.left) + height(root.right) + 1
            return max([left, right, slf])
        return dia(root)

    def diameter_optimized(self, root):
        '''This function takes root node and returns diameter of the tree'''
        if not root:
            return [0, 0]
        left = self.diameter_optimized(root.left)
        right = self.diameter_optimized(root.right)
        slf = left[1] + right[1] + 1
        return [max([left[0], right[0], slf]), max(left[1], right[1]) + 1]
    
obj = Solution()
ans1 = obj.diameter_brutforce(root)
print(ans1)

ans2 = obj.diameter_optimized(root)
print(ans2[0])