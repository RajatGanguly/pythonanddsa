# Return min distance from all node from source node of an unweighted undirected graph
graph = [[1,2], [0,4], [0,3,4,5], [2,5], [1,2], [2,3], [7], [6]]

class Solution:
    def bfs_min_dis(self, graph, src):
        '''This function takes an adjacency list and returns minimum distance of all node from source'''
        from collections import deque
        n = len(graph)
        dis = [float('inf')] * n
        dis[src] = 0 # Because source has no distance from itself
        q = deque([src])
        while q:
            node = q.popleft()
            for v in graph[node]:
                if dis[v] > dis[node] + 1:
                    dis[v] = dis[node] + 1
                    q.append(v)
        return dis
    
obj = Solution()
ans = obj.bfs_min_dis(graph, 0)
print(ans)