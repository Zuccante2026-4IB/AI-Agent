# script main

# Ciao chiuqnue tu sia che sviluppa questo codice sono Alessio, sei pregato di inserire nel file requirements.txt tutte le librerie
# che intendi utilizzare e che non siano già presenti nell'interprete come default come ho fatto io per dimostrare (in questo caso
# beautifulsoap4 ovvero bs4 4 requests).
#
# Sei inoltre pregato di non usare l'intelligenza artificiale per sviluppare questo codice o in tal caso cerca di capirlo e 
# commentarlo a dovere per fare poi un test, inserisci il tag TEST o DEBUG in un commento sopra ai metodi ancora da testare, il tag
# prima del metodo FIXME se devi indicare che qualcosa deve essere sistemato oppure il tag TODO se devi indicare qualcosa ancora da fare
# (P.S. Non deve essere una scusa per lasciare ad altri il lavoro che non vuoi fare ;) )
#
# Buona fortuna a svilupapre il codice
# AlessioDiBattista (RustRello)
#
# Elimina il commento enorme che ho lasciato dopo averlo letto, serve solo per comunicazione <3

from bs4 import BeautifulSoup
import requests
import re

def normalize(word):
    """
    """
    word = word.lower()
    
    # rimuove accenti (opzionale ma consigliato)
    replacements = {
        "à": "a", "è": "e", "é": "e",
        "ì": "i", "ò": "o", "ù": "u"
    }
    for k, v in replacements.items():
        word = word.replace(k, v)

    # rimuove tutto tranne lettere
    word = re.sub(r"[^a-z\s]", "", word)

    # rimuove spazi (attacca tutto)
    word = word.replace(" ", "")

    return word


def extract_italian_words(html):
    soup = BeautifulSoup(html, "html.parser")
    results = set()

    for tag in soup.find_all("i", attrs={"lang": "it"}):
        text = tag.get_text().strip()

        # split varianti
        parts = re.split(r"/|\bor\b", text, flags=re.IGNORECASE)

        for part in parts:
            part = normalize(part)

            if part:
                results.add(part)

    return sorted(results)


# ==== USO ====
if __name__ == "__main__":
    with open("input.html", "r", encoding="utf-8") as f:
        html = f.read()

    words = extract_italian_words(html)

    for w in words:
        print(w)

    print(f"\nTotale: {len(words)}")