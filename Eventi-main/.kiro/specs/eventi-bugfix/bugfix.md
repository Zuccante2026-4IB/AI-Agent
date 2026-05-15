# Bugfix Requirements Document

## Introduction

Il progetto "Progetto GetUP" è una web app JavaScript vanilla per la gestione e visualizzazione di eventi a Venezia. Sono stati identificati 6 bug che compromettono il funzionamento dell'applicazione: due ReferenceError che impediscono il rendering degli eventi e il caricamento della pagina di gestione, un problema di parsing delle date che produce output non validi, inconsistenze nei link di navigazione tra le pagine, e mancanze nell'head di `login.html` che causano problemi di rendering dei caratteri speciali.

---

## Bug Analysis

### Current Behavior (Defect)

**Bug 1 — `card` non dichiarata in `app.js`**

1.1 WHEN la funzione `mostra_pagina()` viene eseguita con un array di eventi non vuoto THEN il sistema lancia un `ReferenceError: card is not defined` perché la variabile `card` viene usata prima di essere dichiarata, impedendo la visualizzazione di qualsiasi evento e bloccando l'esecuzione del ciclo.

**Bug 2 — `verificaAccesso` non definita in `gestione.js`**

1.2 WHEN la pagina `gestione.html` viene caricata e il listener `DOMContentLoaded` viene eseguito THEN il sistema lancia un `ReferenceError: verificaAccesso is not defined` perché la funzione viene chiamata ma non è definita in nessun punto del file, impedendo il caricamento dell'intera pagina di gestione.

**Bug 3 — Link case-sensitive a `index.html` / `Index.html`**

1.3 WHEN un utente naviga verso la homepage cliccando il link "Homepage" da `login.html` o `gestione.html` su un sistema operativo case-sensitive (Linux/server) THEN il sistema restituisce un errore 404 perché i link puntano a `index.html` (minuscola) mentre il file reale si chiama `Index.html` (maiuscola).

1.4 WHEN un utente naviga verso la homepage cliccando il link "Homepage" da `Index.html` stessa THEN il sistema restituisce un errore 404 sullo stesso sistema case-sensitive perché anche il link self-referenziale in `Index.html` punta a `index.html` (minuscola).

**Bug 4 — Parsing del formato data custom dell'API**

1.5 WHEN la funzione `mostra_pagina()` o `mostraDettagli()` riceve una data nel formato custom dell'API (es. `"20260501T20:00:00UTC+02"`) e la passa a `new Date("20260501T20:00:00UTC+02")` THEN il sistema produce un oggetto `Invalid Date`, e la funzione `stringDate()` restituisce la stringa `"NaN/NaN/NaN NaN:NaN"` invece di una data leggibile.

**Bug 5 — Mancanza di `charset` e `lang` in `login.html`**

1.6 WHEN il browser carica `login.html` THEN il sistema non applica la codifica UTF-8 né la lingua italiana perché mancano `<meta charset="UTF-8">` e l'attributo `lang="it"` sull'elemento `<html>`, causando potenziali problemi di rendering dei caratteri speciali italiani (es. à, è, ì, ò, ù).

**Bug 6 — Link "Chat" assente nella navbar di `login.html`**

1.7 WHEN un utente si trova sulla pagina `login.html` e vuole navigare alla Chat THEN il sistema non offre il link "Chat" nella navbar, a differenza di tutte le altre pagine (`Index.html`, `gestione.html`, `chat.html`) che lo includono, creando un'inconsistenza di navigazione.

---

### Expected Behavior (Correct)

**Bug 1 — `card` dichiarata correttamente**

2.1 WHEN la funzione `mostra_pagina()` viene eseguita con un array di eventi non vuoto THEN il sistema SHALL creare un nuovo elemento `div` per ogni evento nel ciclo, assegnarlo alla variabile `card`, configurarne le proprietà e aggiungerlo al DOM, rendendo visibili le card degli eventi nella pagina.

2.2 WHEN la funzione `mostra_pagina()` viene eseguita con un array di eventi non vuoto THEN il sistema SHALL NON lanciare alcun `ReferenceError` relativo alla variabile `card`.

**Bug 2 — `verificaAccesso` definita in `gestione.js`**

2.3 WHEN la pagina `gestione.html` viene caricata da un utente loggato come organizzatore THEN il sistema SHALL caricare il form di gestione senza errori JavaScript nella console.

2.4 WHEN la pagina `gestione.html` viene caricata da un utente non loggato THEN il sistema SHALL reindirizzare l'utente a `Index.html` senza mostrare il form.

2.5 WHEN la pagina `gestione.html` viene caricata da un utente loggato con ruolo diverso da `"organizzatore"` THEN il sistema SHALL reindirizzare l'utente a `Index.html` senza mostrare il form.

**Bug 3 — Link coerenti verso `Index.html`**

2.6 WHEN un utente clicca il link "Homepage" in qualsiasi pagina dell'applicazione (`login.html`, `gestione.html`, `Index.html`, `chat.html`) su un sistema case-sensitive THEN il sistema SHALL caricare `Index.html` con HTTP 200 senza errori 404.

2.7 IF un file HTML dell'applicazione contiene un link alla homepage THEN il valore dell'attributo `href` SHALL essere esattamente `Index.html` (con la I maiuscola) in tutti i file.

2.8 THE applicazione SHALL usare un unico riferimento canonico `Index.html` per tutti i link interni alla homepage, senza varianti `index.html` o `INDEX.HTML`.

**Bug 4 — Parsing corretto del formato data custom**

2.9 WHEN la funzione `stringDate()` riceve una stringa nel formato custom dell'API `"YYYYMMDDThh:mm:ssUTC+TZ"` (es. `"20260501T20:00:00UTC+02"`) THEN il sistema SHALL restituire la stringa `"01/05/2026 20:00"` nel formato `"dd/mm/yyyy hh:mm"`.

2.10 WHEN la funzione `stringDate()` riceve una stringa nel formato custom dell'API con ora a singola cifra (es. `"20260501T09:05:00UTC+02"`) THEN il sistema SHALL restituire `"01/05/2026 09:05"` con zero-padding su ore e minuti.

2.11 IF la funzione `stringDate()` riceve una stringa malformata o non riconoscibile THEN il sistema SHALL restituire la stringa `"—"` invece di `"NaN/NaN/NaN NaN:NaN"`.

**Bug 5 — `charset` e `lang` presenti in `login.html`**

2.12 WHEN il browser carica `login.html` THEN il sistema SHALL dichiarare `<meta charset="UTF-8">` come primo elemento dell'`<head>`, garantendo che i caratteri `à`, `è`, `ì`, `ò`, `ù` siano renderizzati correttamente.

2.13 WHEN il browser carica `login.html` THEN il sistema SHALL dichiarare `lang="it"` sull'elemento `<html>`, in modo che i tool di accessibilità e i browser identifichino la lingua della pagina come italiano.

**Bug 6 — Link "Chat" presente nella navbar di `login.html`**

2.14 WHEN un utente si trova sulla pagina `login.html` THEN il sistema SHALL mostrare nella navbar un elemento `<li>` con un link `<a href="chat.html">Chat</a>`, nella stessa posizione in cui appare nelle altre pagine.

2.15 WHEN un utente clicca il link "Chat" nella navbar di `login.html` THEN il sistema SHALL navigare correttamente alla pagina `chat.html`.

---

### Unchanged Behavior (Regression Prevention)

3.1 WHEN la funzione `mostra_pagina()` riceve un array di eventi non vuoto con dati validi THEN il sistema SHALL CONTINUE TO renderizzare correttamente le card degli eventi con nome, date, luogo, descrizione, tag, target, immagini e valutazione.

3.2 WHEN la funzione `mostra_pagina()` viene chiamata con un numero di pagina valido THEN il sistema SHALL CONTINUE TO applicare la paginazione corretta, mostrando al massimo `eventiPerPagina` eventi per pagina.

3.3 WHEN un utente loggato come organizzatore visualizza un evento di sua proprietà THEN il sistema SHALL CONTINUE TO mostrare i pulsanti "Modifica" ed "Elimina" sulla card dell'evento.

3.4 WHEN la funzione `stringDate()` riceve un oggetto `Date` valido costruito da una stringa ISO 8601 standard THEN il sistema SHALL CONTINUE TO restituire la data formattata nel formato `"dd/mm/yyyy hh:mm"`.

3.5 WHEN un utente non autenticato o non organizzatore tenta di accedere a `gestione.html` THEN il sistema SHALL CONTINUE TO reindirizzare l'utente alla homepage.

3.6 WHEN un organizzatore autenticato accede a `gestione.html` con un `id` evento valido nell'URL THEN il sistema SHALL CONTINUE TO caricare e pre-compilare il form di modifica con i dati dell'evento.

3.7 WHEN un organizzatore autenticato accede a `gestione.html` senza `id` nell'URL THEN il sistema SHALL CONTINUE TO mostrare il form vuoto per la creazione di un nuovo evento.

3.8 WHEN un utente clicca su una card evento THEN il sistema SHALL CONTINUE TO mostrare i dettagli dell'evento tramite `alert`.

3.9 WHEN la funzione `eliminaEvento()` viene chiamata da un organizzatore autorizzato THEN il sistema SHALL CONTINUE TO eliminare l'evento tramite API e aggiornare la lista visualizzata.

3.10 WHEN le pagine `Index.html`, `gestione.html` e `chat.html` vengono caricate THEN il sistema SHALL CONTINUE TO applicare correttamente charset UTF-8 e lingua italiana come già configurato nei rispettivi file.
