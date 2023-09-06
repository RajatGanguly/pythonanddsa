# This is an undirected unweighted graph and here we will use BFS algorith to check if there is any loop present or not
graph = [[1,2], [0,4], [0,3,4], [2,5], [1,2], [2,3], [7], [6]]

'''
    The above decleared graph is depected below
        0    3
      /   \ /  \    6
     1     2 - 5     \
      \   /           7
        4   
'''

class Solution:
    def cycle_detection_dfs(self, graph):
        '''This function takes an adjacency list and return an array of BFS Traversal'''
        n = len(graph)
        #creating a visited array to track if a node is visited or not
        visited = [-1]*n

        def dfs(node, parent = -1):
            visited[node] = 0
            for v in graph[node]:
                if visited[v] == -1:
                    dfs(v, node)
                elif v != parent:
                    return True

        for i in range(n):
            if visited[i] == -1:
                if dfs(i):
                    return "Cycle is present"
        return "Cycle is not present"
    
obj = Solution()
ans = obj.cycle_detection_dfs(graph)
print(ans)