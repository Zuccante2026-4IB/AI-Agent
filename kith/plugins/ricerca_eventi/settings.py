from cat.mad_hatter.decorators import plugin
from pydantic import BaseModel, field_validator # BaseModel implementa il protocollo Mapping (si può usare: classe["attributo"])
from typing import Literal


# classe contenente tutti gli attributi necessari per le impostazioni
class RicercaEventiSettings(BaseModel):
    # formato GG/MM/AA-hh:mm
    data_e_ora_inizio : str = "" # stringa vuota = ogni orario va bene --> no filtri orario
    data_e_ora_fine : str = "" # stringa vuota --> no range orario, considerare solo quello di inizio
    
    #TO TEST TESTARE IL VALORE PREDEFINITO DENTRO UN'ARRAY E VEDERE COME GESTISCE LA CHAT TUTTO QUESTO
    target : Literal [
    "tutti",          # (tutte le età)
    "bambini",        # (0–12)
    "ragazzi",        # (13–17)
    "giovani",        # (18–25)
    "adulti",         # (26–40)
    "adulti_maturi",  # (41–60)
    "senior"          # (60+)
    ]= ["tutti"] # valore di default = [tutti] e accetta solo i valori passati a Literal, accetta più valori
    
    #TO TEST
    @field_validator("data_e_ora_inizio", "data_e_ora_fine") # campi della classe dove deve agire il metodo sottostante
    @classmethod # differisce dai metodi statici perché "conosce" la classe che lo usa mentre quello statico no, classe si può usare
    def pulisci_date(classe, valore): # classe avrebbe il valore di tipo Classe
        if valore: # valore == True --> stringa non vuota
            return valore.replace(" ", "")
        return valore
    
    #TO TEST
    @field_validator("target")
    @classmethod
    def pulisci_target(calsse, valore): # pydantic si occupa di passare i valori alle funzioni quando vengono inserite
        return valore.lower().replace(" ", "")

@plugin
def settings_model():
    return RicercaEventiSettings