# Linked List is a linear data structure used to store data with connected nodes

'''
 ____       _______      _______      _______      _______
|head| --->| 1 | --|--->| 2 | --|--->| 3 | --|--->| 4 | X |
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

class Solution:
    def traverse(self, head):
        '''This function takes head pointer of a linked list and returns an array of lineraly traversed nodes'''
        node = head
        ans = []
        while node:
            ans.append(node.val)
            node = node.next
        return ans
    
obj = Solution()
ans = obj.traverse(head)
print(ans)