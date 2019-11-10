import networkx as nx
import matplotlib as mpl

def narisi(drevo):
    slika = nx.draw(drevo,node_size=4)
    mpl.pyplot.show()
    return None

def mindrevolihalisod(n):
    return nx.star_graph(n-1)

def mindrevosodg(n):
    k = (n-2)//2
    zvezda1 = nx.star_graph(k-1)
    zvezda2 = nx.star_graph(k-1)
    graf = nx.Graph()
    graf.add_edges_from(zvezda1.edges())#zvezda2.edges())
    graf.add_edges_from(zvezda2.edges())
    return nx.disjoint_union(zvezda1, zvezda1)

def mindrevosod(n):
    graf = nx.Graph()
    graf.add_nodes_from([i for i in range(n)])
    graf.add_edge(0,n//2)
    sez1 = [i for i in range(n//2)]
    sez2 = [i for i in range(n//2,n)]
    nx.add_star(graf, sez1)
    nx.add_star(graf, sez2)
    return graf

def optmindrevo(n):
    if n / 2 == n // 2:
        return mindrevolihalisod(n), mindrevosod(n)
    else:
        return mindrevolihalisod(n)

drevo = optmindrevo(16)[1]
narisi(drevo)

#Očitno je moč množice wienerjevih indeksov dreves, nastalih iz drevesa
#z dodajanjem lista, največ 2, saj dobimo natanko dve različni novi drevesi.
#Misliva, da je to optimalna rešitev za poljubno drevo.
