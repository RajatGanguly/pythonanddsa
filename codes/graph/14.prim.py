# Prim's algorithm uses 3 arrays to return the minimum spanning tree

graph = [[[1,5], [2,1]], [[0,5], [2,3]], [[0,1], [1,3]]]

class Solution:
    def prim_algorithm(self, graph):
        '''Prim's algorithm is used to get the minimum spanning tree out of a weighted undirected graph'''
        n = len(graph)
        key = [float('inf')] * n
        mst = [False] * n
        parent = [-1] * n
        key[0] = 0
        for _ in range(n-1): # The minimum spanning tree is to have n-1 edges for n nodes
            mn = float('inf')
            ind = -1
            for i in range(n):
                if not mst[i] and key[i] < mn:
                    mn = key[i]
                    ind = i
            mst[ind] = True
            for node, dis in graph[ind]:
                if not mst[node] and key[node] > dis:
                    key[node] = dis
                    parent[node] = ind
        return f"Cost of MST is: {sum(key)}"
    
obj = Solution()
ans = obj.prim_algorithm(graph)
print(ans)