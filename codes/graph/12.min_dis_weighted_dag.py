graph = [[[1,2], [4,1]], [[2,3]], [[3,6]], [], [[2,2], [5,4]], [[3,1]]]

class Solution:
    def min_dis_weihted_dag(self, graph):
        '''This function takes an adjacency list and returns minimum distance of all node from source'''
        n = len(graph)
        dis = [float('inf')] * n
        dis[0] = 0
        vis = [0] * n
        stack = []

        def dfs(node):
            vis[node] = 1
            for v in graph[node]:
                if not vis[v[0]]:
                    dfs(v[0])
            stack.append(node)
        
        dfs(0)
        while stack:
            node = stack.pop()
            for ver, distance in graph[node]:
                if dis[ver] > dis[node] + distance:
                    dis[ver] = dis[node] + distance
        for i in range(n):
            if dis[i] == float('inf'):
                dis[i] = -1
        return dis

obj = Solution()
ans = obj.min_dis_weihted_dag(graph)
print(ans)