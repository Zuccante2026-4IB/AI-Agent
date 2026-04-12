from cat.mad_hatter.decorators import hook

@hook # priorità predefinits (1)
# Funzione che si chiama esattamente come l'hook
def before_cat_sends_message(message, cat):
    # Stamperà un messaggio con la seguente struttura:
    # 
    # {
    #     "type": "chat",  # type of websocket message, a chat message will appear as a text bubble in the chat
    #     "user_id": "user_1",  # id of the client to which the message is to be sent
    #     "content": "Meeeeow",  # the Cat's answer
    #     "why": {
    #         "input": "Hello Cheshire Cat!",  # user's input
    #         "intermediate_steps": cat_message.get("intermediate_steps"),  # list of tools used to provide the answer
    #         "memory": {
    #             "episodic": episodic_report,  # lists of documents retrieved from the memories
    #             "declarative": declarative_report,
    #             "procedural": procedural_report,
    #         }
    #     }
    # }

    memorie_dichiarative_gatto = cat.working_memory.declarative_memories # Analogo di message.why.memory["declarative"]
    
    print(message.why.memory["declarative"])
    if len(message.why.memory["declarative"]) == 0: # Tag della memoria dichiarativa vuota quindi con valore 0 
        message.content = "Non lo posso sapere" # message.content è il messaggio finale che esprime il gatto
    # bisogna sempre restituire il valore perché se ci sono più hooks vengono messi in sequenza (pipeline) e quindi devono restituire un dato
    return message

    # In questo modo la risposta del gatto sarà modificata nel caso in cui il messaggio non sia prodotto di una richiesta con
    # una memoria dichiarativa rilevante (in questo caso)


# metodo di hook per considerare la memoria episodica in modo diverso (cambiamento valore di K)
@hook # priorità di default = 1
def before_cat_recalls_episodic_memories(episodic_recall_config, cat):
    # cambiamento del numero di memorie episodiche richiamate
    episodic_recall_config["k"] = 0

    return episodic_recall_config 