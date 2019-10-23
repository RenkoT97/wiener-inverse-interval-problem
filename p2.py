import networkx as nx
import numpy as np
import matplotlib as mpl  ## Darjan comment


n = 10

drevesa_reda_n = nx.nonisomorphic_trees(n, create='graph')
sez = []
for drevo in drevesa_reda_n:
    sez.append(drevo)

def seznam_sosedov(graf):
    return[[i, list(graf.neighbors(i))] for i in graf]

def listi(drevo):
    return  [l[0] for l in seznam_sosedov(drevo) if len(l[1])==1]

novi = []
for T in sez:
    w = nx.wiener_index(T, weight=None)
    for lis in listi(T):
        for vozlisce in T:
            G = T.copy()
            G.remove_node(lis)
            G.add_node(lis)
            G.add_edge(lis,vozlisce)
            v = nx.wiener_index(G, weight=None)
            if abs(w-v)==1:
                novi.append(G)

# "novi" je seznam dreves, ki ustrezajo kriteriju točke P2 (sprememba Wien. ind. za +- 1)

if novi:
    di_novi = [nx.diameter(el) for el in novi]
    m = np.argmax(di_novi)
    D = novi[m]
else:
    print("D ne obstaja")
