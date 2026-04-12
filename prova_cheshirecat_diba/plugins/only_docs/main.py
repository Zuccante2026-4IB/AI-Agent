from cat.mad_hatter.decorators import hook

@hook # priorità predefinits (0)
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
    
    print(message.why.memory["declarative"])
    if len(message.why.memory["declarative"]) == 0: # Tag della memoria dichiarativa vuota quindi con valore 0 
        message.content = "Non lo posso sapere" # message.content è il messaggio finale che esprime il gatto
    return message