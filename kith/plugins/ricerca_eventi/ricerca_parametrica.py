# modulo per la ricerca dell'agente secondo dei parametri richiesti dall'utente

from cat.mad_hatter.decorators import tool

@tool(
    examples=[""]
    ) #TODO AGGIUNGERE ESEMPI PER AUMENTARE LA PRECISIONE DI INERENZA COL TOOL PER CERCARE GLI EVENTI
def cerca_con_parametro(*params, cat):
    #TODO FORNIRE PRECISA DOCUMETNAZIONE DEL METODO E DEL CASO IN CUI USARLO E CHE PARAMETRI PRENDERE 
    """
        Funzione per cercare in modo parametrico nel database gli eventi secondo ciò che chiede l'utente.
        
    """
    
    db_address = ""
    
    pass # da non considerare la funzione finché non è completa