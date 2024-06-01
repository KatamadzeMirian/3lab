import networkx as nx

G = nx.erdos_renyi_graph(11, 0.15)
a = 0
# Вычисляем среднее по формуле из презентации
average_formula = (11 - 1) * 0.15

for n in G.nodes():
    a += G.degree(n)

# Вычисляем среднее по результату цикла
average_by_cycle = float(a) / len(G.nodes())