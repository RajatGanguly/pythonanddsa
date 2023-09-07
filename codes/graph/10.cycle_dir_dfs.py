# Check if there is any list in directed graph or not
graph = [[1], [2], [3], [0,3]]

class Solution:
    def dfs_dir_cycle(self, graph):
        '''This function takes an adjacency list and return if there is any cycle or not'''
        n = len(graph)
        visited = [False] * n
        dfs_visited = [False] * n
        
        def dfs(node):
            visited[node] = True
            dfs_visited[node] = True
            for v in graph[node]:
                if visited[v] and dfs_visited[v]:
                    return True
                elif not visited[v]:
                    if dfs(v):
                        return True
            dfs_visited[node] = False
            return False
        
        for i in range(n):
            if not visited[i]:
                if dfs(i):
                    return "Cycle Present"
        return "No Cycle Present"
                
    
obj = Solution()
ans = obj.dfs_dir_cycle(graph)
print(ans)