# modulo per la ricerca dell'agente secondo dei parametri richiesti dall'utente

from cat.mad_hatter.decorators import tool
import requests
import json

class DatabaseConnectionData:
    # Content-Type = application/json
    BASE_URL = "https://strapi.brusegan.it"
    BEARER_TOKEN = "cff92e74316f57f7cd63ce9f93cf8fb309f0f15f673ed41d81afe4f1569a81f88d6b1b4268a94f97e5eb52802a1e1b49ac6702c060f1b96d1d02fa3103f84df65445e2307cd5f15b3ccb141fc91147470465304d44d6f53784989b971c4468aa6932c0b9dc3ed37da4a33e2cd58fcb9fdb87863ead235adca7c87513f47f6e1c"
    LISTA_FASCE = [
        "preadolescenti", # anni: 10 - 13
        "adolescenti",    # anni: 14 - 17
        "giovani",        # anni: 18 - 24
        "giovani_adulti"  # anni: 25 - 35
    ]
    query_params = {
        # permette di avere gli eventi con tutti i dettagli, se assente fornirà l'evento con parte soltanto dei dati
        "populate": "*",
        "pagination[pageSize]": ""
    }
    # utilizzando: filters[target][fascia][$in][{i}]
    query_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }
    
    def __init__(self, populate=True):
        self.query_params["populate"] = "*" if populate else ""
        
        pass
  
def richiesta_eventi_server(DCD:DatabaseConnectionData|None, amount:int|None) -> dict: # restituisce un dizionario
    # restituisce solo 5 eventi dalla ricerca se il parametro amount è None (null)
    DCD.query_params["pagination[pageSize]"] = 5 if amount is None else amount
    
    response = requests.get(f"{DCD.BASE_URL}/api/eventos", params=DCD.query_params, headers=DCD.query_headers)
    # controllo della richiesta se andata a buon fine
    if response.status_code == 200:
        dati = response.json()
    else:
        print(f"Errore con la richiesta: {response.status_code}")

    return dati      
        
        
@tool(
    return_direct=False, # per indicare che la risposta non va stampata direttamente ma "rimandata" al modello che la elabora
    examples=[
    # età esplicita propria
    "Ho 12 anni, ci sono eventi per me?",
    "Ho 16 anni, cosa posso fare questo weekend?",
    "Ho 21 anni, quali eventi trovo?",
    "Ho 28 anni, cosa mi consigli?",
    "Ho 10 anni e voglio uscire, cosa c'è?",
    "Ho 35 anni, ci sono eventi adatti a me?",

    # età esplicita di terzi
    "Mia figlia ha 11 anni, ci sono attività per lei?",
    "Mio fratello ha 17 anni, cosa può fare?",
    "Cerco eventi per mio figlio che ha 13 anni",
    "Ho un gruppo di ragazzi di 15 anni, cosa organizziamo?",

    # categorie nominate direttamente
    "Ci sono eventi per adolescenti?",
    "Cosa c'è per i giovani adulti?",
    "Trovami eventi per preadolescenti",
    "Quali attività ci sono per i giovani?",
    "Dammi una lista di eventi per giovani adulti",

    # range d'età descrittivo
    "Siamo un gruppo tra i 18 e i 24 anni",
    "Cerco attività per ragazzi tra i 10 e i 13 anni",
    "Ho tra i 25 e i 35 anni, cosa c'è?",
    "Attività per chi ha tra i 14 e i 17 anni",

    # formulazioni implicite / alias
    "Sono maggiorenne da poco, che eventi ci sono?",
    "Sono under 18, cosa posso fare?",
    "Attività per under 14 nel weekend",
    "Cosa fanno i giovani in città?",
    "Sono quasi adulto, ci sono eventi per me?",
    "Cerco qualcosa per i giovanissimi",
    "Cosa c'è per i ragazzi delle medie?",
    "Attività per ragazzi delle superiori",
    "Cose da fare per chi è appena entrato nel mondo del lavoro",
    "Sono uno studente universitario, cosa c'è in programma?",

    # richieste generiche con contesto d'età
    "Voglio uscire stasera, ho 19 anni",
    "Cosa c'è di bello da fare per un 30enne?",
    "Suggeriscimi un evento, ho 14 anni",
    "Cosa organizzate per i più giovani?",
    "Attività per ragazzi in età scolare",
]
) 
def cerca_con_parametro(args, cat):
    # L'attributo args indica tutti i criteri secondo cui si puo fare la ricerca, è un dizionario python
    """
        Cerca eventi nel database in base a qualsiasi criterio espresso dall'utente.

        Usa questo tool ogni volta che l'utente vuole trovare, scoprire, cercare
        o chiedere informazioni su eventi, attività, iniziative o appuntamenti,
        indipendentemente da come formula la richiesta.

        I criteri di ricerca supportati sono:

        - nome o titolo dell'evento
        - data, periodo o orario in cui si svolge
        - durata dell'evento
        - luogo, città o sede dove si tiene
        - descrizione o contenuto dell'evento
        - tag o argomenti che riguardano l'evento
        - target d'età del pubblico (preadolescenti, adolescenti, giovani, giovani_adulti)
        - valutazione o popolarità dell'evento
        - organizzatore dell'evento

        L'utente può cercare per uno o più criteri contemporaneamente.
        L'input del tool è la richiesta grezza dell'utente dalla quale
        andranno estratti i parametri di ricerca.
        
        Nel valore di ritorno c'è un dizionario python quindi un JSON dove c'è un tag 'risposta_database' che contiene
        la risposta del database dopo la richiesta degli eventi, tu prendi questa risposta e devi fornirla all'utente 
        rielaborandola correttamente
    """
    pass #!
    
    # Content-Type = application/json
    BASE_URL = DatabaseConnectionData.BASE_URL
    BEARER_TOKEN = DatabaseConnectionData.BEARER_TOKEN
    LISTA_FASCE = DatabaseConnectionData.LISTA_FASCE
    query_headers = DatabaseConnectionData.query_headers
    query_params = DatabaseConnectionData.query_params
    
    fascia_interessata:str = cat.llm(
        """
            In base alla richiesta dell'utente dell'evento, rispondi a modo:
            
            preadolescenti - la risposta che devi dare se l'età è compresa tra i 10 e i 13 anni
            adolescenti - la risposta che devi dare se l'età è compresa tra i 14 e i 17 anni
            giovani - la risposta che devi dare se l'età è compresa tra i 18 e i 24 anni
            giovani_adulti - la risposta che devi dare se l'età è compresa tra i 25 e i 35 anni
        """
    )
    
    # parametrizzazione della query in base alla fascia interessata
    match fascia_interessata:
        case "preadolescenti":
            # istruzione modificando la query con filters[target][fascia][$in][{i}]
            DCD["query_params"[f"filters[target][fascia][$in][{0}]"]]=fascia_interessata
        case "adolescenti":
            DCD["query_params"[f"filters[target][fascia][$in][{1}]"]]=fascia_interessata
        case "giovani":
            DCD["query_params"[f"filters[target][fascia][$in][{2}]"]]=fascia_interessata
        case "giovani_adulti":
            DCD["query_params"[f"filters[target][fascia][$in][{3}]"]]=fascia_interessata
                
    DCD = DatabaseConnectionData(populate=True)
    
    response = richiesta_eventi_server(DCD=DCD) # response è già in formato json 
    
    return dict({ # restituzione di un dizionario python che verrà usato come json dal gatto
        "risposta_database": response
    })
