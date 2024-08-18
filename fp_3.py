import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Створення вагового графа
G = nx.Graph()
G.add_edge("A", "B", weight=1)
G.add_edge("A", "C", weight=4)
G.add_edge("B", "C", weight=2)
G.add_edge("B", "D", weight=5)
G.add_edge("C", "D", weight=1)
G.add_edge("D", "E", weight=3)

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    # Ініціалізація словника найкоротших шляхів
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0

    # Ініціалізація бінарної купи (піраміди) для оптимізації вибору вершин
    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue
        visited.add(current_vertex)

        # Прохід по сусідах поточної вершини
        for neighbor, attributes in graph[current_vertex].items():
            weight = attributes['weight']
            distance = current_distance + weight

            # Якщо знайдено коротший шлях, оновлюємо його
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths

# Використання алгоритму Дейкстри
shortest_paths = dijkstra(G, "A")
print("Найкоротші шляхи:", shortest_paths)

# Візуалізація графа
pos = nx.spring_layout(G)  # Positions for all nodes
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, width=2)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

plt.axis("off")
plt.show()