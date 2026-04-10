#script main
from bs4 import BeautifulSoup
import re

def normalize(word):
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