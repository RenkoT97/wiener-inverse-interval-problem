import networkx as nx
import numpy as np
import matplotlib as mpl

n = 5

drevesa_reda_n = nx.nonisomorphic_trees(n, create='graph')
sez = []
for drevo in drevesa_reda_n:
    sez.append(drevo)

'''
Ne vem, zakaj list(graf.neighbors(i)) ne dela. V drugem filu dela. Sicer
bi moral že graf.neighbors(i) vrniti list, a ga ne. Mislim, da bo ostalo
pravilno delovalo (ampak zelo počasi).
'''

def seznam_sosedov(graf):
    return[[i, list(graf.neighbors(i))] for i in graf]

def listi(drevo):
    return  [l[0] for l in seznam_sosedov(drevo) if len(l[1])==1]

novi = []
for T in sez:
    w = nx.wiener_index(T, weight=None)
    for list in listi(T):
        for vozlisce in T:
            G = T.copy()
            G.remove_node(list)
            G.add_node(list)
            G.add_edge(list,vozlisce)
            v = nx.wiener_index(G, weight=None)
            if abs(w-v)==1:
                novi.append(G)

print(novi)

D = np.argmax(nx.diameter())
