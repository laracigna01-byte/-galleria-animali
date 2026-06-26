import os
import requests


def scarica_immagine(url, percorso):
    """
    Scarica un'immagine da un URL e la salva nel percorso indicato.
    Ritorna True se il salvataggio è riuscito, False altrimenti.
    """

    try:
        risposta = requests.get(url, timeout=15)

        if risposta.status_code == 200:
            with open(percorso, "wb") as file:
                file.write(risposta.content)

            dimensione_kb = len(risposta.content) / 1024
            print(f"  Salvato: {percorso} ({dimensione_kb:.1f} KB)")
            return True

        else:
            print(f"  Errore HTTP {risposta.status_code}: {url}")
            return False

    except requests.exceptions.ConnectionError:
        print(f"  Errore di connessione: {url}")
        return False


def scarica_tutte(url_list, cartella, prefisso):
    """
    Scarica tutte le immagini presenti nella lista.
    """

    salvate = 0

    os.makedirs(cartella, exist_ok=True)

    for numero, url in enumerate(url_list, start=1):

        nome_file_url = url.split("/")[-1]

        if "." in nome_file_url:
            estensione = nome_file_url.split(".")[-1]

            if "?" in estensione:
                estensione = estensione.split("?")[0]
        else:
            estensione = "jpg"

        nome_file = f"{prefisso}_{numero}.{estensione}"
        percorso = os.path.join(cartella, nome_file)

        if scarica_immagine(url, percorso):
            salvate += 1

    print()
    print(f"{salvate}/{len(url_list)} immagini salvate")

    return salvate


if __name__ == "__main__":

    url_test = [
        "https://cdn2.thecatapi.com/images/pb.jpg",
        "https://cdn2.thecatapi.com/images/9qu.jpg",
        "https://cdn2.thecatapi.com/images/arl.jpg"
    ]

    scarica_tutte(url_test, "test_download", "gatto")