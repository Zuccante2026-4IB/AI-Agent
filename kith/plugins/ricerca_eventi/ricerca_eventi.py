# modulo per la ricerca dell'agente secondo dei parametri richiesti dall'utente

from cat.mad_hatter.decorators import tool


# se la ricerca richiede più parametri, si possono mettere in sequenza le funzioni di ricerca

@tool(
    return_direct=False, # per indicare che la risposta non va stampata direttamente ma "rimandata" al modello che la elabora
    examples=["", ""]
)
#? GUARDARE SE USARE UN PARAMETRO SINGOLO OPPURE UN KWARGS SE CI SONO PIU' PARAMETRI
def cerca_con_parametro(param, cat):
    """
        Funzione per cercare in modo parametrico nel database gli eventi secondo ciò che chiede l'utente.
        L'input è il criterio secondo il quale l'utente vuole cercare che sia:
        - il nome dell'evento
        - la sua data
        - la sua durata
        - il luogo dove si svolge
        - la sua descrizione
        - i tag che contiene che indicano un pò "l'argomento" dell'evento
        - il target che ha nel pubblico in base all'età
        - l'id dell'organizzatore dell'evento
        - rank dell'evento quindi la sua valutazione
        
        
        TODO CREARE FORMATTAZIONE DELLA RISPOSTA E IN BASE A QUELLA FORMARE UNA QUERY OPPURE FAR FORMARE LA QUERY ALL'LLM
    """
    pass

    db_address = "" # API di strapi per connettersi al backend e poi al database
    db_query = "" # query per l'API di strapi per la ricerca mirata
    



@tool(
    return_direct=False,    
    examples=["", ""]
)
def ottieni_informazioni_evento(evento, cat):
    """
        Funzione per... (AGGIUNGERE DESCRIZIONE)
    """
    
    pass