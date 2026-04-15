# modulo per la ricerca dell'agente secondo dei parametri richiesti dall'utente

from cat.mad_hatter.decorators import tool


#* se la ricerca richiede più parametri, si possono mettere in sequenza le funzioni di ricerca

@tool(
    return_direct=False, # per indicare che la risposta non va stampata direttamente ma "rimandata" al modello che la elabora
    examples=["", ""]
) #TODO AGGIUNGERE ESEMPI PER AUMENTARE LA PRECISIONE DI INERENZA COL TOOL PER CERCARE GLI EVENTI
#TODO CREARE FIRME PER CERCARE IN BASE A QUALE PARAMETRO CERCARE (RICHIESTO DALL'UTENTE)
def cerca_con_parametro(param_luogo, cat):
    #TODO FORNIRE PRECISA DOCUMETNAZIONE DEL METODO E DEL CASO IN CUI USARLO E CHE PARAMETRI PRENDERE
    """
        Funzione per cercare in modo parametrico nel database gli eventi secondo ciò che chiede l'utente.
        
    """
    
    db_address = "" # API di strapi per connettersi al backend e poi al database
    
    pass #* da non considerare la funzione finché non è completa

@tool(
    return_direct=False,
    examples=["", ""]
)
def cerca_con_parametro(param_data, cat):
    """
        Descrizione della funzione...
    """
    
    pass

@tool(
    return_direct=False,
    examples=["", ""]
)
def cerca_con_parametro(param_orario, cat):
    """
        Descrizione della funzione...
    """
    
    pass


@tool(
    return_direct=False,
    examples=["", ""]
)
def cerca_con_parametro(param_target, cat):
    """
        Descrizione della funzione...
    """
    
    pass

@tool(
    return_direct=False,
    examples=["", ""]
)
def cerca_con_parametro(param_tag, cat):
    """
        Descrizione della funzione...
    """
    
    pass


#TODO IMPLEMENTARE RICERCA PER DESCRIZIONE (VEDI GRUPPO BACKEND COME FORNISCE LE DESCRIZIONI)


@tool(
    return_direct=False,    
    examples=["", ""]
)
def ottieni_informazioni_evento(evento, cat):
    """
        Funzione per...
    """
    
    pass