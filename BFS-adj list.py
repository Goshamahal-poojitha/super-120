def bfs(adj):
    v=len(adj)
    visited=[0]*v
    startNode=0
    ans=[]
    Q=[]
    if(visited[startNode]==0):
        visited[startNode]=1
        Q=[startNode]
        while(Q):
            node=Q.pop(0)
            ans.append(node)
            for i in adj[node]:
                if(visited[i]==0):
                    visited[i]=1
                    Q.append(i)
        return ans
adj= {
    0:[1, 2, 3],
    1:[0, 3],
    2:[0, 3],
    3:[0, 1, 2]
}
print(bfs(adj))
