# Programma fantastichevole per fare il login su Moodle in automatico By Bigceru
## Prerequisiti
+ eseguire il comando `pip install -r requirements.txt`
+ geckodriver (per il browser Firefox), se il file geckodriver già presente non funziona, seguite la guida a fondo pagina.

## How to use
Per avviare il programma basta andare nella cartella dove sono locati i sorgenti in python ed eseguire il comando:

```bash
python loginMoodle.py
```

Se è la prima volta che si avvia, il programma chiederà di inserire una password (che userà per criptare le nostre credenziali), e successivamente chiederà l'inserimento di username e password per l'accesso a Moodle (Attenzione a scriverle correttamente).

In caso di digitazione sbagliata della password Moodle, basterà eliminare il file credentials.txt e rieseguire il programma che ripartirà come se fosse alla prima esecuzione.

### Geckodriver
Geckodriver è un driver che serve a selenium per comunicare con Firefox (nel nostro caso), quindi come tutti i driver deve prima essere installato.

Per procedere con l'installazione basta andare al seguente link [Geckodriver](https://github.com/mozilla/geckodriver/releases) e scaricare dalle release il driver corretto per il propria SO e la propria architettura.

(Da qui in poi la guidà sarà per linux) 
Una volta scaricato, estraiamo il driver:

```bash
 tar -xf geckodriver-<versione_driver>.tar.gz
 ```
 
Ora spostiamo i driver in una cartella contenuta nel path, per esempio:

```bash
sudo cp geckodriver /usr/bin
```


Ed ecco fatto, ora il nostro programma dovrebbe funzionare correttamente, se così non è prova ad aggiornare Firefox e verificare di aver installato tutti i requirements.txt.
