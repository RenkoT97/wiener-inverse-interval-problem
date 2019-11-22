import p1_manjsi_grafi as mg
import json
import networkx as nx
import matplotlib as mpl


def slika(drevo, opt, i, wm):
    nx.draw(drevo,node_size=4)
    mpl.pyplot.savefig('drevo{}{}{}.png'.format(i,opt,wm), format = "PNG")
    mpl.pyplot.close()
    return None

def seznam_sosedov(graf):
    return[[i, list(graf.neighbors(i))] for i in graf]

def zapisi_resitve(n):
    with open("p1-eksaktni.json", "w", encoding = "utf-8") as dat:
        sez = []
        for i in range(2,n):
            import p1_manjsi_grafi
            drevesa_reda_n = nx.nonisomorphic_trees(i, create='graph')
            drevesa = [drevo for drevo in drevesa_reda_n]
            najkrajse_poti_v_drevesih = [mg.najkrajse_poti(drevo) for drevo in drevesa]
            vsote_poti = mg.seznam_vsot_poti(najkrajse_poti_v_drevesih)
            wienerjev_index_s_potmi = mg.wienerjev_index_s_potmi(vsote_poti)
            nova_drevesa, indeksi_novih_dreves = mg.mnozica_dreves_z_dodanim_listom(drevesa, vsote_poti, wienerjev_index_s_potmi)
            moci = mg.moc_mnozic_indeksov_naddreves_dreves(indeksi_novih_dreves)
            mesta_dreves_min = mg.mesta_dreves_min(moci)
            mesta_dreves_max = mg.mesta_dreves_max(moci)
            sezmin, najmanjsa_moc, sezmax, najvecja_moc  = mg.iskana_drevesa(mesta_dreves_max, mesta_dreves_min, drevesa, moci)
            smax = [seznam_sosedov(graf) for graf in sezmax]
            smin = [seznam_sosedov(graf) for graf in sezmin]
            slika(sezmin[0], "min", i, najmanjsa_moc)
            slika(sezmax[0], "max", i, najvecja_moc)
            podatki = {"n": i, "max": najvecja_moc, "min": najmanjsa_moc, "seznam dreves maksimuma": smax, "seznam dreves minimuma": smin}
            sez.append(podatki)
        json.dump(sez,dat)
    return None

zapisi_resitve(17)

def preberi_napisano():
    with open("p1-eksaktni.json", "r+", encoding = "utf-8") as dat:
        vsebina = json.load(dat)
        print(vsebina)
    return None

#preberi_napisano()

     
