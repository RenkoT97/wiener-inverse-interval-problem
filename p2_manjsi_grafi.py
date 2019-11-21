import networkx as nx
import numpy as np
#import matplotlib as mpl
import time

start_time = time.time()

n = 8

def vsa_izomorfna_drevesa(n):
    drevesa_reda_n = nx.nonisomorphic_trees(n, create='graph')
    return list(drevesa_reda_n)

def seznam_sosedov(graf):
    return[[i, list(graf.neighbors(i))] for i in graf]

def listi(drevo):
    return  [l[0] for l in seznam_sosedov(drevo) if len(l[1])==1]

def ustrezna_drevesa(sez):
    #funkcija, ki iz seznama dreves pobere tista, ki se jim index spremeni za ena pri zamenjavi ene povezave pri listu
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
    return novi

def poisci_drevo_z_najvecjim_premerom(drevesa):
    if drevesa:
        diametri = [nx.diameter(el) for el in drevesa]
        m = np.argmax(diametri)
        D = drevesa[m]
        return D, diametri[m]
    else:
        print("D ne obstaja")
        return None

def slika(drevo, i, diam):
    #nx.draw(drevo,node_size=4)
    #mpl.pyplot.savefig('drevo{}diam{}.png'.format(i, diam), format = "PNG")
    #mpl.pyplot.close()
    return None

sez = vsa_izomorfna_drevesa(n)
drevesa = ustrezna_drevesa(sez)
iskano_drevo, diameter = poisci_drevo_z_najvecjim_premerom(drevesa)
slika(iskano_drevo, n, diameter)
print(diameter)

print("%s seconds" % (time.time() - start_time))
