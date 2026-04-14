# Script main
from cat.mad_hatter.decorator import hook

#TO TEST

# funzione per caricare il prompt prefix
@hook(priority = 10) # default priority = 1 --> priorità bassa
def agent_prompt_prefix(prefix, cat):
    settings = cat.mad_hatter.get_plugin().load_settings() # carica le informazioni dall'oggetto creato in settings.py
    prefix = settings["prefix"]
    return prefix # restituzione obbligatoria del valore modificato