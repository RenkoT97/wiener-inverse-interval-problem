import networkx as nx
import random as rd
import numpy as np
import matplotlib as mpl
import time

start_time = time.time()

def prvotni_graf(n):
    graf = nx.Graph()
    nx.add_path(graf, [i for i in range(n)])
    return graf

def slika(drevo, i, diam):
    nx.draw(drevo,node_size=4)
    mpl.pyplot.savefig('drevo{}diam{}.png'.format(i, diam), format = "PNG")
    mpl.pyplot.close()
    print("Drevo je najdeno.")
    return None

def seznam_sosedov(graf):
    return[[i, list(graf.neighbors(i))] for i in graf]

def listi(drevo):
    return  [l[0] for l in seznam_sosedov(drevo) if len(l[1])==1]

def wiener_poti(n):
    sez = [sum(i for i in range(n))]
    k = n-1
    for i in range(1,n):
        sez.append(sez[i-1]-k)
        k-=1
    return sum(sez)
        
def iskanje(k, n):
    #k število korakov, n število vozlišč
    graf = prvotni_graf(n)
    w_star = wiener_poti(n)
    j = 0
    while j < k:
        j += 1
        lis = rd.choice(listi(graf))
        potilis = nx.shortest_path(graf, source = lis)
        vsotalis = sum([(len(potilis[kljuc])-1) for kljuc in potilis])
        vozlisca = list(graf)
        vozlisca.remove(lis)
        v = rd.choice(vozlisca)
        potiv = nx.shortest_path(graf, source = v)
        vsotav = sum([len(potiv[kljuc]) - 1 for kljuc in potiv])
        vlis = nx.shortest_path(graf, source = v, target = lis)
        dolzinavlis = len(vlis) - 1
        graf.remove_node(lis)
        graf.add_node(lis)
        graf.add_edge(lis,v)
        w_nov = w_star - 1 + vsotav - vsotalis + n - dolzinavlis
        if abs(w_nov - w_star) == 1:
            print(w_nov, w_star)
            return slika(graf, len(graf), nx.diameter(graf))
        w_star = w_nov
    print("Ne najdem grafa.")
    return None

iskanje(1000000, 100)

print("%s seconds" % (time.time() - start_time))
