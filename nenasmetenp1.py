import networkx as nx
import numpy as np
import matplotlib as mpl
import random as rd
import time

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
drevesa = naredi_drevesa(10,10)

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
    #če želimo videti nova drevesa, odkomentiramo dele z M
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

'''
def poisci_max_in_min(moc_mnozic_indeksov_za_drevesa):
    return(max(moc_mnozic_indeksov_za_drevesa), np.argmax(moc_mnozic_indeksov_za_drevesa)), (min(moc_mnozic_indeksov_za_drevesa), np.argmin(moc_mnozic_indeksov_za_drevesa))

maxd, mind = poisci_max_in_min(moc_mnozic_indeksov_za_drevesa)

maxdrevo = drevesa[maxd[1]]
najkrajse_poti_maxdrevesa = najkrajse_poti_v_drevesih[maxd[0]]
mindrevo = drevesa[mind[1]]
najkrajse_poti_mindrevesa = najkrajse_poti_v_drevesih[mind[0]]
'''

def sosed(drevo):
    G = drevo.copy()
    
    G.remove_node(lis)
    G.add_node(lis)
    G.add_edge(lis,vozlisce)
    
    novo_drevo = [drevo]
    vs_poti = seznam_vsot_poti(novo_drevo)
    w = wienerjev_index_s_potmi(vs_poti)
    poddrevesa, indeksi_poddreves = mnozica_dreves_z_dodanim_listom(novo_drevo, vs_poti,w)
    moc_mnozice = moc_mnozic_indeksov_naddreves_dreves(indeksi_poddreves)
    return novo_drevo[0], moc_mnozice[0]

def E(s):
    pass
    
def simulated_annealing(mesto_drevesa_v_seznamu_dreves):
    stanje = moc_mnozic_indeksov_za_drevesa[mesto_drevesa_v_seznamu_dreves]
    energija = E(s)
    najboljse_stanje = stanje
    najboljsa_energija = energija
    drevo = drevesa[mesto_drevesa_v_seznamu_dreves]
    k = 0
    while k < kmax and e > emax:
        temperatura = '?'
        novo_drevo, novo_stanje = sosed(drevo)
        nova_energija = E(novo_stanje)
        if P(energija, nova_energija, temperatura > random():
             stanje = novo_stanje, drevo = novo_drevo, najboljsa_energija = nova_energija
        if nova_energija < najboljsa_energija:
             najboljse_stanje = novo_stanje, najboljse_drevo = novo_drevo, najboljsa_energija = nova_energija
             k += 1   
    return najboljse_stanje, najboljse_drevo

def genetski_algoritem(drevesa):
    pass
    
print("%s seconds" % (time.time() - start_time))
