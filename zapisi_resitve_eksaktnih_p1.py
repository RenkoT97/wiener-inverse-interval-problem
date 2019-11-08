import p1_manjsi_grafi as mg
import networkx as nx

def zapisi_resitve(n):
    with open("p1-eksaktni.text", "w+", encoding = "utf-8") as dat:
        for i in range(4,n):
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
            iskana_drevesa = mg.iskana_drevesa(mesta_dreves_max, mesta_dreves_min, drevesa, moci)
            podatki = ""
            dat.write(podatki)
    return None

zapisi_resitve(5)
     
