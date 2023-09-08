# Bridge is an edge that connects two graph components

# graph = [[1], [0, 2], [1, 3], [2]]
graph = [[1,3], [0,2], [1,3], [0,2,4], [3,5], [4]]

class Solution:
    def bridge_detection(self, graph):
        '''This function takes adjacency list and returns the bridges in the graph'''
        n = len(graph)
        vis = [False] * n
        tin = [0] * n
        low = [0] * n
        timer = [0]
        ans = []
        
        def dfs(node, parent, timer):
            print(node, parent)
            vis[node] = True
            tin[node] = timer[0]
            low[node] = timer[0]
            timer[0] += 1
            for v in graph[node]:
                if v == parent:
                    continue
                if not vis[v]:
                    dfs(v, node, timer)
                    low[node] = min(low[node], low[v])
                    if low[v] > tin[node]:
                        ans.append([min(v, node), max(v, node)])
                else:
                    low[node] = min(low[node], tin[v])
        
        for i in range(n):
            if not vis[i]:
                dfs(i, -1, timer)
        return ans
    
obj = Solution()
ans = obj.bridge_detection(graph)
print(ans)