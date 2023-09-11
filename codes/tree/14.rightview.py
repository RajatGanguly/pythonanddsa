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
    def rightview(self, root):
        '''This function takes root node and returns an array rightview of the tree'''
        from collections import deque
        ans = []
        if not root:
            return ans
        q = deque([[root, 0]])
        visited_level = set()
        while q:
            node, level = q.popleft()
            if level not in visited_level:
                ans.append(node.val)
                visited_level.add(level)
            if node.right:
                q.append([node.right, level+1])
            if node.left:
                q.append([node.left, level+1])
        return ans
    
obj = Solution()
ans = obj.rightview(root)
print(ans)