#!/usr/bin/python3
def dfs(graph, node, destination, visited):
    if node not in visited and destination not in visited:
        visited.append(node)
        for connected in graph[node]:
            dfs(graph, connected, destination, visited)
    return visited


#source and destination were provided, 
#considering S to be source and E to be destination for this current program
if __name__=="__main__":
    graph = {
        'S' :   ['A','C','G'],
        'A' :   ['B','S'],
        'B' :   ['F'],
        'C' :   ['D','E','F','S'],
        'D' :   ['C'],
        'E' :   ['C','H'],
        'F' :   ['C','G'],
        'G' :   ['F','S'],
        'H' :   ['E','G']
    }  
    final_path = dfs(graph, 'S', 'E', [])
    for node in final_path:
        print(node, end="->")
    print()