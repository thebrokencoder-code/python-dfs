graph_or_tree = {
"A" :["B","C"],
"B" :["D","E"],
"C" :["B","F"],
"D": [],
"E" : ["F"],
"F" :[],
"G" :["B","A","L","A","J","I"]
}
print(graph_or_tree["G"])
visited_path=[]
parent ={}
dfs_path=[]
for node in graph_or_tree.keys() :
    parent[node] =None
def DFS(node):
    visited_path.append(node)
    dfs_path.append(node)

    for i in graph_or_tree[node]:
        if i not in visited_path:
            parent[i] = node
            DFS(i)
        
DFS("A")
print("The graph =  ",graph_or_tree)
print("=============Depth First Search Algorithm===========")
print("traversal path of depth first search =\t",*dfs_path,sep = " -> ")


