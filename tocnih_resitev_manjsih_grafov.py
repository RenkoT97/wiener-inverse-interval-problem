import p1_manjsi_grafi as mg
import networkx as nx
import json

def seznam_sosedov(graf):
    return[[i, list(graf.neighbors(i))] for i in graf]

def zapisi_resitve(n):
    with open("p1-eksaktni.json", "w+", encoding = "utf-8") as dat:
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
            podatki = {'n': i, 'max': najvecja_moc, 'min': najmanjsa_moc, 'max-drevesa': smax, 'min-drevesa': smin}
            element = json.dumps(podatki)
            sez.append(element)
            #podatki = "Vozlišča: {}, maksimum: {}, minimum: {}, seznam dreves maksimuma {}, seznam dreves minimuma {} \n".format(i, najvecja_moc, najmanjsa_moc, sezmax, sezmin)
        json.dump(sez, dat)
    return None

zapisi_resitve(15)

def preberi_napisano(datoteka):
    with open("p1-eksaktni.json", "r+", encoding = "utf-8") as dat:
        vsebina = json.load(dat)
        print(vsebina)
    return None

preberi_napisano("p1-eksaktni.json")

     
