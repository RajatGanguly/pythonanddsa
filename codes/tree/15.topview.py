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
    def topview(self, root):
        '''This function takes root node and returns an array topview of the tree'''
        from collections import deque
        ans = []    
        q = deque([[root, 0]])
        d = {}
        while q:
            node, hd = q.popleft()
            if hd not in d:
                d[hd] = node.val
            if node.left:
                q.append([node.left, hd-1])
            if node.right:
                q.append([node.right, hd+1])
        min_hd, max_hd = min(d.keys()), max(d.keys())
        for hd in range(min_hd, max_hd+1):
            ans.append(d[hd])
        return ans
    
obj = Solution()
ans = obj.topview(root)
print(ans)