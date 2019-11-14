import p1_vecji_grafi as vg
import time

start_time = time.time()

def shrani_resitve(velikosti_grafov, kmax, st_dreves_za_odstranitev, st_dreves_za_izbiro):
    #v i-tem poteku zanke naredimo st_dreves_za_izbiro dreves velikosti števila na i-tem mestu
    #seznama ali nabora velikosti_grafov, iz teh izberemo (st_dreves_za_izbiro - st_dreves_za_odstranitev)
    #dreves, na katerih bomo izvajali ohlajanje
    for i in velikosti_grafov:
        drevesa, moc_mnozic_indeksov_za_drevesa = vg.ozji_izbor_dreves(i, st_dreves_za_odstranitev, st_dreves_za_izbiro)
        max_drevo, max_moc_mnozice = vg.maximum(drevesa, kmax, i)
        vg.slika(max_drevo, i, max_moc_mnozice)
        print(max_moc_mnozice)
    return None

shrani_resitve([50], 50, 8, 10)

print("%s seconds" % (time.time() - start_time))
