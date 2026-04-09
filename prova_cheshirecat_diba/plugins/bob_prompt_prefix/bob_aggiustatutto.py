from cat.mad_hatter.decorators import hook  # Non crea problemi perché dentro il container esiste la libreria (warning ignorabile)

@hook(priority = 2) # Priorità di default = 1 se non si inserisce il parametro priority = number
#più altà è la priorità più l'hook è "importante" quindi da eseguire prima
def agent_prompt_prefix(prefix, cat): # Bisogna sempre inserire cat come parametro nelle funzioni
    # Cambiare la personalità del gatto

    # Cercando nella pagina dei plugin col nome indicato nel file .json verrà fuori il plugin

    # Carica le impostazioni secondo la classe creata in settings.py
    settings = cat.mad_hatter.get_plugin().load_settings()

    # Prefix dato al gatto da usare come prompt prefix, il gatto riceverà questo prompt ogni volta e modificherà il prefix per l'agente
    prefix = settings["prefix"]
    return prefix # Restituito direttamente al modello