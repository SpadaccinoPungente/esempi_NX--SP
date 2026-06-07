import networkx as nx

g = nx.Graph()
g.add_edge(1, 2)  # peso dell'arco quando non specificato = 1 (??) -> default edge data=1
g.add_edge(2, 3, weight=0.9)  # specify edge data
print(g.edges(data=True))

elist = [(1, 2, 1), (2, 3, 1), (1, 4, 1), (4, 2, 1),
         ('a', 'b', 5.0), ('b', 'c', 3.0), ('a', 'c', 1.0), ('c', 'd', 7.3)]
g.add_weighted_edges_from(elist)
g.add_edge(2, 5, arbitraryAttr="foo")

print(g[2]) # stampa i vicini di 2
print("---------")
print(g['a']['b']) # stampa i dati dell'arco tra 'a' e 'b'
print("---------")
print('e' in g) # 'e' non è un nodo del grafo
print("---------")
for n in g:
    print(n) # stampa tutti i nodi
print("---------")
for nbr in g[2]:
    print(nbr) # stampa i vicini di 2
print("---------")
print(g[2][5]['arbitraryAttr']) # stampa il valore dell'attributo relativo all'arco tra 2 e 5
