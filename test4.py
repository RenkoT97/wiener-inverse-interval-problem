import networkx as nx
import numpy as np
import matplotlib as mpl
import random as rd
import time
import math

#Za teste lahko spreminjaš argumente klicov funkcij naredi_drevesa in optimum

start_time = time.time()

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

def naredi_drevesa(st_vozlisc, st_grafov):
    sez = []
    for i in range(st_grafov):
        sez.append(nakljucno_drevo(st_vozlisc))
    return sez

#Spremeni samo seznam, ki pove stevila vozlisc
drevesa = naredi_drevesa(17,10)

def najkrajse_poti(graf):
    return list(nx.all_pairs_shortest_path(graf))
#seznam vsot poti iz posameznega vozlišča

def seznam_vsot_poti(drevesa):
    s = []
    for sez_poti in [najkrajse_poti(drevo) for drevo in drevesa]:
        sez = []
        for vozlisce_s_potmi in sez_poti:
            vsota = sum(len(vozlisce_s_potmi[1][kljuc]) - 1 for kljuc in vozlisce_s_potmi[1])
            sez.append(vsota)
        s.append(sez)
    return s

vsote_poti = seznam_vsot_poti(drevesa)

def wienerjev_index_s_potmi(seznam_vsot_poti):
    return [sum(vsote)/2 for vsote in seznam_vsot_poti]

wienerjev_index = wienerjev_index_s_potmi(vsote_poti)

#M je množica vseh dreves z n+1 vozlišči, ki jih dobimo, če drevesu T dodamo list

def mnozica_dreves_z_dodanim_listom(drevesa, vsote_poti, wienerjev_index):
    #če želimo videti nova drevesa, odkomentiramo dele z M: zakomentirano, ker nepotrebno in tako dela hitreje
    sez = []
    ind = []
    i = 0
    for drevo in drevesa:
        #M = []
        I = set()
        n = nx.number_of_nodes(drevo)
        osnovni_index = wienerjev_index[i]
        i += 1
        j = 0
        for vozlisce in drevo:
            #T = drevo.copy()
            #T.add_node(n+1)
            #T.add_edge(vozlisce,n+1)
            #M.append(T)
            poti_iz_vozlisca = vsote_poti[i-1][j]
            index = osnovni_index + poti_iz_vozlisca + n
            I.add(index)
            j += 1
        #sez.append(M)
        ind.append(I)
    return sez, ind
nova_drevesa, indeksi_novih_dreves = mnozica_dreves_z_dodanim_listom(drevesa, vsote_poti, wienerjev_index)

def moc_mnozic_indeksov_naddreves_dreves(indeksi_poddreves):
    return [len(indeksi) for indeksi in indeksi_poddreves]

moc_mnozic_indeksov_za_drevesa = moc_mnozic_indeksov_naddreves_dreves(indeksi_novih_dreves)
print(moc_mnozic_indeksov_za_drevesa)

def narisi(drevo):
    slika = nx.draw(drevo,node_size=4)
    mpl.pyplot.show()
    return None

def seznam_sosedov(graf):
    return[[i, list(graf.neighbors(i))] for i in graf]

def listi(drevo):
    return [l[0] for l in seznam_sosedov(drevo) if len(l[1])==1]

def vozlisca(drevo):
    return [i for i in drevo]

def sosed(drevo):
    novo_drevo = drevo.copy()
    l = rd.choice(listi(novo_drevo))
    vozlisce = rd.choice(vozlisca(drevo))
    novo_drevo.remove_node(l)
    novo_drevo.add_node(l)
    novo_drevo.add_edge(l, vozlisce)
    novo_drevo = [novo_drevo]
    vs_poti = seznam_vsot_poti(novo_drevo)
    w = wienerjev_index_s_potmi(vs_poti)
    poddrevesa, indeksi_poddreves = mnozica_dreves_z_dodanim_listom(novo_drevo, vs_poti,w)
    moc_mnozice = moc_mnozic_indeksov_naddreves_dreves(indeksi_poddreves)
    return novo_drevo[0], moc_mnozice[0]

def P(e,en,t):
    #po Kirkpatricku
    if en < e:
        return 1
    else:
        return math.e ** ((e - en) / t)
    
def simulated_annealing(mesto_drevesa_v_seznamu_dreves, kmax = 10, emax = 1, zacetna_temperatura = 100):
    #kmax največje število korakov, emax zadovoljiv rezultat
    stanje = drevesa[mesto_drevesa_v_seznamu_dreves]
    energija = moc_mnozic_indeksov_za_drevesa[mesto_drevesa_v_seznamu_dreves]
    najboljse_stanje = stanje
    najboljsa_energija = energija
    k = 0
    while k < kmax and energija > emax:
        temperatura = zacetna_temperatura / math.log(k+1.1)
        novo_stanje, nova_energija = sosed(stanje)
        if P(energija, nova_energija, temperatura) > rd.random():
             stanje = novo_stanje
             energija = nova_energija
        if nova_energija < najboljsa_energija:
             najboljse_stanje = novo_stanje
             najboljsa_energija = nova_energija
        k += 1   
    return najboljse_stanje, najboljsa_energija

def optimum(drevesa, kmax = 3, emax = 1, zacetna_temperatura = 10):
    sez_optimumov = [simulated_annealing(i, kmax, emax, zacetna_temperatura) for i in range(len(drevesa))]
    print(sez_optimumov) #test
    sez_moci = [el[1] for el in sez_optimumov]
    return sez_optimumov[np.argmin(sez_moci)]

optimalno_drevo, optimalna_moc_mnozice = optimum(drevesa)
print(optimalna_moc_mnozice)

print("%s seconds" % (time.time() - start_time))
