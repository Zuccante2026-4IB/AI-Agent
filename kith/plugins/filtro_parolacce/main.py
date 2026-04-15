from bs4 import BeautifulSoup  # per analizzare HTML
import requests                # per scaricare la pagina web
import re                      # per usare le regex


def normalize(word):
    """
    Pulisce e normalizza una parola:
    - minuscolo
    - rimuove accenti
    - rimuove simboli
    - rimuove spazi
    """
    
    # tutto minuscolo
    word = word.lower()
    
    # sostituzione accenti
    replacements = {
        "à": "a", "è": "e", "é": "e",
        "ì": "i", "ò": "o", "ù": "u"
    }
    for k, v in replacements.items():
        word = word.replace(k, v)

    # rimuove tutto tranne lettere e spazi
    word = re.sub(r"[^a-z\s]", "", word)

    # rimuove gli spazi
    word = word.replace(" ", "")

    return word


def extract_italian_words(html):
    """
    Estrae parole italiane da tag HTML con:
    <i lang="it">...</i>
    """
    
    # parsing HTML
    soup = BeautifulSoup(html, "html.parser")
    
    # set per evitare duplicati
    results = set()

    # trova SOLO tag <i> con attributo lang="it"
    for tag in soup.find_all("i", attrs={"lang": "it"}):
        
        # testo interno del tag
        text = tag.get_text().strip()

        # divide varianti (es: parola1 / parola2 or parola3)
        parts = re.split(r"/|\bor\b", text, flags=re.IGNORECASE)

        for part in parts:
            # normalizza la parola
            part = normalize(part)

            # aggiunge solo se non vuota
            if part:
                results.add(part)

    # restituisce lista ordinata
    return sorted(results)


# ===== PROGRAMMA PRINCIPALE =====
if __name__ == "__main__":

    # URL della pagina Wikipedia
    url = "https://en.wikipedia.org/wiki/Italian_profanity"

    # richiesta HTTP
    response = requests.get(url)

    # controllo errore
    if response.status_code != 200:
        print("Errore nel download:", response.status_code)
        exit()

    # HTML della pagina
    html = response.text

    # estrazione parole italiane
    words = extract_italian_words(html)

    # stampa risultati
    for w in words:
        print(w)

    # stampa totale
    print(f"\nTotale: {len(words)}")