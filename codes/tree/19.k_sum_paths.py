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
    def lca(self, root, k):
        '''This function takes root node and two nodes and return lowest common ancestor of the two nodes'''
        count = 0
        res = []
        def f(root):
            nonlocal count
            if not root:
                return 0
            res.append(root.val)
            left = f(root.left)
            right = f(root.right)
            sm = 0
            for i in res[::-1]:
                sm += i
                if sm == k:
                    count += 1
            res.pop()
        f(root)
        return count
    
obj = Solution()
ans = obj.lca(root, 6)
print(ans)