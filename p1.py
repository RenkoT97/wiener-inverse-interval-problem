import networkx as nx
import numpy as np
import matplotlib as mpl

## Darjan: comment i) import matplotlib, ii) slika&mpl.pyplot pod seznamom sosedov

n = 10

#1. način

drevesa_reda_n = nx.nonisomorphic_trees(n, create='graph')

#sez vsebuje vsa drevesa z n vozlišči
#za naključno drevo premešamo sez (sicer bi bil sez[0] drevo z dvema vozliščema stopnje 1 ter n-2 vozlišči stopnje 2 itn.)

sez = []
for drevo in drevesa_reda_n:
    sez.append(drevo)
np.random.shuffle(sez)

T = sez[0]       #naključno drevo z n vozlišči

'''
2. način

hitrejši (?) način za pridobitev drevesa z n vozlišči
slab, ker s številom vozlišč narašča število poskusov, ki jih potrebujemo, da dobimo drevo
velikokrat dobim graf z n-2 vozlišči stopnje 2 (?)

T = nx.random_powerlaw_tree(n, gamma=3, seed=None, tries=500)
'''

def seznam_sosedov(graf):
    return[[i, list(graf.neighbors(i))] for i in graf]      # Vrne [["zap. št. vozlišča"], ["zap. št. vseh sosedov tega vozlišča"]]

print(seznam_sosedov(T))
slika = nx.draw(T)
mpl.pyplot.show()

w = nx.wiener_index(T, weight=None)

def listi(drevo):
    return  [l[0] for l in seznam_sosedov(drevo) if len(l[1])==1]     # Če ima vozlišče samo 1 sosednje vozlišče (torej je list), zap. št. tega vozlišča dodamo med liste.

listi = listi(T)

#M je množica vseh dreves z n+1 vozlišči, ki jih dobimo, če drevesu T dodamo list

M = []
for v in T:
    H = T.copy()
    H.add_node(n+1)
    H.add_edge(v,n+1)
    M.append(H)
M_seznami = [seznam_sosedov(g) for g in M]

#wienerjevi indeksi dreves iz M

w_M = [nx.wiener_index(T, weight = None) for T in M]
mesto = np.argmin(w_M)

#D je iskano drevo, torej tako iz množice M, da je njegov wienerjev indeks najmanjši

D = M[mesto]


        
