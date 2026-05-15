# Requirements Document

## Introduction

La feature "evento-dettaglio" sostituisce l'attuale visualizzazione tramite `alert()` con una pagina HTML dedicata (`evento.html`) che mostra tutte le informazioni di un evento in modo strutturato e visivamente coerente con il resto dell'applicazione "Progetto GetUP". La pagina deve caricare i dati dall'API Strapi, visualizzare tutte le informazioni dell'evento, e fornire funzionalità di modifica/eliminazione per gli organizzatori proprietari.

## Glossary

- **Event_Detail_Page**: La nuova pagina HTML (`evento.html`) che visualizza i dettagli completi di un singolo evento
- **Event_Card**: L'elemento cliccabile nella lista eventi (`Index.html`) che attiva la navigazione alla pagina dettaglio
- **API_Client**: Il modulo JavaScript che effettua chiamate HTTP all'API Strapi
- **Auth_Manager**: Il modulo che gestisce l'autenticazione e verifica i permessi utente tramite localStorage
- **Event_Renderer**: Il modulo che trasforma i dati dell'evento in HTML strutturato
- **Navigation_Handler**: Il modulo che gestisce la navigazione tra pagine e il passaggio di parametri URL
- **Owner_Controls**: I pulsanti Modifica ed Elimina visibili solo agli organizzatori proprietari dell'evento
- **Markdown_Parser**: Il componente che converte il campo `desc` (markdown) in HTML

## Requirements

### Requirement 1: Navigation from Event List

**User Story:** As a user viewing the event list, I want to click on an event card to see its full details, so that I can access complete information without using an alert popup.

#### Acceptance Criteria

1. WHEN a user clicks on an Event_Card in Index.html, THE Navigation_Handler SHALL navigate to `evento.html?id={event_id}` where `{event_id}` is the numeric `id` field of the event object
2. WHEN the Event_Card is clicked, THE Navigation_Handler SHALL NOT call `mostraDettagli()` or any `alert()` function
3. THE Event_Card SHALL have `cursor: pointer` style and a visible hover effect to indicate it is clickable
4. IF the event object does not have a valid numeric `id` field, THE Event_Card SHALL NOT be rendered as a clickable link to evento.html

### Requirement 2: Event Data Loading

**User Story:** As a user opening the event detail page, I want the page to automatically load the event data from the API, so that I see current and complete information.

#### Acceptance Criteria

1. WHEN evento.html loads, THE Navigation_Handler SHALL read the `id` query parameter from `window.location.search` using `URLSearchParams`
2. IF the `id` parameter is absent or is not a positive integer, THE Event_Detail_Page SHALL display the message "Evento non trovato" and SHALL NOT make any API request
3. WHILE the API request is in progress, THE Event_Detail_Page SHALL display a visible loading indicator in the main content area
4. WHEN the event ID is a valid positive integer, THE API_Client SHALL fetch `GET https://strapi.brusegan.it/api/eventos/{id}?populate=*` with the Bearer token header
5. IF the fetch throws a network error (no response received), THE Event_Detail_Page SHALL display the message "Errore di connessione"
6. IF the API responds with HTTP 404, THE Event_Detail_Page SHALL display the message "Evento non trovato"
7. IF the API responds with any other non-2xx status (e.g. 401, 403, 500), THE Event_Detail_Page SHALL display the message "Errore nel caricamento dell'evento"
8. WHEN the API responds with HTTP 200 and a valid event object, THE Event_Renderer SHALL render the event's `nome`, `desc`, `date_time`, `luogo`, `imgs`, `target`, and `rank` fields in the main content area

### Requirement 3: Event Information Display

**User Story:** As a user viewing the event detail page, I want to see all event information in a structured and readable format, so that I can understand all aspects of the event.

#### Acceptance Criteria

1. THE Event_Renderer SHALL display the event `nome` as an `<h1>` element at the top of the content area
2. THE Event_Renderer SHALL render the event `desc` field through the Markdown_Parser and insert the resulting HTML into a dedicated `<div class="evento-desc-detail">` container
3. FOR EACH entry in `date_time`, THE Event_Renderer SHALL display the start (`st`) and end (`en`) times formatted as "DD/MM/YYYY HH:MM – DD/MM/YYYY HH:MM"
4. THE Event_Renderer SHALL display `luogo.name` as the location label
5. FOR EACH entry in `imgs`, THE Event_Renderer SHALL render an `<img>` element with the `src` and `alt` attributes from the entry; IF `imgs` is empty or absent, no image section SHALL be rendered
6. FOR EACH entry in `target`, THE Event_Renderer SHALL display `target[].fascia` as a styled badge using the `targets` CSS class
7. IF `rank` is present, THE Event_Renderer SHALL display `rank.stars` formatted as "X/5 stelle"
8. IF `rank.sponsored` is `true`, THE Event_Renderer SHALL display a "Sponsorizzato" badge
9. IF `rank` is absent or null, THE Event_Renderer SHALL display "Valutazione: —"

### Requirement 4: Owner Authorization Check

**User Story:** As an event organizer, I want to see edit and delete buttons only for events I own, so that I can manage my events while preventing unauthorized modifications.

#### Acceptance Criteria

1. WHEN evento.html finishes loading the event data, THE Auth_Manager SHALL call `JSON.parse(localStorage.getItem("utenteLoggato"))` to retrieve the current user
2. IF `localStorage.getItem("utenteLoggato")` returns `null` or throws a parse error, THE Owner_Controls SHALL NOT be rendered in the DOM
3. IF the parsed user object has `ruolo !== "organizzatore"`, THE Owner_Controls SHALL NOT be rendered in the DOM
4. IF the parsed user object has `ruolo === "organizzatore"` AND `user.id === evento.org_id`, THEN THE Owner_Controls SHALL be rendered as a visible `<div>` containing the "Modifica" and "Elimina" buttons
5. IF the parsed user object has `ruolo === "organizzatore"` AND `user.id !== evento.org_id`, THE Owner_Controls SHALL NOT be rendered in the DOM

### Requirement 5: Owner Controls Functionality

**User Story:** As an event organizer viewing my event, I want to edit or delete the event from the detail page, so that I can manage my events without returning to the list.

#### Acceptance Criteria

1. WHEN the Owner_Controls are rendered, THE Event_Detail_Page SHALL display a button labelled "✏️ Modifica" with class `btn-modifica` and a button labelled "🗑️ Elimina" with class `btn-elimina`
2. WHEN the "Modifica" button is clicked, THE Navigation_Handler SHALL set `window.location.href` to `gestione.html?id={event_id}`
3. WHEN the "Elimina" button is clicked, THE Event_Detail_Page SHALL call `confirm("Sei sicuro di voler eliminare \"{event_name}\"?")` before making any API call
4. WHEN the user confirms the deletion dialog, THE API_Client SHALL send `DELETE https://strapi.brusegan.it/api/eventos/{id}` with the Bearer token header
5. WHEN the DELETE request returns a 2xx response, THE Navigation_Handler SHALL set `window.location.href` to `Index.html`
6. IF the user dismisses the confirmation dialog, THE API_Client SHALL NOT send any DELETE request and the page SHALL remain unchanged
7. IF the DELETE request fails (network error or non-2xx response), THE Event_Detail_Page SHALL display the message "Errore durante l'eliminazione" without navigating away

### Requirement 6: Return Navigation

**User Story:** As a user viewing an event detail page, I want to return to the event list, so that I can browse other events without using browser back button.

#### Acceptance Criteria

1. THE Event_Detail_Page SHALL display a "← Torna alla lista" link or button visible at all times (including error states)
2. WHEN the "← Torna alla lista" control is clicked, THE Navigation_Handler SHALL navigate to `Index.html`
3. THE "← Torna alla lista" control SHALL use the `btn-annulla` CSS class for visual consistency with other navigation elements

### Requirement 7: Visual Consistency

**User Story:** As a user navigating the application, I want the event detail page to look consistent with other pages, so that I have a cohesive user experience.

#### Acceptance Criteria

1. THE Event_Detail_Page SHALL include the same `<header>` structure as `Index.html` and `gestione.html`, with the title "Progetto GetUP"
2. THE Event_Detail_Page SHALL include a `<nav>` with links to `Index.html` (Homepage), `login.html` (Login), and `chat.html` (Chat)
3. THE `<body>` element SHALL have the class `body1`
4. THE Event_Detail_Page SHALL link `style.css` as its stylesheet
5. THE Event_Detail_Page SHALL set `lang="it"` on the `<html>` element and `<meta charset="UTF-8">` in the `<head>`

### Requirement 8: Markdown Description Rendering

**User Story:** As a user viewing an event detail page, I want to see the event description with proper formatting, so that I can read structured content with headings, lists, and emphasis.

#### Acceptance Criteria

1. IF the `desc` field is an empty string or null, THE Event_Renderer SHALL render an empty `<div class="evento-desc-detail">` without calling the Markdown_Parser
2. WHEN the `desc` field is a non-empty string, THE Markdown_Parser SHALL convert it to HTML supporting: headings (`#`, `##`, `###`), bold (`**text**`), italic (`*text*`), unordered lists (`- item`), and inline links (`[text](url)`)
3. THE Markdown_Parser SHALL strip or escape any `<script>`, `<iframe>`, and `on*` event handler attributes from the output HTML before insertion into the DOM
4. THE Event_Renderer SHALL set the `innerHTML` of `<div class="evento-desc-detail">` to the sanitized HTML output of the Markdown_Parser
5. THE `<div class="evento-desc-detail">` container SHALL have a minimum `line-height` of `1.5` and `padding` of at least `8px` applied via `style.css` or inline style

### Requirement 9: Error Handling and Loading States

**User Story:** As a user waiting for event data to load, I want to see appropriate feedback, so that I know the application is working and understand if something goes wrong.

#### Acceptance Criteria

1. WHILE the API request is in progress, THE Event_Detail_Page SHALL display the text "Caricamento..." in the main content area
2. WHEN the loading state ends (success or error), THE loading indicator SHALL be removed from the DOM
3. IF the event data returned by the API is missing the `nome` field, THE Event_Detail_Page SHALL display "Dati incompleti" instead of rendering the event
4. FOR ALL error and loading states, THE Event_Detail_Page SHALL keep the `<header>`, `<nav>`, and "← Torna alla lista" control visible and functional
