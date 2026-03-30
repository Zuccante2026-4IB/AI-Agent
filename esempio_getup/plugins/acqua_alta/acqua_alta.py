from cat.mad_hatter.decorators import hook,tool
import requests
import json


@tool(
    return_direct=False,
    examples=["what is the level of sea in Venice?", "C'è acqua alta a Venezia?"]
) 
def acqua_alta_venezia(stazione, cat):
    """Qual'è il livello della marea a Venezia? Input the statione value."""
    marea = livello_marea()
    fmarea = float(marea.replace(" m",""))
    if fmarea >= 1.40:
        messaggio = f"Marea eccezionale:{marea}"
    elif fmarea >=1.10:
        messaggio = f"Marea molto sostenuta:{marea}"
    elif fmarea >0.8:
        messaggio = f"Marea sostenuta:{marea}"
    else:
        messaggio = f"Marea normale:{marea}"
    return messaggio

def livello_marea(staz_arg="Punta Salute Canal Grande"):
    # Indirizzo servizio
    # URL del file JSON remoto
    url = "https://dati.venezia.it/sites/default/files/dataset/opendata/livello.json"

    try:
        # Effettua una richiesta GET all'URL
        response = requests.get(url)
        response.raise_for_status()  # Solleva un'eccezione per errori HTTP (4xx o 5xx)

        # Ottieni il contenuto JSON dalla risposta
        # La funzione json.loads() analizza la stringa JSON e la converte in un oggetto Python
        dati_stazioni = json.loads(response.text)

        # Ora puoi lavorare con i dati come un normale dizionario o lista Python
        # print(data)
        for stazione in dati_stazioni:
            if stazione["stazione"] == staz_arg:
                return stazione["valore"]
                break
        else:
            return dati_stazioni[0]['valore']
                
    except requests.exceptions.RequestException as e:
        return f"Errore durante la richiesta: {e}"
    except json.JSONDecodeError as e:
        return f"Errore durante il parsing del JSON: {e}"

