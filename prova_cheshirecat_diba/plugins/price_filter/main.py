from cat.mad_hatter.decorators import hook

@hook # default priority = 1
def before_rabbithole_insert_memory(doc, cat): # doc --> chunk del documento (una parte sola del documento), esamina un pezzo alla volta del documento
    # inserimento del metadato user_id (appartenente a straycat)
    # doc.metadata["user_id"] = cat.user_id

    # invia un messaggio di tipo notifica tramite WebSocket all'utente dove dice "Controllando se ci sono prezzi nel chunck del documento..."
    cat.send_ws_message("Controllando se ci sono prezzi nel chunck del documento...", "notification")

    # chiedere all'llm se ci sono dei prezzi nel chucnk di documento
    response = cat.llm(f"""
        Leggi il seguente contenuto e controlla se sono presenti dei prezzi all'interno.
        Se sono presenti dei prezzi, SEI OBBLIGATO a rispondere "si" sennò SEI OBBLIGATO IN CASO CONTRARIO a rispondere "no".
        {doc.page_content}. Questo è il contenuto che devi esaminare
    """) # richiesta all'llm con in seguito una formattazione della risposta da poi poter elaborare eventualmente

    # invio di una risposta all'utente
    cat.send_ws_message("Il documento contiene prezzi: " + response)
    
    # aggiunge un metadato dove dice se sono presenti prezzi o meno (formattando la risposta in minuscolo con .lower())
    doc.metadata["price"] = response.lower()

    return doc # restituire sempre tutto ciò che viene modificato

# si può usare log per stampare i messaggi a terminale del gatto formattandoli meglio e avendo più funzionalità mentre è attivo

# questo plugin è combinabile con il plugin "only_docs" creato nella directory in modo che si avvii solo quando la risposta contiene
# dei documenti e non quando non sono presenti


@hook # default priority = 1
def before_cat_recalls_declarative_memories(declarative_call_config, cat):
    # prima che il gatto vada a cercare nelle sue memorie dichiarative
    declarative_call_config["metadata"] = {"price": "yes"}
    
    return declarative_call_config