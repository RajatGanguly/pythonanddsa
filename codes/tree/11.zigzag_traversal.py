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
    def zigzag_order(self, root):
        '''This function takes root node and returns an array of zigzag order traversal'''
        from collections import deque
        ans = []
        if not root: # If root is none it will return empty array
            return ans
        q = deque([root])
        left_to_right = True
        while q:
            res = []
            for _ in range(len(q)):
                node = q.popleft()
                res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans += res if left_to_right else res[::-1]
            left_to_right ^= 1
        return ans
 
obj = Solution()
ans = obj.zigzag_order(root)
print(ans)