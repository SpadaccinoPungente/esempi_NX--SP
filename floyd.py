import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()

# Aggiunge gli archi tutti in una volta definendo: (nodo_partenza, nodo_arrivo, peso)
# Nota l'arco (2, 3, -3) con peso negativo.
G.add_weighted_edges_from([(0, 1, 5), (1, 2, 2), (2, 3, -3), (1, 3, 10), (3, 2, 8)])

# Esegue l'algoritmo. Restituisce un dizionario di dizionari.
# fw[nodo_A][nodo_B] conterrà la distanza minima tra il nodo A e il nodo B.
fw = nx.floyd_warshall(G, weight="weight")

# Questo ciclo serve a stampare i risultati in modo leggibile nel terminale
for a, b in fw.items():
    print(f"Nodo {a}: {dict(b)}")  # Stampa il nodo di partenza e un dizionario con le distanze verso tutti gli altri nodi

# Questa è una "dictionary comprehension". Fa la stessa identica cosa del ciclo sopra,
# ma compatta tutto in un unico grande dizionario 'results' e lo stampa.
results = {a: dict(b) for a, b in fw.items()}
print(f"Con dict comprehension: \n{results}")

# Plotting
pos = nx.planar_layout(G) # pos = nx.nx_agraph.graphviz_layout(G)
nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels = labels)
plt.savefig("plot")
plt.show()