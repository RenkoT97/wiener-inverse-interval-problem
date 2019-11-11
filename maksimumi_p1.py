import networkx as nx
import numpy as np
import matplotlib as mpl
import random as rd
import time
import math

start_time = time.time()

n = 100

def prilagojeno_drevo(n):
    graf = nx.Graph()
    graf.add_nodes_from([i for i in range(n)])
    st = rd.randint(8 * n // 10, 95 * n // 100)
    nx.add_path(graf, [i for i in range(st)])
    sez = [i for i in range(st,n)]
    rd.shuffle(sez)
    sez2 = [i for i in range(st)]
    while sez:
        a = sez.pop()
        b = rd.choice(sez2)
        sez2.append(a)
        graf.add_edge(a,b)
    return graf       

graf = prilagojeno_drevo(n)

def moc_mnozice_novih_indeksov(graf):
    n = len(graf)
    osnovni_index = nx.wiener_index(graf)
    najkrajse_poti = nx.all_pairs_shortest_path(graf)
    I = set()
    for i in range(n):
        vozlisce, slovar_poti = next(najkrajse_poti)
        vsota_poti_iz_vozlisca = sum(len(slovar_poti[kljuc]) for kljuc in slovar_poti)
        nov_index = osnovni_index + vsota_poti_iz_vozlisca + n
        I.add(int(nov_index))
    return len(I)

moc_mnozice_novih_indeksov(graf)

def narisi(drevo):
    slika = nx.draw(drevo,node_size=4)
    mpl.pyplot.show()
    return None

def seznam_sosedov(graf):
    return[[i, list(graf.neighbors(i))] for i in graf]

def listi(drevo):
    return [l[0] for l in seznam_sosedov(drevo) if len(l[1]) == 1]

def vozlisca(drevo):
    return [i for i in drevo]

def sosed(drevo):
    novo_drevo = drevo.copy()
    l = rd.choice(listi(novo_drevo))
    vozlisce = rd.choice(vozlisca(drevo))
    novo_drevo.remove_node(l)
    novo_drevo.add_node(l)
    novo_drevo.add_edge(l, vozlisce)
    I = moc_mnozice_novih_indeksov(novo_drevo)
    return novo_drevo, I

def P(e,en,t):
    #po Kirkpatricku
    if en < e:
        return 1
    else:
        return math.e ** ((e - en) / t)
    
def simulated_annealing(drevo, kmax, emax, zacetna_temperatura = 100):
    #kmax največje število korakov, emax zadovoljiv rezultat
    stanje = drevo
    energija = moc_mnozice_novih_indeksov(drevo)
    najboljse_stanje = stanje
    najboljsa_energija = energija
    k = 0
    while k < kmax and energija < emax:
        temperatura = zacetna_temperatura / math.log(k+1.1)
        novo_stanje, nova_energija = sosed(stanje)
        if P(energija, nova_energija, temperatura) > rd.random():
             stanje = novo_stanje
             energija = nova_energija
        if nova_energija > najboljsa_energija:
             najboljse_stanje = novo_stanje
             najboljsa_energija = nova_energija
        k += 1   
    return najboljse_stanje, najboljsa_energija

def ozji_izbor_dreves(st_vozlisc, st_dreves = 10):
    sez_dreves = [prilagojeno_drevo(n) for i in range(st_dreves)]
    moc_mnozic_indeksov_za_drevesa = [moc_mnozice_novih_indeksov(drevo) for drevo in sez_dreves]
    k = 4 * st_dreves // 5
    while k > 0:
        k -= 1
        i = np.argmin(moc_mnozic_indeksov_za_drevesa)
        del sez_dreves[i]
        del moc_mnozic_indeksov_za_drevesa[i]
    return sez_dreves, moc_mnozic_indeksov_za_drevesa

drevesa, moc_mnozic_indeksov_za_drevesa = ozji_izbor_dreves(n, 10)
print(drevesa)#test
print(moc_mnozic_indeksov_za_drevesa)

def maximum(drevesa, kmax = 10, emax = n, zacetna_temperatura = 100):
    sez_maximumov = [simulated_annealing(i, kmax, emax, zacetna_temperatura) for i in drevesa]
    print(sez_maximumov) #test
    sez_moci = [el[1] for el in sez_maximumov]
    print(sez_moci) #test
    return sez_maximumov[np.argmax(sez_moci)]

max_drevo, max_moc_mnozice = maximum(drevesa)
print(max_moc_mnozice)

print("%s seconds" % (time.time() - start_time))

narisi(max_drevo)
