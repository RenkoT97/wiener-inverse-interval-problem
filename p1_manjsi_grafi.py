import networkx as nx
import numpy as np
#import matplotlib as mpl
import random as rd

def najkrajse_poti(graf):
    return list(nx.all_pairs_shortest_path(graf))

def seznam_vsot_poti(najkrajse_poti_v_drevesih):
    s = []
    for sez_poti in najkrajse_poti_v_drevesih:
        sez = []
        for vozlisce_s_potmi in sez_poti:
            vsota = sum(len(vozlisce_s_potmi[1][kljuc]) - 1 for kljuc in vozlisce_s_potmi[1])
            sez.append(vsota)
        s.append(sez)
    return s

def wienerjev_index_s_potmi(grafi):
    return [sum(vsote)/2 for vsote in grafi]

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

def moc_mnozic_indeksov_naddreves_dreves(indeksi_poddreves):
    return [len(indeksi) for indeksi in indeksi_poddreves]

def mesta_dreves_max(moci):
    maksimumi = np.argwhere(moci == np.amax(moci))
    return list(maksimumi.flatten())

def mesta_dreves_min(moci):
    minimumi = np.argwhere(moci == np.amin(moci))
    return list(minimumi.flatten())

def iskana_drevesa(mesta_dreves_max, mesta_dreves_min, drevesa, moci):
    MAX = []
    MIN = []
    najmanjsa_moc = moci[mesta_dreves_min[0]]
    najvecja_moc = moci[mesta_dreves_max[0]]
    for i in mesta_dreves_min:
        MIN.append(drevesa[i])
    for i in mesta_dreves_max:
        MAX.append(drevesa[i])
    return MIN, najmanjsa_moc, MAX, najvecja_moc
