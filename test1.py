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

def naredi_drevesa(sez_st_vozlisc):
    #argument je seznam, ki ima za elemente željena števila vozlišč grafov, ki jih bomo zgenerirali
    sez = []
    for st_vozlisc in sez_st_vozlisc:
        sez.append(nakljucno_drevo(st_vozlisc))
    return sez
    
'''
Dolg način: vsa drevesa z istim številom vozlišč

drevesa_reda_n = nx.nonisomorphic_trees(n, create='graph')

drevesa = []
for drevo in drevesa_reda_n:
    drevesa.append(drevo)
'''
'''
Način z vgrajeno funkcijo za delanje dreves: dobivamo čudna drevesa

def naredi_drevesa(sez_st_vozlisc):
    #argument je seznam, ki ima za elemente željena števila vozlišč grafov, ki jih bomo zgenerirali
    sez = []
    for i in range(len(sez_st_vozlisc)):
        n = sez_st_vozlisc.pop()
        try:
            sez.append(nx.random_powerlaw_tree(n, gamma=3, seed=None, tries=100000))
        except nx.exception.NetworkXError:
            pass
    return sez
'''
#Spremeni samo seznam, ki je argument funkcije naredi_drevesa
drevesa = naredi_drevesa([10])
st = len(drevesa)

def najkrajse_poti(graf):
    return list(nx.all_pairs_shortest_path(graf))
najkrajse_poti_v_drevesih = [najkrajse_poti(drevo) for drevo in drevesa]
#seznam vsot poti iz posameznega vozlišča

def seznam_vsot_poti(graf):
    s = []
    for sez_poti in najkrajse_poti_v_drevesih:
        sez = []
        for vozlisce_s_potmi in sez_poti:
            vsota = sum(len(vozlisce_s_potmi[1][kljuc]) - 1 for kljuc in vozlisce_s_potmi[1])
            sez.append(vsota)
        s.append(sez)
    return s
vsote_poti = seznam_vsot_poti(drevesa)

def wienerjev_index_s_potmi(grafi):
    return [sum(vsote)/2 for vsote in grafi]
wienerjev_index_s_potmi = wienerjev_index_s_potmi(vsote_poti)

'''
def wienerjev_index(drevesa):
    return [nx.wiener_index(drevo, weight=None) for drevo in drevesa]
wienerjevi_indeksi = wienerjev_index(drevesa)
'''

#M je množica vseh dreves z n+1 vozlišči, ki jih dobimo, če drevesu T dodamo list

def mnozica_dreves_z_dodanim_listom(drevesa):
    sez = []
    ind = []
    i = 0
    for drevo in drevesa:
        M = []
        I = []
        n = nx.number_of_nodes(drevo)
        osnovni_index = wienerjev_index_s_potmi[i]
        i += 1
        j = 0
        for vozlisce in drevo:
            T = drevo.copy()
            T.add_node(n+1)
            T.add_edge(vozlisce,n+1)
            M.append(T)
            poti_iz_vozlisca = vsote_poti[i-1][j]
            index = osnovni_index + poti_iz_vozlisca + n
            I.append(index)
            j += 1
        sez.append(M)
        ind.append(I)
    return sez, ind
nova_drevesa, indeksi_novih_dreves = mnozica_dreves_z_dodanim_listom(drevesa)

mnozica_indeksov = set(indeksi_novih_dreves)
moc_mnozice_indeksov = len(mnozica_indeksov)
'''
def mnozica_dreves_z_dodanim_listom(drevesa):
    sez = []
    for drevo in drevesa:
        M = []
        n = nx.number_of_nodes(drevo)
        for vozlisce in drevo:
            T = drevo.copy()
            T.add_node(n+1)
            T.add_edge(vozlisce,n+1)
            M.append(T)
        sez.append(M)
    return sez
nova_drevesa = mnozica_dreves_z_dodanim_listom(drevesa)

wienerjevi indeksi dreves iz M
def indeksi_novih_dreves(nova_drevesa):
    return [[nx.wiener_index(T, weight = None) for T in M] for M in nova_drevesa]
indeksi_novih_dreves = indeksi_novih_dreves(nova_drevesa)
'''

'''
def mesta_dreves(indeksi_dreves):
    return [np.argmin(s) for s in indeksi_dreves]
    #argmin->argmax za drugi vidik
mesta_dreves = mesta_dreves(indeksi_novih_dreves)

def iskana_drevesa(mesta, drevesa):
    D = []
    for i in range(len(drevesa)):
        sez = drevesa[i]
        mesto = mesta[i]
        D.append(sez[mesto])
    return D
#D so taka drevesa iz množice M, da je njihov wienerjev indeks najmanjši (največji)
iskana_drevesa = iskana_drevesa(mesta_dreves, nova_drevesa)
'''

slika = nx.draw(drevesa[0],node_size=4)
mpl.pyplot.show()

print("%s seconds" % (time.time() - start_time))
