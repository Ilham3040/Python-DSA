connection = {
    'Basuki': ['Wirawan', 'Maryono', 'Sumanto'],
    'Wirawan': ['Basuki', 'Widodo', 'Sumanto'],
    'Maryono': ['Basuki', 'Sumanto', 'Purwadi'],
    'Sumanto': ['Basuki', 'Wirawan', 'Maryono', 'Jumali', 'Handoko'],
    'Jumali': ['Sumanto', 'Sutrisno', 'Handoko'],
    'Sunarno': ['Purwadi', 'Sumono'],
    'Purwadi': ['Maryono', 'Sunarno'],
    'Handoko': ['Sumanto', 'Jumali', 'Joko'],
    'Joko': ['Handoko', 'Sumono'],
    'Sumono': ['Sunarno', 'Joko', 'Suwano'],
    'Sutrisno': ['Jumali', 'Suwano'],
    'Widodo': ['Wirawan'],
    'Suwano': ['Sutrisno', 'Sumono']
}

def bfs(graph,start,end):
    if start not in graph or end not in graph:
        return None

    queue = [(start,[start])]
    visited = set()

    while queue:
        node,path = queue.pop(0)

        if node in visited:
            continue

        visited.add(node)

        if node == end:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None
  
path_from_basuki_to_suwano = bfs(connection,"Basuki","Suwano")

print(path_from_basuki_to_suwano)