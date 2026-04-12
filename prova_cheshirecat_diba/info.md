password come admin a http://localhost:1865

user: admin
password: admin





facendo partire ollama usare "ollama run nome_modello_scaricato"

usare "/bye" per uscire dall'uso del modello





PER INSTALLARE LE DEPENDENCIES E LE LIBRERIE VARIE, CREARE UN requirements.text DENTRO LA CARTELLA DEL PLUGIN,
LO STREGATTO INSTALLERA' AUTOMATICAMENTE LE LIBRERIE IMPORTATE NEGLI SCRIPT



dopo aver fatto partire "ollama serve" per il server ollama e "ollama run nome-modello" per il modello in esecuzione, nello
stregatto impostare come indirizzo al server ollama (URL modello) http://host.internal.docker:11434




Usato Qdrant FastEmbed come embedder dell'agente e ollama per l'LLM (poi bisogna vedere quale modello è stato messo su ollama)