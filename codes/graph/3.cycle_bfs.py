# This is an undirected unweighted graph and here we will use BFS algorith to check if there is any loop present or not
graph = [[1,2], [0,4], [0,3,4,5], [2,5], [1,2], [2,3], [7], [6]]

'''
    The above decleared graph is depected below
        0    3
      /   \ /  \    6
     1     2 - 5     \
      \   /           7
        4   
'''

class Solution:
    def cycle_detection_bfs(self, graph):
        '''This function takes an adjacency list and return if there is any cycle present or not'''
        from collections import deque
        n = len(graph)
        #creating a visited array to track if a node is visited or not
        visited = [-1]*n

        def bfs(node):
            q = deque([node])
            while q:
                vertex = q.popleft()
                visited[vertex] = 1
                for v in graph[vertex]:
                    if visited[v] == -1:
                        q.append(v)
                        visited[v] = 0
                    elif visited[v] == 0:
                        # if the element is not the parent and visited before then there must be a loop
                        return True
            return False

        for i in range(n):
            if visited[i] == -1:
                if bfs(i):
                    return "Cycle is present"
        return "Cycle is not present"
    
obj = Solution()
ans = obj.cycle_detection_bfs(graph)
print(ans)