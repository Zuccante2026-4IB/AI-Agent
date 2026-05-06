# modulo per la ricerca dell'agente secondo dei parametri richiesti dall'utente

from cat.mad_hatter.decorators import tool
import requests
import json


# se la ricerca richiede più parametri, si possono mettere in sequenza le funzioni di ricerca

@tool(
    return_direct=False, # per indicare che la risposta non va stampata direttamente ma "rimandata" al modello che la elabora
    examples=["", ""] # todo 
)
# TO TEST 
def cerca_con_parametro(*param, cat):
    # L'attributo *param indica tutti i criteri secondo cui si puo fare la ricerca
    """
        Funzione per cercare in modo parametrico nel database gli eventi secondo ciò che chiede l'utente.
        L'input è il criterio secondo il quale l'utente vuole cercare che sia:
        
        - il nome dell'evento
        - la sua data
        - la sua durata
        - il luogo dove si svolge
        - la sua descrizione
        - i tag che contiene che indicano un pò "l'argomento" dell'evento
        - il target che ha nel pubblico in base all'età scegliendo tra:
            - preadolescenti (gente compresa tra i 10 e i 13 anni)
            - adolescenti (gente compresa tra i 14 e i 17 anni)
            - giovani (gente compresa tra i 18 e i 24 anni)
            - giovani_adulti (gente compresa tra i 25 e i 35 anni)
            
            Non accetti altre categorie oltre a queste 4 e devi inserire nella posizione 0
            del parametro *param (kwarg) una lista con dentro per ogni valore i valori richiesti
            quindi se chiede più categorie tu fai una lista con ognuna di queste sennò una lista
            con un valore solo
            
            esempio:
                Se l'utente chiede giovani e adolescenti tu crei una lista in
                param[0] equivalente a ['giovani', 'adolescenti']
            
        - l'id dell'organizzatore dell'evento
        - rank dell'evento quindi la sua valutazione
        
        
    """
    #! TOOL NON TERMINATO ################################################################################################
    pass
    #! TOOL NON TERMINATO ################################################################################################
    
    # Content-Type = application/json
    BASE_URL = "https://strapi.brusegan.it"
    BEARER_TOKEN = "cff92e74316f57f7cd63ce9f93cf8fb309f0f15f673ed41d81afe4f1569a81f88d6b1b4268a94f97e5eb52802a1e1b49ac6702c060f1b96d1d02fa3103f84df65445e2307cd5f15b3ccb141fc91147470465304d44d6f53784989b971c4468aa6932c0b9dc3ed37da4a33e2cd58fcb9fdb87863ead235adca7c87513f47f6e1c"
    LISTA_FASCE = [
        "preadolescenti",
        "adolescenti",
        "giovani",
        "giovani_adulti"
    ]
    
    filtri_ricerca = param[0]
    
    query_params = {
        "populate": "*", # permette di avere gli eventi con tutti i dettagli
    }
    
    #popolamento dell'attributo filters[target][fascia][$in][{i}] in params con i valori corretti
    for i, f in enumerate(LISTA_FASCE):
        query_params[f"filters[target][fascia][$in][{i}]"] = f #
    
    query_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }
    
    response = requests.get(f"{BASE_URL}/api/eventos", params=query_params, headers=query_headers)
    
    if response.status_code == 200:
        dati = response.json()
    else:
        print(f"Errore: {response.status_code}")
    
    # TODO INSERIRE LINK ALL'EVENTO NELLA RISPOSTA 
    