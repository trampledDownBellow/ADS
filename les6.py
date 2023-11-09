from collections import deque              # Двостороння черга

def dfs(graph, start):
    visited = set()                         # Створюємо пустий набір для відвіданих вузлів
    stack = [start]                            # Створюємо стек і додаємо початковий вузол до стеку

    while stack:
        vertex = stack.pop()                # Беремо вершину з вершини стеку
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            stack.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

def bfs(graph, start):
    visited = set()                         # Створюємо пустий набір для відвіданих вузлів
    queue = deque([start])                   # Створюємо чергу і додаємо початковий вузол до черги

    while queue:
        vertex = queue.popleft()             # Беремо вершину з початку черги
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

print("\nDFS:")
dfs(graph, 'A')

print("\nBFS:")
bfs(graph, 'A')

graph = {
    'A': ['A', 'F'],
    'B': ['B', 'A', 'F', 'D'],
    'C': ['A', 'E', 'D',],
    'D': ['E'],
    'E': [],
    'F': []
}

print("\nDFS:")
dfs(graph, 'A')

print("\nBFS:")
bfs(graph, 'A')

graph = {
    'A': ['3', '9'],
    'B': ['2', '5',],
    'C': ['12', '9', '4',],
    'D': ['4'],
    'E': [],
    'F': []
}

print("\nDFS:")
dfs(graph, 'A')

print("\nBFS:")
bfs(graph, 'A')

