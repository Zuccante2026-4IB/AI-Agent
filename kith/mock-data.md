# Mock Data — Tag ed Eventos

---

## TAG (100 mock)

Ogni richiesta va inviata come POST a `/api/tags` con il seguente body:

```json
{ "data": { "text": "..." } }
```

### Lista tag

- mock - musica
- mock - sport
- mock - arte
- mock - teatro
- mock - cinema
- mock - danza
- mock - fotografia
- mock - pittura
- mock - scultura
- mock - letteratura
- mock - poesia
- mock - fumetti
- mock - videogiochi
- mock - tecnologia
- mock - informatica
- mock - robotica
- mock - scienza
- mock - astronomia
- mock - natura
- mock - ambiente
- mock - sostenibilità
- mock - cucina
- mock - streetfood
- mock - degustazione
- mock - birra artigianale
- mock - cocktail
- mock - caffè
- mock - moda
- mock - design
- mock - architettura
- mock - storia
- mock - cultura
- mock - tradizioni
- mock - religione
- mock - filosofia
- mock - psicologia
- mock - benessere
- mock - yoga
- mock - meditazione
- mock - fitness
- mock - running
- mock - ciclismo
- mock - skateboard
- mock - surf
- mock - arrampicata
- mock - escursionismo
- mock - campeggio
- mock - volontariato
- mock - sociale
- mock - politica
- mock - economia
- mock - startup
- mock - imprenditoria
- mock - networking
- mock - hackathon
- mock - workshop
- mock - conferenza
- mock - seminario
- mock - formazione
- mock - lingue
- mock - inglese
- mock - spagnolo
- mock - francese
- mock - giapponese
- mock - anime
- mock - k-pop
- mock - hip hop
- mock - rap
- mock - rock
- mock - jazz
- mock - classica
- mock - elettronica
- mock - DJ set
- mock - live music
- mock - karaoke
- mock - giochi da tavolo
- mock - escape room
- mock - quiz
- mock - stand up comedy
- mock - magia
- mock - circo
- mock - street art
- mock - graffiti
- mock - podcast
- mock - radio
- mock - editoria
- mock - animali
- mock - cavalli
- mock - cani
- mock - gatti
- mock - mare
- mock - montagna
- mock - lago
- mock - città
- mock - viaggio
- mock - scambio culturale
- mock - intercultura
- mock - pride
- mock - inclusione
- mock - accessibilità

---

## EVENTOS (100 mock)

Ogni richiesta va inviata come POST a `/api/eventos` con il seguente body completo.

> I tag vanno collegati separatamente dopo aver creato i tag e ottenuto i loro ID.

---

- mock - Concerto Rock al Parco
```json
{
  "data": {
    "nome": "mock - Concerto Rock al Parco",
    "desc": "## Concerto Rock\nUna serata di musica rock dal vivo con band locali.",
    "date_time": [{"st": "20260601T20:00:00UTC+02", "en": "20260601T23:00:00UTC+02"}],
    "luogo": {"name": "Parco Centrale", "lat": 45.4654, "lon": 9.1859},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 1,
    "imgs": [{"alt": "Concerto rock", "src": "https://esempio.com/rock.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Festival dello Street Food
```json
{
  "data": {
    "nome": "mock - Festival dello Street Food",
    "desc": "## Street Food Festival\nI migliori cibi di strada da tutto il mondo in un unico posto.",
    "date_time": [{"st": "20260610T12:00:00UTC+02", "en": "20260610T22:00:00UTC+02"}],
    "luogo": {"name": "Piazza Garibaldi", "lat": 45.4668, "lon": 9.1905},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 2,
    "imgs": [{"alt": "Street food", "src": "https://esempio.com/streetfood.jpg"}],
    "rank": {"stars": 5, "sponsored": true}
  }
}
```

- mock - Hackathon Giovani Sviluppatori
```json
{
  "data": {
    "nome": "mock - Hackathon Giovani Sviluppatori",
    "desc": "## Hackathon\n48 ore per costruire un'app e vincere premi.",
    "date_time": [{"st": "20260615T09:00:00UTC+02", "en": "20260617T18:00:00UTC+02"}],
    "luogo": {"name": "Fab Lab Milano", "lat": 45.4720, "lon": 9.1800},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 3,
    "imgs": [{"alt": "Hackathon", "src": "https://esempio.com/hackathon.jpg"}],
    "rank": {"stars": 5, "sponsored": true}
  }
}
```

- mock - Mostra di Fotografia Urbana
```json
{
  "data": {
    "nome": "mock - Mostra di Fotografia Urbana",
    "desc": "## Fotografia Urbana\nEsposizione di fotografi emergenti under 30.",
    "date_time": [{"st": "20260620T10:00:00UTC+02", "en": "20260620T19:00:00UTC+02"}],
    "luogo": {"name": "Galleria d'Arte Moderna", "lat": 45.4690, "lon": 9.1750},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 4,
    "imgs": [{"alt": "Fotografia urbana", "src": "https://esempio.com/foto.jpg"}],
    "rank": {"stars": 3, "sponsored": false}
  }
}
```

- mock - Torneo di Skateboard
```json
{
  "data": {
    "nome": "mock - Torneo di Skateboard",
    "desc": "## Skate Contest\nGara di skateboard aperta a tutti i livelli.",
    "date_time": [{"st": "20260622T14:00:00UTC+02", "en": "20260622T20:00:00UTC+02"}],
    "luogo": {"name": "Skate Park Navigli", "lat": 45.4520, "lon": 9.1710},
    "target": [{"fascia": "preadolescenti"}, {"fascia": "adolescenti"}],
    "org_id": 5,
    "imgs": [{"alt": "Skateboard", "src": "https://esempio.com/skate.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Workshop di Pittura Acrilica
```json
{
  "data": {
    "nome": "mock - Workshop di Pittura Acrilica",
    "desc": "## Pittura Acrilica\nImpara le tecniche base della pittura acrilica con un artista professionista.",
    "date_time": [{"st": "20260625T15:00:00UTC+02", "en": "20260625T18:00:00UTC+02"}],
    "luogo": {"name": "Atelier Brera", "lat": 45.4725, "lon": 9.1870},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 6,
    "imgs": [{"alt": "Pittura", "src": "https://esempio.com/pittura.jpg"}],
    "rank": {"stars": 3, "sponsored": false}
  }
}
```

- mock - Serata Karaoke
```json
{
  "data": {
    "nome": "mock - Serata Karaoke",
    "desc": "## Karaoke Night\nCanta le tue canzoni preferite in compagnia.",
    "date_time": [{"st": "20260628T21:00:00UTC+02", "en": "20260629T01:00:00UTC+02"}],
    "luogo": {"name": "Bar del Centro", "lat": 45.4640, "lon": 9.1890},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 7,
    "imgs": [{"alt": "Karaoke", "src": "https://esempio.com/karaoke.jpg"}],
    "rank": {"stars": 2, "sponsored": false}
  }
}
```

- mock - Corso di Yoga all'Aperto
```json
{
  "data": {
    "nome": "mock - Corso di Yoga all'Aperto",
    "desc": "## Yoga al Parco\nLezione di yoga per principianti in un ambiente naturale.",
    "date_time": [{"st": "20260701T08:00:00UTC+02", "en": "20260701T10:00:00UTC+02"}],
    "luogo": {"name": "Parco Sempione", "lat": 45.4741, "lon": 9.1727},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 8,
    "imgs": [{"alt": "Yoga", "src": "https://esempio.com/yoga.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - DJ Set Elettronico
```json
{
  "data": {
    "nome": "mock - DJ Set Elettronico",
    "desc": "## Electronic Night\nUna notte di musica elettronica con DJ internazionali.",
    "date_time": [{"st": "20260705T22:00:00UTC+02", "en": "20260706T04:00:00UTC+02"}],
    "luogo": {"name": "Club Warehouse", "lat": 45.4580, "lon": 9.2100},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 9,
    "imgs": [{"alt": "DJ Set", "src": "https://esempio.com/djset.jpg"}],
    "rank": {"stars": 5, "sponsored": true}
  }
}
```

- mock - Torneo di Videogiochi
```json
{
  "data": {
    "nome": "mock - Torneo di Videogiochi",
    "desc": "## Gaming Tournament\nCompetizione su giochi popolari con premi in palio.",
    "date_time": [{"st": "20260708T10:00:00UTC+02", "en": "20260708T22:00:00UTC+02"}],
    "luogo": {"name": "Gaming Arena", "lat": 45.4700, "lon": 9.2050},
    "target": [{"fascia": "preadolescenti"}, {"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 10,
    "imgs": [{"alt": "Gaming", "src": "https://esempio.com/gaming.jpg"}],
    "rank": {"stars": 5, "sponsored": true}
  }
}
```

- mock - Gita in Bici lungo il Naviglio
```json
{
  "data": {
    "nome": "mock - Gita in Bici lungo il Naviglio",
    "desc": "## Bike Tour\nPasseggiata in bici di 20km lungo i Navigli milanesi.",
    "date_time": [{"st": "20260712T09:00:00UTC+02", "en": "20260712T13:00:00UTC+02"}],
    "luogo": {"name": "Naviglio Grande", "lat": 45.4530, "lon": 9.1700},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 11,
    "imgs": [{"alt": "Bici", "src": "https://esempio.com/bici.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Stand Up Comedy Night
```json
{
  "data": {
    "nome": "mock - Stand Up Comedy Night",
    "desc": "## Comedy Night\nUna serata di risate con i migliori comici emergenti.",
    "date_time": [{"st": "20260715T21:00:00UTC+02", "en": "20260715T23:30:00UTC+02"}],
    "luogo": {"name": "Teatro Piccolo", "lat": 45.4680, "lon": 9.1820},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 12,
    "imgs": [{"alt": "Comedy", "src": "https://esempio.com/comedy.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Mercatino Vintage
```json
{
  "data": {
    "nome": "mock - Mercatino Vintage",
    "desc": "## Vintage Market\nAbiti, accessori e oggetti vintage a prezzi accessibili.",
    "date_time": [{"st": "20260719T10:00:00UTC+02", "en": "20260719T18:00:00UTC+02"}],
    "luogo": {"name": "Piazza Dergano", "lat": 45.4890, "lon": 9.1780},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 13,
    "imgs": [{"alt": "Vintage", "src": "https://esempio.com/vintage.jpg"}],
    "rank": {"stars": 3, "sponsored": false}
  }
}
```

- mock - Serata Anime e Manga
```json
{
  "data": {
    "nome": "mock - Serata Anime e Manga",
    "desc": "## Anime Night\nProjection di anime cult e scambio di manga tra appassionati.",
    "date_time": [{"st": "20260722T18:00:00UTC+02", "en": "20260722T23:00:00UTC+02"}],
    "luogo": {"name": "Centro Culturale Giapponese", "lat": 45.4710, "lon": 9.1960},
    "target": [{"fascia": "preadolescenti"}, {"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 14,
    "imgs": [{"alt": "Anime", "src": "https://esempio.com/anime.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Corso di Arrampicata Indoor
```json
{
  "data": {
    "nome": "mock - Corso di Arrampicata Indoor",
    "desc": "## Climbing\nLezione introduttiva all'arrampicata sportiva indoor.",
    "date_time": [{"st": "20260725T16:00:00UTC+02", "en": "20260725T19:00:00UTC+02"}],
    "luogo": {"name": "Palestra Boulder", "lat": 45.4760, "lon": 9.2010},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 15,
    "imgs": [{"alt": "Arrampicata", "src": "https://esempio.com/climbing.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Flash Mob in Piazza
```json
{
  "data": {
    "nome": "mock - Flash Mob in Piazza",
    "desc": "## Flash Mob\nUnisciti al flash mob di danza in piazza aperto a tutti.",
    "date_time": [{"st": "20260801T17:00:00UTC+02", "en": "20260801T18:30:00UTC+02"}],
    "luogo": {"name": "Piazza del Duomo", "lat": 45.4642, "lon": 9.1900},
    "target": [{"fascia": "preadolescenti"}, {"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 16,
    "imgs": [{"alt": "Flash mob", "src": "https://esempio.com/flashmob.jpg"}],
    "rank": {"stars": 3, "sponsored": false}
  }
}
```

- mock - Serata di Escape Room
```json
{
  "data": {
    "nome": "mock - Serata di Escape Room",
    "desc": "## Escape Room\nRisolvi gli enigmi e scappa dalla stanza prima che scada il tempo.",
    "date_time": [{"st": "20260805T19:00:00UTC+02", "en": "20260805T22:00:00UTC+02"}],
    "luogo": {"name": "Escape Milano", "lat": 45.4715, "lon": 9.1945},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 17,
    "imgs": [{"alt": "Escape room", "src": "https://esempio.com/escape.jpg"}],
    "rank": {"stars": 5, "sponsored": true}
  }
}
```

- mock - Proiezione Cinema all'Aperto
```json
{
  "data": {
    "nome": "mock - Proiezione Cinema all'Aperto",
    "desc": "## Cinema Estivo\nFilm cult proiettati sotto le stelle nel parco.",
    "date_time": [{"st": "20260808T21:30:00UTC+02", "en": "20260809T00:00:00UTC+02"}],
    "luogo": {"name": "Arena Estiva", "lat": 45.4600, "lon": 9.1850},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 18,
    "imgs": [{"alt": "Cinema", "src": "https://esempio.com/cinema.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Workshop di Podcast
```json
{
  "data": {
    "nome": "mock - Workshop di Podcast",
    "desc": "## Podcast Workshop\nImpara a creare e pubblicare il tuo podcast da zero.",
    "date_time": [{"st": "20260812T14:00:00UTC+02", "en": "20260812T18:00:00UTC+02"}],
    "luogo": {"name": "Coworking Space", "lat": 45.4695, "lon": 9.1920},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 19,
    "imgs": [{"alt": "Podcast", "src": "https://esempio.com/podcast.jpg"}],
    "rank": {"stars": 3, "sponsored": false}
  }
}
```

- mock - Gara di Running 5km
```json
{
  "data": {
    "nome": "mock - Gara di Running 5km",
    "desc": "## City Run\nCorsa non competitiva di 5km per le vie del centro.",
    "date_time": [{"st": "20260815T08:00:00UTC+02", "en": "20260815T11:00:00UTC+02"}],
    "luogo": {"name": "Parco Sempione", "lat": 45.4741, "lon": 9.1727},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 20,
    "imgs": [{"alt": "Running", "src": "https://esempio.com/running.jpg"}],
    "rank": {"stars": 4, "sponsored": true}
  }
}
```

- mock - Laboratorio di Ceramica
```json
{
  "data": {
    "nome": "mock - Laboratorio di Ceramica",
    "desc": "## Ceramica\nCrea il tuo oggetto in ceramica con le mani guidato da un ceramista.",
    "date_time": [{"st": "20260818T15:00:00UTC+02", "en": "20260818T18:00:00UTC+02"}],
    "luogo": {"name": "Studio Artigiano", "lat": 45.4670, "lon": 9.1780},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 21,
    "imgs": [{"alt": "Ceramica", "src": "https://esempio.com/ceramica.jpg"}],
    "rank": {"stars": 3, "sponsored": false}
  }
}
```

- mock - Serata Giochi da Tavolo
```json
{
  "data": {
    "nome": "mock - Serata Giochi da Tavolo",
    "desc": "## Board Game Night\nUna serata dedicata ai giochi da tavolo moderni.",
    "date_time": [{"st": "20260820T18:00:00UTC+02", "en": "20260820T23:00:00UTC+02"}],
    "luogo": {"name": "Ludoteca del Quartiere", "lat": 45.4655, "lon": 9.1830},
    "target": [{"fascia": "preadolescenti"}, {"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 22,
    "imgs": [{"alt": "Board game", "src": "https://esempio.com/boardgame.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Corso di Hip Hop Dance
```json
{
  "data": {
    "nome": "mock - Corso di Hip Hop Dance",
    "desc": "## Hip Hop Dance\nLezione di danza hip hop per principianti e intermedi.",
    "date_time": [{"st": "20260822T17:00:00UTC+02", "en": "20260822T19:00:00UTC+02"}],
    "luogo": {"name": "Centro Danza Urbana", "lat": 45.4730, "lon": 9.1990},
    "target": [{"fascia": "preadolescenti"}, {"fascia": "adolescenti"}],
    "org_id": 23,
    "imgs": [{"alt": "Hip hop", "src": "https://esempio.com/hiphop.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Evento di Networking Startup
```json
{
  "data": {
    "nome": "mock - Evento di Networking Startup",
    "desc": "## Startup Networking\nIncontra fondatori, investitori e appassionati di startup.",
    "date_time": [{"st": "20260825T18:30:00UTC+02", "en": "20260825T21:30:00UTC+02"}],
    "luogo": {"name": "Impact Hub Milano", "lat": 45.4750, "lon": 9.2030},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 24,
    "imgs": [{"alt": "Startup", "src": "https://esempio.com/startup.jpg"}],
    "rank": {"stars": 5, "sponsored": true}
  }
}
```

- mock - Laboratorio di Street Art
```json
{
  "data": {
    "nome": "mock - Laboratorio di Street Art",
    "desc": "## Street Art Lab\nImpara le tecniche base del graffiti e della street art legale.",
    "date_time": [{"st": "20260829T14:00:00UTC+02", "en": "20260829T18:00:00UTC+02"}],
    "luogo": {"name": "Muro Libero Isola", "lat": 45.4840, "lon": 9.1880},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 25,
    "imgs": [{"alt": "Street art", "src": "https://esempio.com/streetart.jpg"}],
    "rank": {"stars": 3, "sponsored": false}
  }
}
```

- mock - Conferenza sull'Intelligenza Artificiale
```json
{
  "data": {
    "nome": "mock - Conferenza sull'Intelligenza Artificiale",
    "desc": "## AI Conference\nRelatori esperti parlano del futuro dell'intelligenza artificiale.",
    "date_time": [{"st": "20260902T09:00:00UTC+02", "en": "20260902T18:00:00UTC+02"}],
    "luogo": {"name": "Politecnico di Milano", "lat": 45.4780, "lon": 9.2270},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 26,
    "imgs": [{"alt": "AI", "src": "https://esempio.com/ai.jpg"}],
    "rank": {"stars": 5, "sponsored": true}
  }
}
```

- mock - Torneo di Beach Volley
```json
{
  "data": {
    "nome": "mock - Torneo di Beach Volley",
    "desc": "## Beach Volley\nTorneo amatoriale di beach volley aperto a tutti.",
    "date_time": [{"st": "20260905T10:00:00UTC+02", "en": "20260905T18:00:00UTC+02"}],
    "luogo": {"name": "Beach Arena Idroscalo", "lat": 45.4430, "lon": 9.2780},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 27,
    "imgs": [{"alt": "Beach volley", "src": "https://esempio.com/beachvolley.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Serata Jazz dal Vivo
```json
{
  "data": {
    "nome": "mock - Serata Jazz dal Vivo",
    "desc": "## Jazz Night\nMusica jazz live con trio locale in un locale storico.",
    "date_time": [{"st": "20260908T20:00:00UTC+02", "en": "20260908T23:30:00UTC+02"}],
    "luogo": {"name": "Blue Note Milano", "lat": 45.4825, "lon": 9.1710},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 28,
    "imgs": [{"alt": "Jazz", "src": "https://esempio.com/jazz.jpg"}],
    "rank": {"stars": 5, "sponsored": false}
  }
}
```

- mock - Workshop di Fotografia con Smartphone
```json
{
  "data": {
    "nome": "mock - Workshop di Fotografia con Smartphone",
    "desc": "## Mobile Photography\nImpara a fare foto professionali con il tuo telefono.",
    "date_time": [{"st": "20260912T14:00:00UTC+02", "en": "20260912T17:00:00UTC+02"}],
    "luogo": {"name": "Brera Design District", "lat": 45.4725, "lon": 9.1870},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 29,
    "imgs": [{"alt": "Fotografia", "src": "https://esempio.com/mobilephoto.jpg"}],
    "rank": {"stars": 3, "sponsored": false}
  }
}
```

- mock - Mercato delle Pulci
```json
{
  "data": {
    "nome": "mock - Mercato delle Pulci",
    "desc": "## Flea Market\nOggetti usati, vinili, libri e curiosità a prezzi stracciati.",
    "date_time": [{"st": "20260915T09:00:00UTC+02", "en": "20260915T17:00:00UTC+02"}],
    "luogo": {"name": "Viale Papiniano", "lat": 45.4590, "lon": 9.1720},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 30,
    "imgs": [{"alt": "Mercato pulci", "src": "https://esempio.com/flea.jpg"}],
    "rank": {"stars": 3, "sponsored": false}
  }
}
```

- mock - Serata di Meditazione Guidata
```json
{
  "data": {
    "nome": "mock - Serata di Meditazione Guidata",
    "desc": "## Meditazione\nSessione di meditazione guidata per ridurre lo stress.",
    "date_time": [{"st": "20260918T19:00:00UTC+02", "en": "20260918T21:00:00UTC+02"}],
    "luogo": {"name": "Centro Zen", "lat": 45.4680, "lon": 9.1900},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 31,
    "imgs": [{"alt": "Meditazione", "src": "https://esempio.com/meditazione.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Torneo di Ping Pong
```json
{
  "data": {
    "nome": "mock - Torneo di Ping Pong",
    "desc": "## Ping Pong Tournament\nTorneo amatoriale di ping pong con premi finali.",
    "date_time": [{"st": "20260920T15:00:00UTC+02", "en": "20260920T20:00:00UTC+02"}],
    "luogo": {"name": "Spazio Jova", "lat": 45.4700, "lon": 9.1950},
    "target": [{"fascia": "preadolescenti"}, {"fascia": "adolescenti"}],
    "org_id": 32,
    "imgs": [{"alt": "Ping pong", "src": "https://esempio.com/pingpong.jpg"}],
    "rank": {"stars": 3, "sponsored": false}
  }
}
```

- mock - Festival della Birra Artigianale
```json
{
  "data": {
    "nome": "mock - Festival della Birra Artigianale",
    "desc": "## Craft Beer Festival\nDegustazione di oltre 50 birre artigianali italiane.",
    "date_time": [{"st": "20260925T16:00:00UTC+02", "en": "20260925T23:00:00UTC+02"}],
    "luogo": {"name": "Piazza Oberdan", "lat": 45.4720, "lon": 9.2050},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 33,
    "imgs": [{"alt": "Birra", "src": "https://esempio.com/birra.jpg"}],
    "rank": {"stars": 5, "sponsored": true}
  }
}
```

- mock - Corso di Lingua Giapponese
```json
{
  "data": {
    "nome": "mock - Corso di Lingua Giapponese",
    "desc": "## Giapponese Base\nLezione introduttiva alla lingua e cultura giapponese.",
    "date_time": [{"st": "20261002T17:00:00UTC+02", "en": "20261002T19:00:00UTC+02"}],
    "luogo": {"name": "Istituto Giapponese di Cultura", "lat": 45.4710, "lon": 9.1965},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 34,
    "imgs": [{"alt": "Giapponese", "src": "https://esempio.com/giapponese.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Serata K-Pop Dance
```json
{
  "data": {
    "nome": "mock - Serata K-Pop Dance",
    "desc": "## K-Pop Night\nImpara le coreografie dei gruppi K-Pop più famosi.",
    "date_time": [{"st": "20261005T18:00:00UTC+02", "en": "20261005T21:00:00UTC+02"}],
    "luogo": {"name": "Dance Studio K", "lat": 45.4735, "lon": 9.1880},
    "target": [{"fascia": "preadolescenti"}, {"fascia": "adolescenti"}],
    "org_id": 35,
    "imgs": [{"alt": "K-pop", "src": "https://esempio.com/kpop.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Escursione sul Monte Rosa
```json
{
  "data": {
    "nome": "mock - Escursione sul Monte Rosa",
    "desc": "## Trekking\nEscursione guidata di un giorno sul Monte Rosa adatta a tutti.",
    "date_time": [{"st": "20261010T07:00:00UTC+02", "en": "20261010T19:00:00UTC+02"}],
    "luogo": {"name": "Monte Rosa", "lat": 45.9369, "lon": 7.8703},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 36,
    "imgs": [{"alt": "Montagna", "src": "https://esempio.com/montagna.jpg"}],
    "rank": {"stars": 5, "sponsored": false}
  }
}
```

- mock - Laboratorio di Fumetto
```json
{
  "data": {
    "nome": "mock - Laboratorio di Fumetto",
    "desc": "## Comics Lab\nCrea il tuo fumetto con tecniche professionali.",
    "date_time": [{"st": "20261015T14:00:00UTC+02", "en": "20261015T17:00:00UTC+02"}],
    "luogo": {"name": "Fumetteria Centrale", "lat": 45.4665, "lon": 9.1875},
    "target": [{"fascia": "preadolescenti"}, {"fascia": "adolescenti"}],
    "org_id": 37,
    "imgs": [{"alt": "Fumetto", "src": "https://esempio.com/fumetto.jpg"}],
    "rank": {"stars": 3, "sponsored": false}
  }
}
```

- mock - Serata di Astronomia
```json
{
  "data": {
    "nome": "mock - Serata di Astronomia",
    "desc": "## Stargazing\nOsservazione del cielo notturno con telescopi professionali.",
    "date_time": [{"st": "20261018T21:00:00UTC+02", "en": "20261019T01:00:00UTC+02"}],
    "luogo": {"name": "Osservatorio di Brera", "lat": 45.4728, "lon": 9.1872},
    "target": [{"fascia": "preadolescenti"}, {"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 38,
    "imgs": [{"alt": "Astronomia", "src": "https://esempio.com/stelle.jpg"}],
    "rank": {"stars": 5, "sponsored": false}
  }
}
```

- mock - Workshop di Design Grafico
```json
{
  "data": {
    "nome": "mock - Workshop di Design Grafico",
    "desc": "## Graphic Design\nImpara le basi del design grafico con Figma.",
    "date_time": [{"st": "20261022T14:00:00UTC+02", "en": "20261022T18:00:00UTC+02"}],
    "luogo": {"name": "Coworking CreativeHub", "lat": 45.4755, "lon": 9.2010},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 39,
    "imgs": [{"alt": "Design", "src": "https://esempio.com/design.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Torneo di Calcetto
```json
{
  "data": {
    "nome": "mock - Torneo di Calcetto",
    "desc": "## Calcetto\nTorneo amatoriale di calcio a 5 aperto a squadre libere.",
    "date_time": [{"st": "20261025T15:00:00UTC+02", "en": "20261025T20:00:00UTC+02"}],
    "luogo": {"name": "Campo Sportivo Gorla", "lat": 45.4950, "lon": 9.2200},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 40,
    "imgs": [{"alt": "Calcetto", "src": "https://esempio.com/calcetto.jpg"}],
    "rank": {"stars": 3, "sponsored": false}
  }
}
```

- mock - Serata Quiz Trivia
```json
{
  "data": {
    "nome": "mock - Serata Quiz Trivia",
    "desc": "## Quiz Night\nGara a squadre su cultura generale, cinema, musica e sport.",
    "date_time": [{"st": "20261028T19:30:00UTC+02", "en": "20261028T22:00:00UTC+02"}],
    "luogo": {"name": "Pub The Crown", "lat": 45.4690, "lon": 9.1940},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 41,
    "imgs": [{"alt": "Quiz", "src": "https://esempio.com/quiz.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Laboratorio di Robotica
```json
{
  "data": {
    "nome": "mock - Laboratorio di Robotica",
    "desc": "## Robotica\nCostruisci e programma il tuo robot con Arduino.",
    "date_time": [{"st": "20261101T10:00:00UTC+01", "en": "20261101T13:00:00UTC+01"}],
    "luogo": {"name": "Maker Space Milano", "lat": 45.4780, "lon": 9.1800},
    "target": [{"fascia": "preadolescenti"}, {"fascia": "adolescenti"}],
    "org_id": 42,
    "imgs": [{"alt": "Robotica", "src": "https://esempio.com/robotica.jpg"}],
    "rank": {"stars": 5, "sponsored": true}
  }
}
```

- mock - Serata di Improvvisazione Teatrale
```json
{
  "data": {
    "nome": "mock - Serata di Improvvisazione Teatrale",
    "desc": "## Teatro Impro\nSpettacolo di teatro di improvvisazione con pubblico coinvolto.",
    "date_time": [{"st": "20261105T20:30:00UTC+01", "en": "20261105T22:30:00UTC+01"}],
    "luogo": {"name": "Teatro dell'Elfo", "lat": 45.4698, "lon": 9.2015},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 43,
    "imgs": [{"alt": "Teatro", "src": "https://esempio.com/teatro.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Open Mic Poetry
```json
{
  "data": {
    "nome": "mock - Open Mic Poetry",
    "desc": "## Open Mic\nSali sul palco e leggi le tue poesie davanti al pubblico.",
    "date_time": [{"st": "20261108T19:00:00UTC+01", "en": "20261108T22:00:00UTC+01"}],
    "luogo": {"name": "Libreria Verso", "lat": 45.4660, "lon": 9.1830},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 44,
    "imgs": [{"alt": "Poesia", "src": "https://esempio.com/poetry.jpg"}],
    "rank": {"stars": 3, "sponsored": false}
  }
}
```

- mock - Corso di Mixology
```json
{
  "data": {
    "nome": "mock - Corso di Mixology",
    "desc": "## Cocktail Workshop\nImpara a preparare cocktail classici e creativi.",
    "date_time": [{"st": "20261112T18:00:00UTC+01", "en": "20261112T21:00:00UTC+01"}],
    "luogo": {"name": "Bar Academy", "lat": 45.4720, "lon": 9.1980},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 45,
    "imgs": [{"alt": "Cocktail", "src": "https://esempio.com/cocktail.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Campagna di Volontariato Ambientale
```json
{
  "data": {
    "nome": "mock - Campagna di Volontariato Ambientale",
    "desc": "## Clean Up Day\nPulizia del parco cittadino insieme ad altri volontari.",
    "date_time": [{"st": "20261115T09:00:00UTC+01", "en": "20261115T13:00:00UTC+01"}],
    "luogo": {"name": "Parco Forlanini", "lat": 45.4460, "lon": 9.2530},
    "target": [{"fascia": "preadolescenti"}, {"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 46,
    "imgs": [{"alt": "Volontariato", "src": "https://esempio.com/volontariato.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Fiera del Libro Usato
```json
{
  "data": {
    "nome": "mock - Fiera del Libro Usato",
    "desc": "## Libri Usati\nScambia e acquista libri usati a prezzi simbolici.",
    "date_time": [{"st": "20261118T10:00:00UTC+01", "en": "20261118T18:00:00UTC+01"}],
    "luogo": {"name": "Piazza Sant'Agostino", "lat": 45.4600, "lon": 9.1760},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 47,
    "imgs": [{"alt": "Libri", "src": "https://esempio.com/libri.jpg"}],
    "rank": {"stars": 3, "sponsored": false}
  }
}
```

- mock - Serata di Magia
```json
{
  "data": {
    "nome": "mock - Serata di Magia",
    "desc": "## Magic Show\nSpettacolo di magia close-up e grande illusionismo.",
    "date_time": [{"st": "20261122T20:00:00UTC+01", "en": "20261122T22:30:00UTC+01"}],
    "luogo": {"name": "Teatro Carcano", "lat": 45.4615, "lon": 9.1905},
    "target": [{"fascia": "preadolescenti"}, {"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 48,
    "imgs": [{"alt": "Magia", "src": "https://esempio.com/magia.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Torneo di Basket 3x3
```json
{
  "data": {
    "nome": "mock - Torneo di Basket 3x3",
    "desc": "## Basket 3x3\nTorneo di streetball in stile NBA aperto a tutti.",
    "date_time": [{"st": "20261125T14:00:00UTC+01", "en": "20261125T19:00:00UTC+01"}],
    "luogo": {"name": "Campetto Turro", "lat": 45.4910, "lon": 9.2180},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 49,
    "imgs": [{"alt": "Basket", "src": "https://esempio.com/basket.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Laboratorio di Scrittura Creativa
```json
{
  "data": {
    "nome": "mock - Laboratorio di Scrittura Creativa",
    "desc": "## Creative Writing\nEsercizi e tecniche per sviluppare il tuo stile narrativo.",
    "date_time": [{"st": "20261129T16:00:00UTC+01", "en": "20261129T19:00:00UTC+01"}],
    "luogo": {"name": "Biblioteca Sormani", "lat": 45.4635, "lon": 9.1945},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 50,
    "imgs": [{"alt": "Scrittura", "src": "https://esempio.com/scrittura.jpg"}],
    "rank": {"stars": 3, "sponsored": false}
  }
}
```

- mock - Serata Rap Battle
```json
{
  "data": {
    "nome": "mock - Serata Rap Battle",
    "desc": "## Rap Battle\nSfida i migliori rapper della città in una battle freestyle.",
    "date_time": [{"st": "20261202T20:00:00UTC+01", "en": "20261202T23:30:00UTC+01"}],
    "luogo": {"name": "Circolo Magnolia", "lat": 45.4450, "lon": 9.2760},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 51,
    "imgs": [{"alt": "Rap", "src": "https://esempio.com/rap.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Corso di Cucina Giapponese
```json
{
  "data": {
    "nome": "mock - Corso di Cucina Giapponese",
    "desc": "## Sushi Workshop\nImpara a preparare sushi e ramen con uno chef giapponese.",
    "date_time": [{"st": "20261205T14:00:00UTC+01", "en": "20261205T17:00:00UTC+01"}],
    "luogo": {"name": "Scuola di Cucina Orientale", "lat": 45.4705, "lon": 9.1960},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 52,
    "imgs": [{"alt": "Sushi", "src": "https://esempio.com/sushi.jpg"}],
    "rank": {"stars": 5, "sponsored": false}
  }
}
```

- mock - Mostra di Arte Digitale
```json
{
  "data": {
    "nome": "mock - Mostra di Arte Digitale",
    "desc": "## Digital Art Exhibition\nEsposizione di opere d'arte create con strumenti digitali e AI.",
    "date_time": [{"st": "20261208T10:00:00UTC+01", "en": "20261215T19:00:00UTC+01"}],
    "luogo": {"name": "BASE Milano", "lat": 45.4552, "lon": 9.1820},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 53,
    "imgs": [{"alt": "Arte digitale", "src": "https://esempio.com/digital-art.jpg"}],
    "rank": {"stars": 5, "sponsored": true}
  }
}
```

- mock - Campionato di Scacchi
```json
{
  "data": {
    "nome": "mock - Campionato di Scacchi",
    "desc": "## Torneo Scacchi\nCampionato aperto a tutti i livelli, dai principianti ai professionisti.",
    "date_time": [{"st": "20261210T09:00:00UTC+01", "en": "20261210T18:00:00UTC+01"}],
    "luogo": {"name": "Circolo Scacchistico Milanese", "lat": 45.4680, "lon": 9.1890},
    "target": [{"fascia": "preadolescenti"}, {"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 54,
    "imgs": [{"alt": "Scacchi", "src": "https://esempio.com/scacchi.jpg"}],
    "rank": {"stars": 3, "sponsored": false}
  }
}
```

- mock - Concerto di Musica Classica
```json
{
  "data": {
    "nome": "mock - Concerto di Musica Classica",
    "desc": "## Classica\nConcerto del quartetto d'archi con brani di Mozart e Beethoven.",
    "date_time": [{"st": "20261212T20:30:00UTC+01", "en": "20261212T22:30:00UTC+01"}],
    "luogo": {"name": "Conservatorio di Milano", "lat": 45.4638, "lon": 9.2001},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 55,
    "imgs": [{"alt": "Classica", "src": "https://esempio.com/classica.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Hackathon Sostenibilità
```json
{
  "data": {
    "nome": "mock - Hackathon Sostenibilità",
    "desc": "## Green Hackathon\n24 ore per sviluppare soluzioni tech per l'ambiente.",
    "date_time": [{"st": "20261215T09:00:00UTC+01", "en": "20261216T18:00:00UTC+01"}],
    "luogo": {"name": "Green Hub", "lat": 45.4762, "lon": 9.2040},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 56,
    "imgs": [{"alt": "Hackathon green", "src": "https://esempio.com/greenhack.jpg"}],
    "rank": {"stars": 5, "sponsored": true}
  }
}
```

- mock - Mercatino di Natale Artigianale
```json
{
  "data": {
    "nome": "mock - Mercatino di Natale Artigianale",
    "desc": "## Christmas Market\nProdotti artigianali, decorazioni e cibo tipico natalizio.",
    "date_time": [{"st": "20261218T11:00:00UTC+01", "en": "20261224T20:00:00UTC+01"}],
    "luogo": {"name": "Piazza Mercanti", "lat": 45.4644, "lon": 9.1873},
    "target": [{"fascia": "preadolescenti"}, {"fascia": "adolescenti"}, {"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 57,
    "imgs": [{"alt": "Natale", "src": "https://esempio.com/natale.jpg"}],
    "rank": {"stars": 4, "sponsored": true}
  }
}
```

- mock - Festa di Capodanno in Piazza
```json
{
  "data": {
    "nome": "mock - Festa di Capodanno in Piazza",
    "desc": "## New Year's Eve\nConto alla rovescia e fuochi d'artificio in piazza.",
    "date_time": [{"st": "20261231T22:00:00UTC+01", "en": "20270101T02:00:00UTC+01"}],
    "luogo": {"name": "Piazza del Duomo", "lat": 45.4642, "lon": 9.1900},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 58,
    "imgs": [{"alt": "Capodanno", "src": "https://esempio.com/capodanno.jpg"}],
    "rank": {"stars": 5, "sponsored": true}
  }
}
```

- mock - Corso di Produzione Musicale
```json
{
  "data": {
    "nome": "mock - Corso di Produzione Musicale",
    "desc": "## Music Production\nImpara a produrre musica con Ableton Live da zero.",
    "date_time": [{"st": "20270110T14:00:00UTC+01", "en": "20270110T18:00:00UTC+01"}],
    "luogo": {"name": "Recording Studio 44", "lat": 45.4745, "lon": 9.2020},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 59,
    "imgs": [{"alt": "Produzione musicale", "src": "https://esempio.com/music-prod.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Torneo di Freccette
```json
{
  "data": {
    "nome": "mock - Torneo di Freccette",
    "desc": "## Darts Tournament\nTorneo amatoriale di freccette con finale a premi.",
    "date_time": [{"st": "20270115T19:00:00UTC+01", "en": "20270115T23:00:00UTC+01"}],
    "luogo": {"name": "The Darts Pub", "lat": 45.4688, "lon": 9.1935},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 60,
    "imgs": [{"alt": "Freccette", "src": "https://esempio.com/darts.jpg"}],
    "rank": {"stars": 2, "sponsored": false}
  }
}
```

- mock - Laboratorio di Elettronica
```json
{
  "data": {
    "nome": "mock - Laboratorio di Elettronica",
    "desc": "## Electronics Lab\nCostruisci circuiti elettronici con componenti base.",
    "date_time": [{"st": "20270118T10:00:00UTC+01", "en": "20270118T13:00:00UTC+01"}],
    "luogo": {"name": "Maker Space Isola", "lat": 45.4845, "lon": 9.1890},
    "target": [{"fascia": "preadolescenti"}, {"fascia": "adolescenti"}],
    "org_id": 61,
    "imgs": [{"alt": "Elettronica", "src": "https://esempio.com/elettronica.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Degustazione di Vini Naturali
```json
{
  "data": {
    "nome": "mock - Degustazione di Vini Naturali",
    "desc": "## Natural Wine Tasting\nDegustazione guidata di vini naturali e biodinamici.",
    "date_time": [{"st": "20270122T18:30:00UTC+01", "en": "20270122T21:30:00UTC+01"}],
    "luogo": {"name": "Enoteca Naturale", "lat": 45.4670, "lon": 9.1800},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 62,
    "imgs": [{"alt": "Vino", "src": "https://esempio.com/vino.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Serata di Salsa e Bachata
```json
{
  "data": {
    "nome": "mock - Serata di Salsa e Bachata",
    "desc": "## Latin Night\nLezione introduttiva di salsa e bachata seguita da serata danzante.",
    "date_time": [{"st": "20270125T20:00:00UTC+01", "en": "20270126T01:00:00UTC+01"}],
    "luogo": {"name": "Club Latino", "lat": 45.4695, "lon": 9.1975},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 63,
    "imgs": [{"alt": "Salsa", "src": "https://esempio.com/salsa.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Campeggio Invernale
```json
{
  "data": {
    "nome": "mock - Campeggio Invernale",
    "desc": "## Winter Camp\nWeekend di campeggio invernale con attività all'aperto nella neve.",
    "date_time": [{"st": "20270201T08:00:00UTC+01", "en": "20270202T18:00:00UTC+01"}],
    "luogo": {"name": "Rifugio Alpe Devero", "lat": 46.2833, "lon": 8.3167},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 64,
    "imgs": [{"alt": "Campeggio", "src": "https://esempio.com/campeggio.jpg"}],
    "rank": {"stars": 5, "sponsored": false}
  }
}
```

- mock - Serata Retrogaming
```json
{
  "data": {
    "nome": "mock - Serata Retrogaming",
    "desc": "## Retrogaming Night\nGioca con console vintage anni 80 e 90 in libertà.",
    "date_time": [{"st": "20270205T17:00:00UTC+01", "en": "20270205T22:00:00UTC+01"}],
    "luogo": {"name": "Arcade Nostalgia", "lat": 45.4720, "lon": 9.1860},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 65,
    "imgs": [{"alt": "Retrogaming", "src": "https://esempio.com/retro.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Workshop di Illustrazione Digitale
```json
{
  "data": {
    "nome": "mock - Workshop di Illustrazione Digitale",
    "desc": "## Digital Illustration\nImpara a disegnare digitalmente con Procreate su iPad.",
    "date_time": [{"st": "20270208T14:00:00UTC+01", "en": "20270208T17:00:00UTC+01"}],
    "luogo": {"name": "Creative Studio Brera", "lat": 45.4725, "lon": 9.1870},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 66,
    "imgs": [{"alt": "Illustrazione", "src": "https://esempio.com/illustration.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Serata di Birdwatching
```json
{
  "data": {
    "nome": "mock - Serata di Birdwatching",
    "desc": "## Birdwatching\nOsservazione degli uccelli migratori all'alba nel parco naturale.",
    "date_time": [{"st": "20270212T06:30:00UTC+01", "en": "20270212T10:00:00UTC+01"}],
    "luogo": {"name": "Oasi WWF Vanzago", "lat": 45.5270, "lon": 8.9970},
    "target": [{"fascia": "preadolescenti"}, {"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 67,
    "imgs": [{"alt": "Birdwatching", "src": "https://esempio.com/birds.jpg"}],
    "rank": {"stars": 3, "sponsored": false}
  }
}
```

- mock - Corso di Difesa Personale
```json
{
  "data": {
    "nome": "mock - Corso di Difesa Personale",
    "desc": "## Self Defense\nLezioni base di difesa personale per ragazze e ragazzi.",
    "date_time": [{"st": "20270215T17:00:00UTC+01", "en": "20270215T19:00:00UTC+01"}],
    "luogo": {"name": "Palestra Krav Maga", "lat": 45.4755, "lon": 9.2010},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 68,
    "imgs": [{"alt": "Difesa personale", "src": "https://esempio.com/selfdefense.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Serata Letteraria
```json
{
  "data": {
    "nome": "mock - Serata Letteraria",
    "desc": "## Book Night\nLetture ad alta voce e discussione su romanzi contemporanei.",
    "date_time": [{"st": "20270218T18:30:00UTC+01", "en": "20270218T21:00:00UTC+01"}],
    "luogo": {"name": "Libreria Gogol", "lat": 45.4655, "lon": 9.1875},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 69,
    "imgs": [{"alt": "Letteratura", "src": "https://esempio.com/libri2.jpg"}],
    "rank": {"stars": 3, "sponsored": false}
  }
}
```

- mock - Torneo di Badminton
```json
{
  "data": {
    "nome": "mock - Torneo di Badminton",
    "desc": "## Badminton\nTorneo amatoriale di badminton in singolo e doppio.",
    "date_time": [{"st": "20270222T10:00:00UTC+01", "en": "20270222T17:00:00UTC+01"}],
    "luogo": {"name": "Palasport Saini", "lat": 45.4830, "lon": 9.2310},
    "target": [{"fascia": "preadolescenti"}, {"fascia": "adolescenti"}],
    "org_id": 70,
    "imgs": [{"alt": "Badminton", "src": "https://esempio.com/badminton.jpg"}],
    "rank": {"stars": 3, "sponsored": false}
  }
}
```

- mock - Laboratorio di Cucito e Moda
```json
{
  "data": {
    "nome": "mock - Laboratorio di Cucito e Moda",
    "desc": "## Fashion Lab\nImpara a cucire e personalizzare i tuoi abiti.",
    "date_time": [{"st": "20270225T14:00:00UTC+01", "en": "20270225T17:00:00UTC+01"}],
    "luogo": {"name": "Atelier Creativo", "lat": 45.4700, "lon": 9.1820},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 71,
    "imgs": [{"alt": "Moda", "src": "https://esempio.com/moda.jpg"}],
    "rank": {"stars": 3, "sponsored": false}
  }
}
```

- mock - Serata Culturale Interculturale
```json
{
  "data": {
    "nome": "mock - Serata Culturale Interculturale",
    "desc": "## World Night\nCibo, musica e tradizioni da 10 Paesi diversi in una serata.",
    "date_time": [{"st": "20270301T18:00:00UTC+01", "en": "20270301T23:00:00UTC+01"}],
    "luogo": {"name": "Casa delle Culture", "lat": 45.4680, "lon": 9.1900},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 72,
    "imgs": [{"alt": "Intercultura", "src": "https://esempio.com/world.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Corso di Parkour
```json
{
  "data": {
    "nome": "mock - Corso di Parkour",
    "desc": "## Parkour Base\nLezione introduttiva al parkour in sicurezza.",
    "date_time": [{"st": "20270305T15:00:00UTC+01", "en": "20270305T18:00:00UTC+01"}],
    "luogo": {"name": "Piazzale Lugano", "lat": 45.4890, "lon": 9.1750},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 73,
    "imgs": [{"alt": "Parkour", "src": "https://esempio.com/parkour.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Serata di Improvvisazione Musicale
```json
{
  "data": {
    "nome": "mock - Serata di Improvvisazione Musicale",
    "desc": "## Jam Session\nJam session aperta a tutti gli strumentisti.",
    "date_time": [{"st": "20270308T20:00:00UTC+01", "en": "20270308T23:30:00UTC+01"}],
    "luogo": {"name": "Circolo Ohibò", "lat": 45.4820, "lon": 9.1700},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 74,
    "imgs": [{"alt": "Jam session", "src": "https://esempio.com/jam.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Workshop di Candle Making
```json
{
  "data": {
    "nome": "mock - Workshop di Candle Making",
    "desc": "## Candele Fai da Te\nCrea le tue candele profumate personalizzate.",
    "date_time": [{"st": "20270312T15:00:00UTC+01", "en": "20270312T17:30:00UTC+01"}],
    "luogo": {"name": "Studio DIY", "lat": 45.4665, "lon": 9.1845},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 75,
    "imgs": [{"alt": "Candele", "src": "https://esempio.com/candles.jpg"}],
    "rank": {"stars": 3, "sponsored": false}
  }
}
```

- mock - Torneo di Tennis
```json
{
  "data": {
    "nome": "mock - Torneo di Tennis",
    "desc": "## Tennis Open\nTorneo amatoriale di tennis su terra battuta.",
    "date_time": [{"st": "20270315T09:00:00UTC+01", "en": "20270315T18:00:00UTC+01"}],
    "luogo": {"name": "Tennis Club Bonacossa", "lat": 45.4780, "lon": 9.1680},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 76,
    "imgs": [{"alt": "Tennis", "src": "https://esempio.com/tennis.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Serata di Circo Contemporaneo
```json
{
  "data": {
    "nome": "mock - Serata di Circo Contemporaneo",
    "desc": "## Circo Moderno\nSpettacolo di circo contemporaneo con acrobati e giocolieri.",
    "date_time": [{"st": "20270318T20:30:00UTC+01", "en": "20270318T22:30:00UTC+01"}],
    "luogo": {"name": "Tendone Circo", "lat": 45.4610, "lon": 9.2100},
    "target": [{"fascia": "preadolescenti"}, {"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 77,
    "imgs": [{"alt": "Circo", "src": "https://esempio.com/circo.jpg"}],
    "rank": {"stars": 5, "sponsored": false}
  }
}
```

- mock - Corso di Web Development
```json
{
  "data": {
    "nome": "mock - Corso di Web Development",
    "desc": "## Web Dev Intro\nImpara HTML, CSS e JavaScript partendo da zero.",
    "date_time": [{"st": "20270322T09:00:00UTC+01", "en": "20270322T13:00:00UTC+01"}],
    "luogo": {"name": "Digital School", "lat": 45.4770, "lon": 9.2050},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 78,
    "imgs": [{"alt": "Web dev", "src": "https://esempio.com/webdev.jpg"}],
    "rank": {"stars": 5, "sponsored": true}
  }
}
```

- mock - Fiera della Sostenibilità
```json
{
  "data": {
    "nome": "mock - Fiera della Sostenibilità",
    "desc": "## Green Fair\nProdotti eco-sostenibili, workshop e talk sul futuro verde.",
    "date_time": [{"st": "20270325T10:00:00UTC+01", "en": "20270325T19:00:00UTC+01"}],
    "luogo": {"name": "Fabbrica del Vapore", "lat": 45.4790, "lon": 9.1720},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 79,
    "imgs": [{"alt": "Sostenibilità", "src": "https://esempio.com/green.jpg"}],
    "rank": {"stars": 4, "sponsored": true}
  }
}
```

- mock - Serata Speed Friending
```json
{
  "data": {
    "nome": "mock - Serata Speed Friending",
    "desc": "## Speed Friending\nConosci nuove persone con mini conversazioni da 3 minuti.",
    "date_time": [{"st": "20270328T19:00:00UTC+01", "en": "20270328T22:00:00UTC+01"}],
    "luogo": {"name": "Social Club Brera", "lat": 45.4725, "lon": 9.1870},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 80,
    "imgs": [{"alt": "Speed friending", "src": "https://esempio.com/friending.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Laboratorio di Origami
```json
{
  "data": {
    "nome": "mock - Laboratorio di Origami",
    "desc": "## Origami\nImpara le tecniche base e avanzate dell'arte della carta giapponese.",
    "date_time": [{"st": "20270401T15:00:00UTC+02", "en": "20270401T17:30:00UTC+02"}],
    "luogo": {"name": "Centro Culturale Giapponese", "lat": 45.4710, "lon": 9.1965},
    "target": [{"fascia": "preadolescenti"}, {"fascia": "adolescenti"}],
    "org_id": 81,
    "imgs": [{"alt": "Origami", "src": "https://esempio.com/origami.jpg"}],
    "rank": {"stars": 3, "sponsored": false}
  }
}
```

- mock - Serata di Pole Dance Fitness
```json
{
  "data": {
    "nome": "mock - Serata di Pole Dance Fitness",
    "desc": "## Pole Fitness\nLezione introduttiva di pole dance come disciplina sportiva.",
    "date_time": [{"st": "20270405T18:00:00UTC+02", "en": "20270405T20:00:00UTC+02"}],
    "luogo": {"name": "Studio Pole Art", "lat": 45.4735, "lon": 9.2000},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 82,
    "imgs": [{"alt": "Pole dance", "src": "https://esempio.com/pole.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Tour in Kayak sul Lago
```json
{
  "data": {
    "nome": "mock - Tour in Kayak sul Lago",
    "desc": "## Kayak Tour\nEscursione in kayak sul Lago Maggiore con guida esperta.",
    "date_time": [{"st": "20270410T09:00:00UTC+02", "en": "20270410T14:00:00UTC+02"}],
    "luogo": {"name": "Lago Maggiore - Arona", "lat": 45.7566, "lon": 8.5597},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 83,
    "imgs": [{"alt": "Kayak", "src": "https://esempio.com/kayak.jpg"}],
    "rank": {"stars": 5, "sponsored": false}
  }
}
```

- mock - Concorso di Street Photography
```json
{
  "data": {
    "nome": "mock - Concorso di Street Photography",
    "desc": "## Street Photo Contest\nInvia le tue foto di strada e vinci premi.",
    "date_time": [{"st": "20270415T00:00:00UTC+02", "en": "20270430T23:59:00UTC+02"}],
    "luogo": {"name": "Online + Mostra finale a Milano", "lat": 45.4642, "lon": 9.1900},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 84,
    "imgs": [{"alt": "Street photo", "src": "https://esempio.com/streetphoto.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Serata di Mindfulness e Journaling
```json
{
  "data": {
    "nome": "mock - Serata di Mindfulness e Journaling",
    "desc": "## Mindfulness Night\nSessione guidata di mindfulness e scrittura riflessiva.",
    "date_time": [{"st": "20270418T18:00:00UTC+02", "en": "20270418T20:30:00UTC+02"}],
    "luogo": {"name": "Spazio Quiete", "lat": 45.4665, "lon": 9.1860},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 85,
    "imgs": [{"alt": "Mindfulness", "src": "https://esempio.com/mindfulness.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Torneo di Ultimate Frisbee
```json
{
  "data": {
    "nome": "mock - Torneo di Ultimate Frisbee",
    "desc": "## Ultimate Frisbee\nTorneo misto di ultimate frisbee in stile spirito del gioco.",
    "date_time": [{"st": "20270422T10:00:00UTC+02", "en": "20270422T18:00:00UTC+02"}],
    "luogo": {"name": "Campo Coltivato Lambro", "lat": 45.4490, "lon": 9.2400},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 86,
    "imgs": [{"alt": "Frisbee", "src": "https://esempio.com/frisbee.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Workshop di Animazione 2D
```json
{
  "data": {
    "nome": "mock - Workshop di Animazione 2D",
    "desc": "## Animazione\nCrea il tuo primo cortometraggio animato con tecniche digitali.",
    "date_time": [{"st": "20270425T14:00:00UTC+02", "en": "20270425T18:00:00UTC+02"}],
    "luogo": {"name": "NABA Milano", "lat": 45.4762, "lon": 9.2050},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 87,
    "imgs": [{"alt": "Animazione", "src": "https://esempio.com/animation.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Primo Maggio - Concerto Alternativo
```json
{
  "data": {
    "nome": "mock - Primo Maggio - Concerto Alternativo",
    "desc": "## Concerto 1 Maggio\nFestival musicale alternativo per celebrare la Festa dei Lavoratori.",
    "date_time": [{"st": "20270501T16:00:00UTC+02", "en": "20270501T23:59:00UTC+02"}],
    "luogo": {"name": "Arco della Pace", "lat": 45.4762, "lon": 9.1700},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 88,
    "imgs": [{"alt": "Concerto", "src": "https://esempio.com/1maggio.jpg"}],
    "rank": {"stars": 5, "sponsored": true}
  }
}
```

- mock - Corso di Barista
```json
{
  "data": {
    "nome": "mock - Corso di Barista",
    "desc": "## Barista Course\nImpara a preparare espresso, cappuccino e latte art.",
    "date_time": [{"st": "20270505T10:00:00UTC+02", "en": "20270505T13:00:00UTC+02"}],
    "luogo": {"name": "Accademia del Caffè", "lat": 45.4695, "lon": 9.1920},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 89,
    "imgs": [{"alt": "Caffè", "src": "https://esempio.com/caffe.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Serata Pride
```json
{
  "data": {
    "nome": "mock - Serata Pride",
    "desc": "## Pride Night\nFesta di celebrazione dell'identità e dell'inclusione.",
    "date_time": [{"st": "20270508T20:00:00UTC+02", "en": "20270509T02:00:00UTC+02"}],
    "luogo": {"name": "Circolo Arci Bellezza", "lat": 45.4580, "lon": 9.1880},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 90,
    "imgs": [{"alt": "Pride", "src": "https://esempio.com/pride.jpg"}],
    "rank": {"stars": 5, "sponsored": true}
  }
}
```

- mock - Laboratorio di Slime e Chimica
```json
{
  "data": {
    "nome": "mock - Laboratorio di Slime e Chimica",
    "desc": "## Science Lab\nEsperimenti divertenti di chimica per ragazzi.",
    "date_time": [{"st": "20270512T15:00:00UTC+02", "en": "20270512T17:00:00UTC+02"}],
    "luogo": {"name": "Museo della Scienza", "lat": 45.4632, "lon": 9.1738},
    "target": [{"fascia": "preadolescenti"}],
    "org_id": 91,
    "imgs": [{"alt": "Chimica", "src": "https://esempio.com/chimica.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Serata di Spoken Word
```json
{
  "data": {
    "nome": "mock - Serata di Spoken Word",
    "desc": "## Spoken Word\nPerformance di poesia parlata e storytelling dal vivo.",
    "date_time": [{"st": "20270515T19:30:00UTC+02", "en": "20270515T22:00:00UTC+02"}],
    "luogo": {"name": "Spazio Teatro 89", "lat": 45.4870, "lon": 9.1650},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 92,
    "imgs": [{"alt": "Spoken word", "src": "https://esempio.com/spoken.jpg"}],
    "rank": {"stars": 3, "sponsored": false}
  }
}
```

- mock - Corso di Permacultura
```json
{
  "data": {
    "nome": "mock - Corso di Permacultura",
    "desc": "## Permacultura\nPrincipi base della permacultura e coltivazione sostenibile.",
    "date_time": [{"st": "20270518T10:00:00UTC+02", "en": "20270518T16:00:00UTC+02"}],
    "luogo": {"name": "Orto Comunitario Lambrate", "lat": 45.4810, "lon": 9.2380},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 93,
    "imgs": [{"alt": "Permacultura", "src": "https://esempio.com/permacultura.jpg"}],
    "rank": {"stars": 3, "sponsored": false}
  }
}
```

- mock - Torneo di Ping Pong Freestyle
```json
{
  "data": {
    "nome": "mock - Torneo di Ping Pong Freestyle",
    "desc": "## Freestyle Ping Pong\nGara di trick shot e freestyle con la racchetta.",
    "date_time": [{"st": "20270522T16:00:00UTC+02", "en": "20270522T20:00:00UTC+02"}],
    "luogo": {"name": "Piazza XXIV Maggio", "lat": 45.4558, "lon": 9.1775},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 94,
    "imgs": [{"alt": "Ping pong freestyle", "src": "https://esempio.com/ppfreestyle.jpg"}],
    "rank": {"stars": 3, "sponsored": false}
  }
}
```

- mock - Laboratorio di Birra Fatta in Casa
```json
{
  "data": {
    "nome": "mock - Laboratorio di Birra Fatta in Casa",
    "desc": "## Homebrewing\nImpara a produrre la tua birra artigianale partendo da zero.",
    "date_time": [{"st": "20270525T14:00:00UTC+02", "en": "20270525T18:00:00UTC+02"}],
    "luogo": {"name": "Birrificio Artigianale", "lat": 45.4730, "lon": 9.2100},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 95,
    "imgs": [{"alt": "Homebrewing", "src": "https://esempio.com/homebrewing.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Serata di Fotografia Notturna
```json
{
  "data": {
    "nome": "mock - Serata di Fotografia Notturna",
    "desc": "## Night Photography\nEsplorazione fotografica notturna della città con un fotografo professionista.",
    "date_time": [{"st": "20270528T22:00:00UTC+02", "en": "20270529T01:00:00UTC+02"}],
    "luogo": {"name": "Quartiere Navigli", "lat": 45.4530, "lon": 9.1700},
    "target": [{"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 96,
    "imgs": [{"alt": "Fotografia notturna", "src": "https://esempio.com/nightphoto.jpg"}],
    "rank": {"stars": 4, "sponsored": false}
  }
}
```

- mock - Festival Hip Hop
```json
{
  "data": {
    "nome": "mock - Festival Hip Hop",
    "desc": "## Hip Hop Fest\nDue giorni di musica, danza, graffiti e cultura hip hop.",
    "date_time": [{"st": "20270601T14:00:00UTC+02", "en": "20270602T23:00:00UTC+02"}],
    "luogo": {"name": "Parco Trotter", "lat": 45.4920, "lon": 9.2210},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 97,
    "imgs": [{"alt": "Hip hop fest", "src": "https://esempio.com/hiphopfest.jpg"}],
    "rank": {"stars": 5, "sponsored": true}
  }
}
```

- mock - Corso di Primo Soccorso
```json
{
  "data": {
    "nome": "mock - Corso di Primo Soccorso",
    "desc": "## First Aid\nLezione pratica di primo soccorso e manovre di rianimazione.",
    "date_time": [{"st": "20270605T09:00:00UTC+02", "en": "20270605T13:00:00UTC+02"}],
    "luogo": {"name": "Croce Rossa Milano", "lat": 45.4760, "lon": 9.2000},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 98,
    "imgs": [{"alt": "Primo soccorso", "src": "https://esempio.com/firstaid.jpg"}],
    "rank": {"stars": 5, "sponsored": false}
  }
}
```

- mock - Serata di Stargazing Urbano
```json
{
  "data": {
    "nome": "mock - Serata di Stargazing Urbano",
    "desc": "## Urban Stargazing\nOsservazione delle stelle dal tetto di un palazzo con telescopio.",
    "date_time": [{"st": "20270608T22:00:00UTC+02", "en": "20270609T01:00:00UTC+02"}],
    "luogo": {"name": "Terrazza Triennale", "lat": 45.4716, "lon": 9.1755},
    "target": [{"fascia": "adolescenti"}, {"fascia": "giovani"}, {"fascia": "giovani_adulti"}],
    "org_id": 99,
    "imgs": [{"alt": "Stargazing", "src": "https://esempio.com/stargazing.jpg"}],
    "rank": {"stars": 5, "sponsored": false}
  }
}
```

- mock - Torneo di Calcio Balilla
```json
{
  "data": {
    "nome": "mock - Torneo di Calcio Balilla",
    "desc": "## Biliardino\nGran torneo di calcio balilla a coppie con premi finali.",
    "date_time": [{"st": "20270612T17:00:00UTC+02", "en": "20270612T22:00:00UTC+02"}],
    "luogo": {"name": "Bar Sport Centrale", "lat": 45.4672, "lon": 9.1895},
    "target": [{"fascia": "preadolescenti"}, {"fascia": "adolescenti"}, {"fascia": "giovani"}],
    "org_id": 100,
    "imgs": [{"alt": "Calcio balilla", "src": "https://esempio.com/biliardino.jpg"}],
    "rank": {"stars": 3, "sponsored": false}
  }
}
```
