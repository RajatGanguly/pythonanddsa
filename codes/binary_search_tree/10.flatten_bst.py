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
    s = set()
    def flatten_to_dll(self, root):
        '''This function takes root node and makes it a doubly linked list'''
        head, prev = None, None
        def helper(root):
            if not root:
                return
            nonlocal prev, head
            helper(root.left)
            if not prev:
                head = root
            else:
                root.left = prev
                prev.right = root
            prev = root
            helper(root.right)
        helper(root)
        return head
        
    def travel_ll(self, head):
        node = head
        while node:
            print(node.val, end="\t")
            node = node.right
    
obj = Solution()
head = obj.flatten_to_dll(root)
obj.travel_ll(head)