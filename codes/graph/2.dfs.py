# This is an undirected unweighted graph and here we will use DFS algorith to traverse the graph
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
    def dfs_traversal(self, graph):
        '''This function takes an adjacency list and return an array of DFS Traversal'''
        n = len(graph)
        ans = []
        visited = [False]*n #creating a visited array to track if a node is visited or not

        def dfs(node):
            visited[node] = True
            ans.append(node)
            for v in graph[node]:
                if not visited[v]:
                    dfs(v)

        for i in range(n):
            # checking nodes are visited or not
            # this checking is important for graph with multiple component
            if not visited[i]:
                visited[i] = True
                dfs(i)
        return ans
    
obj = Solution()
ans = obj.dfs_traversal(graph)
print(ans)

# Notes:    This algorithm can also be used in counting components in a graph
# by incrementing a variable each time the loop got one element with visited[i] == True