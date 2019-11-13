import p1_vecji_grafi as vg
import time

start_time = time.time()

def shrani_resitve(velikosti_grafov, kmax):
    for i in velikosti_grafov:
        drevesa, moc_mnozic_indeksov_za_drevesa = vg.ozji_izbor_dreves(i, 10)
        max_drevo, max_moc_mnozice = vg.maximum(drevesa, kmax, i)
        vg.slika(max_drevo, i, max_moc_mnozice)
        print(max_moc_mnozice)
    return None

shrani_resitve([100], 20)

print("%s seconds" % (time.time() - start_time))
