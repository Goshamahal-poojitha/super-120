def DFS(Node,visited,adj,ans):
    visited[Node]=1
    ans.append(Node)
    for i in adj(Node):
        if(visited[i]==0):
            dfs(i,visited,adj,ans)
def dfs(adj):
    v=len(adj)
    visited=[0]*v
    ans=[]
    Node=0
    if(visited[Node]==0):
        DFS(Node,visited,adj,ans)
    return ans
adj = {
   0:[1, 2, 3],
   1:[0, 3],
   2:[0, 3],
   3:[0, 1, 2]
}
