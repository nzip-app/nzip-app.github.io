# Formato di archivio .nzip — specifica, versione 1.1

Questo documento descrive in modo completo il formato dei file `.nzip` prodotti da NZip.
È pubblico di proposito: chiunque deve poter scrivere un denzip partendo da qui,
anche se un giorno il software originale non esistesse più.

Implementazione di riferimento: `src/core/` (C++17, portabile: Windows, Linux, macOS, x64 e ARM64).

**Versioni del formato.** 1.0 (NZip 3.1): tutto ciò che è descritto qui tranne la trasformazione 3.
1.1 (NZip 3.2): aggiunge la trasformazione 3 (§8.3, pixel dei PNG in JPEG XL senza perdita). Gli archivi
che la usano hanno "livello minimo del lettore" = 2 nell'intestazione; tutti gli altri restano a 1 e sono
leggibili anche dai programmi per il formato 1.0.

---

## 1. Principi (non negoziabili)

1. **Un archivio si apre sempre, su qualunque PC.** La decodifica usa solo aritmetica intera
   e non dipende dal processore, dal sistema operativo, dalla lingua o da risorse esterne.
2. **Identificatori congelati.** I numeri di codec, filtri e trasformazioni (§6–§8), una volta pubblicati,
   non cambiano mai significato. Le versioni nuove *aggiungono* identificatori, non ne tolgono.
3. **Tutto ha un checksum.** Intestazione, blocchi, indice e chiusura sono protetti.
   Ogni file estratto viene confrontato con il suo hash BLAKE3.
4. **Compatibilità in avanti.** Un lettore che trova un identificatore sconosciuto rifiuta *solo*
   i dati che lo usano, con un messaggio chiaro, e continua a estrarre il resto.

Tutti gli interi sono **little-endian**. Le date sono FILETIME di Windows
(intervalli di 100 ns dal 1° gennaio 1601, UTC). I percorsi sono UTF-8 con separatore `/`.

---

## 2. Struttura generale

```
+-----------------------+  offset 0
| Intestazione (64 B)   |
+-----------------------+
| Blocco 0              |  intestazione di blocco (64 B) + dati compressi
| Blocco 1              |
| ...                   |
+-----------------------+  footer.dataEnd
| Indice                |  stessa struttura di un blocco, magic "ZIDX"
| Copia dell'indice     |  byte per byte identica alla precedente
+-----------------------+
| Chiusura (64 B)       |  "footer"
+-----------------------+
| Dati di ripristino    |  opzionali (§9)
| Coda di ripristino 64B|
+-----------------------+  fine del file
```

Per leggere un archivio: leggere l'intestazione, poi gli ultimi 64 byte. Se sono la chiusura
(magic `NZEND`), leggerla; se sono la coda di ripristino (magic `NZTAIL`), usare l'offset
della chiusura che vi è indicato. Poi leggere l'indice (o la sua copia, se il primo è danneggiato).

### Hash usati

| Uso | Algoritmo |
|---|---|
| Checksum di intestazioni, blocchi, chiusura | XXH3-64 (`XXH3_64bits`, seme 0) |
| Identità dei file e dei frammenti | BLAKE3 (32 byte; i frammenti usano i primi 16) |

Una struttura "sigillata" di 64 byte ha negli ultimi 8 byte l'XXH3-64 dei primi 56.

---

## 3. Intestazione (64 byte, offset 0)

| Offset | Dim. | Campo |
|---|---|---|
| 0 | 8 | Magic: `4E 5A 49 50 1A 0D 0A 00` (`"NZIP"`, 0x1A, CR, LF, 0x00) |
| 8 | 2 | Versione del formato, maggiore (= 1) |
| 10 | 2 | Versione del formato, minore (= 1; 0 negli archivi di NZip 3.1) |
| 12 | 2 | Livello minimo del lettore: 1 = formato 1.0, 2 = serve anche la trasformazione 3 (§8.3). Se maggiore di quello supportato: rifiutare l'archivio intero con un messaggio chiaro ("serve una versione più recente"). |
| 14 | 2 | Flag: bit 0 = archivio protetto da password (§9bis) |
| 16 | 16 | ID casuale dell'archivio |
| 32 | 8 | Data di creazione (FILETIME) |
| 40 | 6 | Versione del programma creatore (maggiore, minore, patch; 2 byte ciascuno) |
| 46 | 10 | Riservati (0) |
| 56 | 8 | XXH3-64 dei byte 0–55 |

Il magic contiene i byte 0x1A, CR e LF per rilevare trasferimenti in modalità testo (come PNG).

---

## 4. Blocchi

I dati dei file sono divisi in **frammenti** (§5.2) e concatenati in **blocchi**. Ogni blocco
contiene frammenti di una sola **classe** e viene compresso in modo indipendente dagli altri.

### Intestazione di blocco (64 byte)

| Offset | Dim. | Campo |
|---|---|---|
| 0 | 4 | Magic `ZBLK` (0x4B4C425A); per l'indice `ZIDX` (0x5844495A) |
| 4 | 4 | Numero del blocco (0, 1, 2… in ordine; 0xFFFFFFFF per l'indice) |
| 8 | 1 | Classe (§4.1) |
| 9 | 1 | Codec (§6) |
| 10 | 1 | Filtro (§7) |
| 11 | 1 | Riservato |
| 12 | 4 | Flag (0) |
| 16 | 8 | Dimensione decompressa |
| 24 | 8 | Dimensione compressa (byte che seguono l'intestazione) |
| 32 | 8 | XXH3-64 dei dati decompressi |
| 40 | 8 | XXH3-64 dei dati compressi |
| 48 | 8 | Riservati |
| 56 | 8 | XXH3-64 dei byte 0–55 |

Decodifica: verificare il sigillo, verificare l'XXH3 dei dati compressi, decodificare con il codec,
applicare il filtro inverso, verificare l'XXH3 dei dati decompressi. La dimensione decompressa
di un blocco non supera 4 GiB.

### 4.1 Classi (informative)

`0` memorizzato, `1` testo, `2` binario, `3` eseguibili x86/x64, `4` eseguibili ARM64, `255` indice.
La classe è solo informativa: la decodifica dipende esclusivamente da codec e filtro.

---

## 5. Indice

L'indice è memorizzato come un blocco con magic `ZIDX`, codec zstd (1), filtro 0.
Una volta decompresso ha questa struttura (`var` = intero senza segno LEB128;
`svar` = intero con segno zig-zag + LEB128):

```
u32   magic "ZIDX"
var   versione dell'indice (= 1)

var   numero di blocchi B
B volte:
  var  offset dell'intestazione del blocco nel file
  u8   classe
  u8   codec
  u8   filtro
  var  dimensione decompressa
  var  dimensione compressa
  u64  XXH3-64 dei dati decompressi

var   numero di frammenti C
C volte:
  var  numero del blocco
  var  dimensione del frammento
  16 B primi 16 byte del BLAKE3 del frammento

var   numero di voci E
E volte:
  var  lunghezza del percorso, poi il percorso in UTF-8
  u8   tipo: 0 = file, 1 = cartella
  var  attributi (0x1 sola lettura, 0x2 nascosto, 0x4 sistema, 0x20 archivio)
  u64  data di modifica (FILETIME)
  u64  data di creazione (FILETIME)
  se file:
    var  dimensione originale
    32 B BLAKE3 del contenuto originale
    u8   trasformazione (§8)
    var  dimensione della rappresentazione memorizzata
    var  numero di frammenti K
    K volte: svar  (indice del frammento − indice precedente − 1), con precedente iniziale = −1

var   numero di record di estensione X  (versione 1: 0)
X volte: var etichetta, var lunghezza, dati   (i lettori ignorano le etichette sconosciute)
```

### 5.1 Posizione dei frammenti

L'offset di un frammento **non è memorizzato**: dentro ogni blocco i frammenti sono consecutivi
nell'ordine in cui compaiono nella tabella. L'offset del frammento *i* è la somma delle dimensioni
dei frammenti precedenti dello stesso blocco. La somma non deve superare la dimensione del blocco.

### 5.2 Frammenti condivisi

Più file (o più punti dello stesso file) possono riferirsi allo stesso frammento.
Il contenuto memorizzato di un file è la concatenazione dei suoi frammenti, nell'ordine indicato.

### 5.3 Controlli obbligatori del lettore

- ogni riferimento (blocco, frammento) deve essere nell'intervallo valido;
- la somma dei frammenti di un file deve essere uguale alla sua dimensione memorizzata;
- senza trasformazione, dimensione memorizzata = dimensione originale;
- **percorsi**: rifiutare percorsi vuoti, assoluti, con `..`, `.`, componenti vuote, `:` o caratteri
  di controllo (protezione contro la scrittura fuori dalla cartella di destinazione);
- dopo l'estrazione, il BLAKE3 del file deve coincidere con quello dell'indice.

---

## 6. Codec (identificatori congelati)

| ID | Nome | Contenuto del blocco |
|---|---|---|
| 0 | Memorizzato | I dati così come sono |
| 1 | Zstandard | Un frame zstd completo (RFC 8878) |
| 2 | LZMA | 5 byte di proprietà LZMA (lc/lp/pb + dizionario) seguiti dal flusso LZMA **senza** marcatore di fine; la lunghezza è la dimensione decompressa del blocco |
| 3 | PPMd | 1 byte ordine (2–64), 4 byte memoria (LE, ≤ 1 GiB), poi flusso PPMd var.H con il range coder di 7-Zip ("Ppmd7z") |

Implementazioni di riferimento: zstd 1.5.7, LZMA SDK 26.02 (Igor Pavlov, pubblico dominio).

## 7. Filtri (identificatori congelati)

Applicati ai dati **prima** della compressione; il lettore applica l'inverso **dopo** la decompressione.

| ID | Filtro |
|---|---|
| 0 | Nessuno |
| 1 | x86/x64 (BCJ, conversione di CALL/JMP relativi in assoluti), stato iniziale 0, PC iniziale 0 — `z7_BranchConvSt_X86_Dec` dell'LZMA SDK |
| 2 | ARM64 (BL/ADRP), PC iniziale 0 — `z7_BranchConv_ARM64_Dec` dell'LZMA SDK |

## 8. Trasformazioni (identificatori congelati)

Una trasformazione sostituisce il contenuto del file con una rappresentazione che comprime meglio.
L'inversa deve ricreare il file **bit per bit**: la verifica BLAKE3 finale lo garantisce.

### 8.1 Trasformazione 1: contenitore deflate

Usata per zlib, gzip, PNG, ZIP (quindi DOCX, XLSX, PPTX, JAR, APK, NUPKG…), PDF, pacchetti git.
Il file originale è visto come una sequenza di **segmenti**: byte letterali e pezzi di flussi deflate.

```
u8   versione del layout (= 1)
var  dimensione originale
var  numero di segmenti S
S volte:
  u8   tipo: 0 = letterale, 1 = continua il flusso corrente, 2 = inizia il flusso successivo
  var  lunghezza in byte nel file originale
var  numero di flussi F
F volte:
  var  lunghezza del flusso deflate ricostruito
  var  lunghezza dei dati decompressi
  var  lunghezza delle informazioni di ricostruzione
var  lunghezza totale dei letterali, poi i letterali concatenati
     informazioni di ricostruzione dei flussi, concatenate
     dati decompressi dei flussi, concatenati
```

Ricostruzione: per ogni flusso, il flusso deflate originale si ottiene con
`preflate_reencode(informazioni, dati decompressi)` della libreria **preflate 0.3.5**
(Dirk Steinke, Apache 2.0; il formato delle informazioni di ricostruzione è quello della libreria).
Poi si percorrono i segmenti: i letterali si copiano, i pezzi di flusso si prendono in ordine dal flusso corrente.
Un flusso può essere spezzato in più pezzi (come i chunk IDAT di un PNG).

### 8.2 Trasformazione 2: JPEG

`u8` versione (= 1), seguito da un flusso **brunsli** (Google, MIT). La decodifica brunsli ricrea il JPEG identico.

### 8.3 Trasformazione 3: PNG con pixel in JPEG XL (formato 1.1, livello del lettore 2)

Per PNG non interlacciati a 8 o 16 bit (grigio, RGB, tavolozza a 8 bit, grigio + alfa, RGBA) con un solo
flusso zlib nei chunk IDAT. I dati IDAT decompressi sono righe "byte di filtro + campioni filtrati"
(filtri PNG 0–4: nessuno, Sub, Up, Average, Paeth). I filtri vengono tolti, i pixel veri sono codificati
con **JPEG XL senza perdita** (libjxl 0.12.0, BSD 3-Clause) e il resto del file è un contenitore deflate (§8.1).

```
u8   versione del layout (= 1)
var  larghezza W
var  altezza H
u8   profondità in bit (8 o 16)
u8   tipo di colore PNG (0, 2, 3, 4, 6)
H byte: il byte di filtro di ogni riga (0–4)
var  lunghezza C del contenitore
C byte: contenitore deflate (§8.1) con un solo flusso, i cui "dati decompressi" hanno lunghezza 0
resto: codestream JPEG XL (senza contenitore ISOBMFF)
```

Il codestream contiene W × H pixel con 1 (grigio, o indice della tavolozza), 2 (grigio + alfa), 3 (RGB) o 4
(RGBA) campioni, alla profondità indicata, profilo sRGB, senza perdita. Ricostruzione:

1. decodificare il codestream in campioni interi senza segno a 8 o 16 bit (16 bit: big endian, come nel PNG),
   nell'ordine dei canali del PNG;
2. per ogni riga y, applicare il filtro indicato dal suo byte (come fa un codificatore PNG, con i byte per
   pixel = canali × profondità / 8) e anteporre il byte di filtro: si ottengono i dati IDAT decompressi originali;
3. usare questi dati come "dati decompressi" dell'unico flusso del contenitore deflate e procedere come in §8.1.

Un lettore che non supporta la trasformazione 3 non deve estrarre il file: il campo "livello minimo del
lettore" gli fa rifiutare l'archivio prima ancora di leggerne il contenuto.

---

## 9. Dati di ripristino (opzionali)

Proteggono i byte `[0, P)` dell'archivio, dove P è la dimensione dell'archivio fino alla chiusura inclusa.

- Il file è diviso in **sezioni** di `S` byte (l'ultima completata con zeri). La sezione *i* appartiene
  al gruppo `i mod G` con posizione `i div G` (le sezioni vicine finiscono in gruppi diversi).
- Ogni gruppo ha `k ≤ 200` sezioni di dati e `m` sezioni di parità Reed-Solomon su GF(2^8)
  (polinomio 0x11D), con matrice di Cauchy: coefficiente(parità *j*, dato *s*) = 1 / ((j + k) XOR s).
- Parità *j* del gruppo *g* = Σ_s coeff(j, s) · sezione(g, s), byte per byte.

Struttura aggiunta dopo la chiusura:

```
Intestazione di ripristino (64 B): magic "NZREC" 1A 0D 0A, u16 versione = 1 @8,
   u64 P @16, u32 S @24, u32 G @28, u32 k @32, u32 m @36, u64 numero di sezioni @40, XXH3 @56
Tabella: XXH3-64 di ogni sezione di dati, poi di ogni sezione di parità (gruppo per gruppo)
Parità: G × m sezioni di S byte (gruppo 0 parità 0, gruppo 0 parità 1, …)
Copia dell'intestazione di ripristino e della tabella
Coda (64 B): magic "NZTAIL" 0D 0A, u64 offset dei dati di ripristino @8,
   u64 offset della chiusura @16, u64 lunghezza della sezione @24, XXH3 @56
```

Riparazione: individuare le sezioni danneggiate confrontando gli XXH3; per ogni gruppo con al massimo
*m* sezioni danneggiate, risolvere il sistema di Cauchy con le parità intatte.

---

## 9bis. Protezione con password

Se il bit 0 dei flag dell'intestazione è attivo, subito dopo l'intestazione (offset 64) c'è il
**record chiave** (64 byte) e i blocchi iniziano all'offset 128.

| Offset | Dim. | Campo |
|---|---|---|
| 0 | 8 | Magic `4E 5A 4B 45 59 1A 0D 0A` (`"NZKEY"`, 0x1A, CR, LF) |
| 8 | 2 | Versione (= 1) |
| 10 | 1 | Derivazione della chiave: 1 = PBKDF2-HMAC-SHA256 |
| 11 | 1 | Cifratura: 1 = AES-256-CTR + HMAC-SHA256 troncato a 16 byte |
| 12 | 4 | Iterazioni PBKDF2 (versione 1.0: 600.000) |
| 16 | 16 | Sale casuale |
| 32 | 8 | Verifica della password: primi 8 byte di HMAC-SHA256(chiave MAC, `"NZip: verifica della password"`) |
| 40 | 16 | Riservati |
| 56 | 8 | XXH3-64 dei byte 0–55 |

**Chiavi.** `PBKDF2-HMAC-SHA256(password in UTF-8, sale, iterazioni)` produce 64 byte:
i primi 32 sono la chiave AES-256, gli altri 32 la chiave HMAC.

**Blocchi cifrati.** Un blocco con il bit 0 dei flag attivo (anche l'indice) ha come contenuto
`IV (16 byte casuali) || testo cifrato || tag (16 byte)`, dove:

- testo cifrato = AES-256-CTR del contenuto normale del blocco (quello descritto in §6), con la
  convenzione di 7-Zip: i primi 8 byte del blocco contatore (inizialmente l'IV) sono un intero
  little-endian a 64 bit che viene **incrementato prima** di cifrare ogni blocco AES di 16 byte;
  il flusso di chiave è `AES(chiave, blocco contatore)`; l'ultimo blocco parziale usa i primi byte;
- tag = primi 16 byte di `HMAC-SHA256(chiave MAC, numero del blocco (u32 LE) || IV || testo cifrato)`;
  l'indice usa come numero 0xFFFFFFFF. Il numero del blocco nel tag impedisce di scambiare i blocchi.

Il lettore verifica il tag (in tempo costante) **prima** di decifrare. Nei blocchi cifrati il campo
"XXH3 dei dati decompressi" vale 0: l'integrità è garantita dal tag e dagli hash BLAKE3 dei file.
Sono cifrati anche i nomi dei file, perché l'indice è un blocco cifrato.

### 9ter. Cifratura per destinatari (record chiave versione 2)

Per cifrare un archivio per delle persone (le loro *identità*, vedi §10ter) — con o senza password — il
contenuto è cifrato con una **chiave del contenuto** casuale di 64 byte (32 AES + 32 HMAC, stesso
schema di §9bis) e il record chiave ha versione 2:

| Offset | Dim. | Campo |
|---|---|---|
| 0 | 8 | Magic `"NZKEY"`, 0x1A, CR, LF |
| 8 | 2 | Versione (= 2) |
| 10 | 1 | 2 = chiave del contenuto negli slot |
| 11 | 1 | Cifratura: 1 = AES-256-CTR + HMAC-SHA256 troncato a 16 byte |
| 12 | 4 | Lunghezza L degli slot che seguono il record |
| 16 | 16 | Riservati (0) |
| 32 | 8 | Verifica: primi 8 byte di HMAC-SHA256(chiave MAC del contenuto, `"NZip: verifica della password"`) |
| 40 | 16 | Riservati |
| 56 | 8 | XXH3-64 dei byte 0–55 |

Gli **slot** (L byte, offset 128) precedono i blocchi, che quindi iniziano all'offset 128 + L:

    "NZSLOTS1" | numero u16 | numero × (tipo u8 | lunghezza u16 | dati) | XXH3-64 di tutto quanto precede

- tipo 1, **password**: iterazioni u32 | sale 16 | nonce 24 | chiave del contenuto cifrata 64 | tag 16 —
  la chiave di cifratura sono i primi 32 byte di `PBKDF2-HMAC-SHA256(password, sale, iterazioni)`,
  l'algoritmo è XChaCha20-Poly1305 (IETF, senza dati associati);
- tipo 2, **destinatario**: chiave pubblica Ed25519 32 | chiave pubblica X25519 32 | lunghezza del nome u16 |
  nome UTF-8 | chiave pubblica effimera X25519 32 | nonce 24 | chiave del contenuto cifrata 64 | tag 16 —
  `condiviso = X25519(effimera segreta, destinatario)`, chiave di cifratura =
  `BLAKE2b-256(condiviso || effimera pubblica || destinatario X25519)`, algoritmo XChaCha20-Poly1305.

Il lettore prova prima le identità dell'utente (slot di tipo 2 con la sua chiave X25519), poi la
password. La **chiave di recupero aziendale** (criteri di NZip Enterprise) è semplicemente uno slot di
tipo 2 in più. Un lettore della versione 1.0 rifiuta questi archivi con "Metodo di cifratura non
supportato".

---

## 10. Chiusura (64 byte)

| Offset | Dim. | Campo |
|---|---|---|
| 0 | 8 | Magic `4E 5A 45 4E 44 1A 0D 0A` (`"NZEND"`, 0x1A, CR, LF) |
| 8 | 8 | Offset dell'indice |
| 16 | 8 | Offset della copia dell'indice |
| 24 | 8 | Fine dei blocchi di dati |
| 32 | 8 | Riservato (0) |
| 40 | 8 | Memoria richiesta per l'estrazione (byte, indicativa) |
| 48 | 8 | Primi 8 byte dell'ID dell'archivio (deve coincidere con l'intestazione) |
| 56 | 8 | XXH3-64 dei byte 0–55 |

---

## 10bis. Contenitori dell'archivio

Il file .nzip può trovarsi dentro altri contenitori; il lettore li riconosce e legge l'archivio
come se fosse un file unico (offset 0 = intestazione).

**Archivio diviso in parti.** `nome.nzip.001`, `nome.nzip.002`, ... sono pezzi consecutivi dello stesso
file .nzip (ogni parte tranne l'ultima ha la stessa dimensione). Il lettore concatena tutte le parti
esistenti a partire da `.001`, qualunque parte venga aperta. Unire le parti con una semplice copia
binaria (`copy /b`, `cat`) ricostruisce il file .nzip.

**Programma autoestraente.** `[programma di estrazione][archivio .nzip]["NZSFXEND" | offset u64 | lunghezza u64]`:
gli ultimi 24 byte indicano dove si trova l'archivio nel file. Il programma di estrazione è `nzip-sfx`.

**Firma digitale.** Dopo l'archivio (e dopo i dati di ripristino) può esserci un blocco di firma
seguito da una coda di 16 byte `"NZSTAIL1" | lunghezza del blocco u64`. Il lettore la toglie prima di
cercare la chiusura (§10), quindi un archivio firmato resta leggibile. Blocco:

| Campo | Dim. |
|---|---|
| Magic `"NZSIGN01"` | 8 |
| Versione u16 (= 1), flag u16, riservati u32 | 8 |
| Chiave pubblica Ed25519 del firmatario | 32 |
| Chiave pubblica X25519 del firmatario | 32 |
| Data della firma (secondi Unix) u64 | 8 |
| Lunghezza firmata u64 (= byte dell'archivio prima del blocco) | 8 |
| BLAKE2b-512 dei byte firmati | 64 |
| Lunghezza del nome u16, nome UTF-8 del firmatario | 2 + n |
| Firma Ed25519 di tutti i byte precedenti del blocco | 64 |

La firma è valida se la firma Ed25519 è corretta, la lunghezza firmata coincide e l'hash BLAKE2b dei
byte firmati è identico. Chi firma è attendibile se la sua chiave è tra le identità o i contatti
dell'utente o tra le chiavi fidate dei criteri aziendali. Una **marca temporale** RFC 3161 (file
`archivio.nzip.tsr`, facoltativo) certifica lo SHA-256 del blocco di firma.

---

## 10ter. Identità

Un'identità è un seme casuale di 32 byte: coppia Ed25519 = `crypto_ed25519_key_pair(seme)` (per le
firme), chiave segreta X25519 = `BLAKE2b-256(chiave = seme, "NZip identita X25519")` (per gli slot di
tipo 2). La parte pubblica si scambia come testo:
`NZID1.` + base64url(Ed25519 pubblica 32 | X25519 pubblica 32 | nome UTF-8). L'**impronta** mostrata
agli utenti sono i primi 8 byte di BLAKE2b(Ed25519 | X25519) in esadecimale (`3F2A-9C01-77B4-E0D2`).

---

## 11. Regole per le versioni future

- Nuovi codec, filtri e trasformazioni ricevono **nuovi** numeri; quelli esistenti non cambiano mai.
- Nuove informazioni nell'indice vanno nei record di estensione (§5).
- Un cambiamento incompatibile (come una nuova trasformazione) richiede di aumentare il "livello minimo
  del lettore" nell'intestazione, **solo negli archivi che lo usano**: i lettori vecchi rifiuteranno
  quegli archivi con un messaggio chiaro, e continueranno a leggere tutti gli altri.
- Ogni versione rilasciata aggiunge i propri archivi a `tests/golden/`; ogni versione successiva
  deve estrarli tutti bit per bit (`python tests/run_all.py`).
