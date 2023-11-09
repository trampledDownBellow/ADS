from collections import deque              

def dfs(graph, start):
    visited = set()                       
    stack = [start]                            

    while stack:
        vertex = stack.pop()                
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            stack.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

def bfs(graph, start):
    visited = set()                         
    queue = deque([start])                   

    while queue:
        vertex = queue.popleft()             
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

graph = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'D', 'E',],
    'C': ['C', 'A', 'D', 'F'],
    'D': ['D', 'B', 'F', 'C'],
    'E': ['A', 'B'],
    'F': ['D', 'C',]
}

print("DFS:")
dfs(graph, 'A')

print("BFS:")
bfs(graph, 'A')

graph = {
    'A': ['A', 'F'],
    'B': ['B', 'A', 'F', 'D'],
    'C': ['A', 'E', 'D',],
    'D': ['E'],
    'E': [],
    'F': []
}

print("DFS:")
dfs(graph, 'A')

print("BFS:")
bfs(graph, 'A')

