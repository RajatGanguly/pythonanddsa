class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

in_order = [4, 8, 2, 5, 1, 6, 3, 7]
post_order = [8, 4, 5, 2, 6, 7, 3, 1]

class Solution:
    def post_in_tree(self, in_order, post_order):
        '''This function takes postorder and inorder array and construct a tree out of it'''
        n = len(post_order)
        ind = n-1

        def find(element, start, end):
            for i in range(start, end+1):
                if in_order[i] == element:
                    return i
            return -1

        def build(start, end):
            nonlocal ind
            if ind < 0 or start > end:
                return None
            element = post_order[ind]
            ind -= 1
            pos = find(element, start, end)
            root = Node(element)
            root.right = build(pos+1, end)
            root.left = build(start, pos-1)
            return root
        
        root = build(0, n-1)
        return root
    
    def preorder(self, root):
        if not root:
            return
        print(root.val, end = "\t")
        self.preorder(root.left)
        self.preorder(root.right)
    
obj = Solution()
root = obj.post_in_tree(in_order, post_order)
obj.preorder(root)