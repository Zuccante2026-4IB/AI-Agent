from fastapi import FastAPI, HTTPrequest

# indica la path dopo l'indirizzo nella richiesta http
@app.get("/")
def root():
    return {"codice_richiesta": "200, riuscita"}

# Il client farà uina richiesta post al backend fastAPI che poi la farà al gatto che si metterà in ascolto in determinati momenti