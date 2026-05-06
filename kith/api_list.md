# API Cheshire Cat - Guida Rapida

## Elenco Endpoint e Descrizioni

### Core & Conversazione
- `GET /`: Verifica se il server è attivo e risponde.
- `POST /query`: Invia un messaggio al Cat e riceve la risposta elaborata dall'LLM.
- `GET /ws/{client_id}`: Apre una connessione WebSocket per la chat in tempo reale.

### Stato & Metadati
- `GET /status`: Restituisce lo stato del sistema e del database vettoriale.
- `GET /info`: Fornisce informazioni sulla versione e sui plugin attivi.

### Memoria (LTM)
- `GET /memory/collections`: Elenca le collezioni di memoria vettoriale disponibili.
- `DELETE /memory/collections/{collection_id}`: Elimina un'intera collezione di memoria.
- `GET /memory/recall`: Cerca ricordi rilevanti nelle memorie in base a una stringa.
- `GET /memory/points/{collection_id}`: Recupera i singoli vettori memorizzati in una collezione.
- `DELETE /memory/points/{collection_id}`: Elimina vettori specifici da una collezione.
- `POST /memory/conversation_history/wipe`: Cancella interamente la cronologia della conversazione attuale.

### Plugin & Tool
- `GET /plugins`: Elenca tutti i plugin installati nel sistema.
- `POST /plugins/upload`: Carica un nuovo plugin tramite file .zip.
- `POST /plugins/upload/registry`: Installa un plugin direttamente dal registro ufficiale.
- `GET /plugins/settings`: Recupera le configurazioni di tutti i plugin.
- `GET /plugins/settings/{plugin_id}`: Recupera le impostazioni specifiche di un singolo plugin.
- `PUT /plugins/settings/{plugin_id}`: Aggiorna le impostazioni di un plugin specifico.
- `POST /plugins/toggle/{plugin_id}`: Attiva o disattiva un plugin senza disinstallarlo.
- `DELETE /plugins/{plugin_id}`: Rimuove definitivamente un plugin dal sistema.

### Impostazioni
- `GET /settings`: Elenca tutte le impostazioni globali del Cat.
- `POST /settings`: Crea una nuova configurazione globale.
- `GET /settings/{setting_id}`: Recupera i dettagli di una specifica impostazione.
- `PUT /settings/{setting_id}`: Modifica un'impostazione esistente.
- `DELETE /settings/{setting_id}`: Elimina un'impostazione specifica.

### Modelli (LLM & Embedder)
- `GET /llm/list`: Elenca i modelli di linguaggio supportati e configurabili.
- `PUT /llm/settings/{llm_id}`: Configura le chiavi API e i parametri per un LLM specifico.
- `GET /embedder/list`: Elenca i modelli di embedding disponibili.
- `PUT /embedder/settings/{embedder_id}`: Configura i parametri per un embedder specifico.

### Rabbit Hole (Ingestione dati)
- `POST /rabbithole`: Invia un file locale per essere indicizzato nella memoria.
- `POST /rabbithole/web`: Invia un URL per estrarre contenuti web nella memoria.
- `GET /rabbithole/allowed-mimetypes`: Elenca i formati di file supportati per il caricamento.

---

## Esempi per UI Web (JavaScript Fetch)

### 1. Inviare un messaggio alla Chat
```javascript
const sendMessage = async (text) => {
    const response = await fetch('http://localhost:8006/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: text })
    });
    return await response.json();
};
```

### 2. Caricare un file nel Rabbit Hole
```javascript
const uploadFile = async (file) => {
    const formData = new FormData();
    formData.append('file', file);
    
    await fetch('http://localhost:8006/rabbithole', {
        method: 'POST',
        body: formData
    });
};
```

### 3. Cambiare Impostazioni di un Plugin
```javascript
const updatePluginSettings = async (pluginId, settings) => {
    await fetch(`http://localhost:8006/plugins/settings/${pluginId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(settings)
    });
};
```

### 4. Connessione WebSocket (Real-time)
```javascript
const socket = new WebSocket('ws://localhost:8006/ws/user_123');
socket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log("Messaggio dal Cat:", data.content);
};
```
