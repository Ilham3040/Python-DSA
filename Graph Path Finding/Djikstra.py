order = {
    'Pak Handoko': 1,
    'Pak Sunarno': 2,
    'Pak Sutrisno': 3,
    'Pak Jumali': 4,
    'Pak Joko': 5,
    'Pak Sumanto': 6,
    'Pak Hadi': 7,
    'Pak Sumono': 8,
    'Pak Purwoadi': 9,
    'Pak Maryono': 10,
    'Pak Widodo': 11,
    'Pak Wirawan': 13,
    'Pak Basuki': 14
}

connection = {
    "Wirawan" : [("Widodo", 5),("Basuki", 4)],
    "Basuki" : [("Wirawan", 4),("Widodo",5),("Suwarno",4)],
    "Suwarno" : [("Basuki", 4),("Sutrisno",5),("Widodo", 6)],
    "Widodo" : [("Wirawan", 5),("Basuki",5),("Suwarno",6),("Sutrisno",5),("Sumanto",4)],
    "Sutrisno" : [("Suwarno",5),("Widodo",5),("Sumanto",7),("Handoko",5)],
    "Sumanto" : [("Widodo",4),("Sutrisno",7),("Handoko",7),("Jumali",3)],
    "Handoko" : [("Sutrisno",5),("Sumanto",7),("Jumali",5),("Sunarno",4),("Joko",6)],
    "Jumali" : [("Sumanto",3),("Handoko",5),("Maryono",2)],
    "Maryono" : [("Jumali",2),("Hadi",6)],
    "Sunarno" : [("Handoko",4),("Hadi",6),("Sumono",6)],
    "Joko" : [("Handoko",6),("Sumono",3)],
    "Hadi" : [("Maryono",6),("Sunarno",6),("Purwoadi",4)],
    "Purwoadi" : [("Hadi",4),("Sumono",4)],
    "Sumono" : [("Joko",3),("Sunarno",6),("Purwoadi",4)]
}


def dijkstra(graph, start, destination):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    visited = set()

    while len(visited) < len(graph):
        current_node = None
        current_distance = float('inf')

        for node in graph:
            if node not in visited and distances[node] < current_distance:
                current_distance = distances[node]
                current_node = node

        if current_node is None:
            break

        visited.add(current_node)

        for neighbor, weight in graph[current_node]:
            if neighbor not in visited:
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous_nodes[neighbor] = current_node

    path = []
    current_node = destination
    while current_node is not None:
        path.insert(0, current_node)
        current_node = previous_nodes[current_node]

    if path[0] != start:
        return None, float('inf')

    return path, distances[destination]


shortest_path_to_joko = dijkstra(connection, "Wirawan", "Joko")
print(f"The shortest distance from Wirawan to Joko is: {shortest_path_to_joko}")

shortest_path_to_maryono = dijkstra(connection, "Handoko", "Sumono")
print(f"The shortest distance from Wirawan to Maryono is: {shortest_path_to_maryono}")



