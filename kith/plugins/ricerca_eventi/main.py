# script main

from pydantic import ValidationError
import ricerca_parametrica

# TODO DA MODIFICARE IN BASE A QUANDO VA CHIAMATO
#TO TEST
def carica_impostazioni_plugin():
    try:
        settings = cat.mad_hatter.get_plugin().load_settings()
    except ValidationError as _: # "_" indica quando l'istanza non si usa (sennò si sarebbe messo "e" al posto di "_")
        cat.send_ws_message("Campo non valido", "error") # messaggio all'utente indicando che c'è un'errore