from animali_api import scarica_url_cani, scarica_url_gatti
from animali_download import scarica_tutte
from animali_cartella import crea_cartella, elenca_immagini
from animali_galleria import ordina_alfabeticamente, stampa_galleria

CARTELLA = "immagini_animali"
QUANTE = 5

if __name__ == "__main__":
    print("=== GALLERIA ANIMALI ===")
    print()

    # STEP 1 - Crea la cartella
    crea_cartella(CARTELLA)

    # STEP 2 - Recupera gli URL delle immagini
    print("Recupero URL cani...")
    url_cani = scarica_url_cani(QUANTE)

    print("Recupero URL gatti...")
    url_gatti = scarica_url_gatti(QUANTE)

    # STEP 3 - Scarica le immagini
    print()
    print("Download immagini cani...")
    scarica_tutte(url_cani, CARTELLA, "cane")

    print("Download immagini gatti...")
    scarica_tutte(url_gatti, CARTELLA, "gatto")

    # STEP 4 - Legge i file presenti nella cartella
    print()
    file_presenti = elenca_immagini(CARTELLA)

    # STEP 5 - Ordina e stampa la galleria
    file_ordinati = ordina_alfabeticamente(file_presenti)
    stampa_galleria(file_ordinati, CARTELLA)