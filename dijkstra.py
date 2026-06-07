import networkx as nx
import matplotlib.pyplot as plt
import random

# Creazione del grafo
# '[3] * 15' crea una lista di quindici 3. Significa: 15 nodi con grado di ingresso e uscita pari a 3.
G = nx.directed_havel_hakimi_graph([3] * 15, [3] * 15, create_using=None)

for e in G.edges():
    # e[0] è il nodo di partenza, e[1] è il nodo di arrivo dell'arco e.
    # Assegniamo a quell'arco un peso casuale ('weight') compreso tra 1 e 9.
    G[e[0]][e[1]]['weight'] = random.randrange(1,10)

print(G.nodes())
print(G.edges())

# Trova e stampa la sequenza di nodi del percorso più breve dal nodo 0 al nodo 8
print(nx.dijkstra_path(G, 0, 8))

# Calcola e stampa la SOMMA dei pesi del percorso più breve dal nodo 0 al nodo 7
print(nx.dijkstra_path_length(G, 0, 7))

# Salviamo il percorso da 0 a 7 in una variabile (restituisce una lista di nodi, es: [0, 4, 12, 7])
optpath = nx.dijkstra_path(G, 0, 7)

# Questo blocco serve a trasformare la lista di nodi in una lista di "archi pesati"
optedges = []
for i in range(0, len(optpath)-1):
    optedges.append([optpath[i], optpath[i+1],  G[optpath[i]][optpath[i+1]]['weight']])

# Plotting
pos = nx.spring_layout(G) # pos = nx.nx_agraph.graphviz_layout(G)
nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels = labels)
nx.draw_networkx_edges(G, pos, optedges, edge_color = "red")
plt.savefig("plot")
plt.show()