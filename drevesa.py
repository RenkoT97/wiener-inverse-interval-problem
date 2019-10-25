import networkx as nx
import random as rd
import matplotlib.pyplot as plt
from timeit import timeit

def nakljucno_drevo(n):
    sez = [i for i in range(n)]
    rd.shuffle(sez)
    g = nx.Graph()
    g.add_nodes_from(sez)
    sez2 = []
    sez2.append(sez.pop())
    while sez:
        a = sez.pop()
        b = rd.choice(sez2)
        sez2.append(a)
        g.add_edge(a, b)
    return g

def simpleDraw(G):
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=5)
    nx.draw_networkx_edges(G, pos)
    plt.show()


poskusi = 1000
a = map(
    lambda i: timeit(
        lambda i=i: nakljucno_drevo(i),number=1),
        range(1, poskusi)
    )
plt.plot(range(1, poskusi), list(a))
plt.show()

