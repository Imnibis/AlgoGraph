import networkx as nx
import matplotlib.pyplot as plt

# Étape 1: Créer un petit graphe aléatoire
def create_random_graph(num_nodes, num_edges):
    G = nx.gnm_random_graph(num_nodes, num_edges)
    while not nx.is_connected(G):
        G = nx.gnm_random_graph(num_nodes, num_edges)
    return G

# Étape 2: Trouver un chemin eulérien
def find_eulerian_path(G):
    if nx.is_eulerian(G):
        return list(nx.eulerian_circuit(G))
    elif nx.has_eulerian_path(G):
        return list(nx.eulerian_path(G))
    return None

# Étape 3: Construire le graphe linéaire
def create_line_graph(G):
    return nx.line_graph(G)

# Étape 4: Trouver un chemin hamiltonien (utilisation de l'algorithme de recherche de chemin hamiltonien)
def find_hamiltonian_path(G):
    def backtrack(path, visited):
        if len(path) == len(G):
            return path
        current_node = path[-1]
        for neighbor in G.neighbors(current_node):
            if neighbor not in visited:
                visited.add(neighbor)
                result = backtrack(path + [neighbor], visited)
                if result:
                    return result
                visited.remove(neighbor)
        return None

    for start_node in G.nodes:
        path = backtrack([start_node], {start_node})
        if path:
            return path
    return None

# Étape 5: Sauvegarder les graphes et les chemins trouvés dans un fichier PDF
def save_graph(G, path=None, filename='graph.pdf', title='Graph'):
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
    if path:
        edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', width=2)
    plt.title(title)
    plt.savefig(filename)
    plt.close()

# Exemple d'utilisation
num_nodes = 5
num_edges = 7
G = create_random_graph(num_nodes, num_edges)

# Trouver et sauvegarder le chemin eulérien
eulerian_path = find_eulerian_path(G)
print("Eulerian Path:", eulerian_path)
save_graph(G, eulerian_path, filename='original_graph_with_eulerian_path.pdf', title='Original Graph with Eulerian Path')

# Créer et sauvegarder le graphe linéaire
line_graph = create_line_graph(G)
save_graph(line_graph, filename='line_graph.pdf', title='Line Graph')

# Trouver et sauvegarder le chemin hamiltonien dans le graphe linéaire
hamiltonian_path = find_hamiltonian_path(line_graph)
print("Hamiltonian Path in Line Graph:", hamiltonian_path)
save_graph(line_graph, hamiltonian_path, filename='line_graph_with_hamiltonian_path.pdf', title='Line Graph with Hamiltonian Path')
