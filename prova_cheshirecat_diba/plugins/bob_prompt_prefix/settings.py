from pydantic import BaseModel # Per creare un'oggetto con tutte le impostazioni
from cat.mad_hatter.decorators import plugin

class BobSettings(BaseModel):
    prefix: str = """You are Bob l'aggiustatutto, always happy to help the Human in a kind but direct way""" # Con valore di default



# Crea nel plugin la possibilità di configurare le impostazioni (attributi della classe BobSettings) inserendo l'icona di una rotellina
# dove cliccando port a un menù laterale dove ci sono gli attributi della classe da configurare,
# sovrascrive quindi il comportamento normale del metodo dandogli la possibilità di modificare le configurazioni del plugin stesso
# come se fosse un file .json con tutte le impostazioni e viene caricato dal metodo @plugin chiamato da load_settings()
#  (vedi bob_aggiustatutto.py all'inizializzazione della variabile settings nella funzione @hook per il prefix del prompt del modello)
@plugin
def settings_model():
    return BobSettings # Viene "detto" che esiste un modello di impostazioni ed è la classe BobSettings
 