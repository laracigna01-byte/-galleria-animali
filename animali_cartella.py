import os


def crea_cartella(percorso):
    esisteva_gia = os.path.exists(percorso)

    os.makedirs(percorso, exist_ok=True)

    if esisteva_gia:
        print(f"Cartella già esistente: {percorso}")
    else:
        print(f"Cartella creata: {percorso}")


def elenca_immagini(cartella):
    tutti_i_file = os.listdir(cartella)

    immagini = []
    for nome_file in tutti_i_file:
        nome_lower = nome_file.lower()

        if nome_lower.endswith(".jpg") or nome_lower.endswith(".jpeg") or nome_lower.endswith(".png"):
            immagini.append(nome_file)

    print(f"Trovate {len(immagini)} immagini in {cartella}")
    return immagini