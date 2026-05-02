# 🐱 Cheshire Cat AI – API Reference (Guida Completa)

## (Secondo ChatGPT)

## 📌 Cos'è Cheshire Cat

Cheshire Cat è un framework open source per creare chatbot e agenti AI con memoria, plugin e gestione documenti.

---

# 🧠 1. CHAT API

## POST /v1/chat

Invia un messaggio al bot e ricevi una risposta.

### Request

```json
{
  "message": "Ciao",
  "conversation_id": "user1"
}
```

### Response

```json
{
  "response": "Ciao! Come posso aiutarti?",
  "conversation_id": "user1"
}
```

---

## WS /v1/chat/stream

Risposte in tempo reale (streaming token-by-token).

---

# 💬 2. CONVERSAZIONI

## GET /v1/conversations

Lista di tutte le conversazioni

## GET /v1/conversations/{id}

Dettaglio conversazione

## DELETE /v1/conversations/{id}

Elimina conversazione

---

# 🧠 3. MEMORY API

## POST /v1/memory

Salva informazioni nella memoria

```json
{
  "text": "L'utente ama il calcio"
}
```

---

## GET /v1/memory?query=...

Cerca nella memoria

---

## DELETE /v1/memory/{id}

Elimina memoria

---

# 📄 4. DOCUMENTS (RAG)

## POST /v1/documents

Carica documenti (PDF, TXT, ecc.)

## GET /v1/documents

Lista documenti

## DELETE /v1/documents/{id}

Elimina documento

---

# 🔍 5. SEARCH & EMBEDDINGS

## POST /v1/embeddings

Genera embedding

## POST /v1/search

Ricerca semantica nei dati

---

# 🔌 6. PLUGINS

## GET /v1/plugins

Lista plugin disponibili

## POST /v1/plugins/{plugin_id}/toggle

Attiva/disattiva plugin

## POST /v1/plugins/{plugin_id}/settings

Configura plugin

---

# ⚙️ 7. LLM CONFIG

## GET /v1/llm

Ottieni configurazione corrente

## POST /v1/llm

Imposta configurazione

```json
{
  "provider": "openai",
  "model": "gpt-4",
  "temperature": 0.7
}
```

---

# 👤 8. USERS

## GET /v1/users

Lista utenti

## POST /v1/users

Crea utente

---

# 🔐 9. AUTH

## POST /v1/auth/login

Login

## POST /v1/auth/logout

Logout

---

# 📡 10. SYSTEM

## GET /v1/status

Stato sistema

## GET /v1/health

Health check

---

# 🌐 11. WEBSOCKET

## WS /ws

Connessione realtime

---

# 🧱 STRUTTURA GENERALE

* Chat → /v1/chat
* Memoria → /v1/memory
* Documenti → /v1/documents
* Plugin → /v1/plugins
* Config AI → /v1/llm

---

# ⚠️ NOTE IMPORTANTI

* Le API possono cambiare in base alla versione
* Alcune route dipendono dai plugin attivi
* Cheshire Cat va hostato in locale o server

---

# 🚀 TEST API

Apri nel browser:

http://localhost:1865/docs

Troverai Swagger UI con tutte le API aggiornate.

---

# ✅ USE CASE TIPICI

* Chatbot con memoria
* Assistente con documenti (RAG)
* AI con plugin personalizzati
* Backend per app AI

---

# 🎯 CONSIGLIO

Inizia da:

1. /v1/chat
2. /v1/memory
3. /v1/documents

E poi espandi con plugin e configurazioni.

---
