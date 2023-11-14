# 2. Labos iz predmeta "Otvoreno računalstvo"
U ovom labosu sam napravio web-stranicu u pomoću HTML-a za frontend i Flaska(Python) za backend. Prva stranica sadrži osnovne podatke o skupu podataka, kao README od prošlog labosa, i ima link na JSON i CSV. Druga stranica ima tablični prikaz podataka pomoću datatable, te omogućeno filtriranje tablice općenito (built-in u datatable) ili po atributu/stupcu. Također se može skinuti CSV i JSON filtrirane tablice. 
## Opis podataka:
- Izdavač: Tvrtko Tomić
- Datum izdanja: 14.11.2023.
- Licensa: CC BY 4.0
- Verzija: 2.0
- Jezik: hrvatski
- Zemlje pokrivene: Hrvatska, Njemačka
- Baza: postgresql
- Frontend: HTML + CSS
- Backend: Flask (Python)
- ključne riječi: dućan, tehnika, web-stranica, JSON, CSV
- opis atributa:
    - naziv -> naziv dućana (string)
    - adresa -> adresa dućana (string)
    - grad -> grad u kojem se nalaz dućan (string)
    - telefonski_broj -> broj dostupan kupcima za kontakt (int)
    - email -> e-mail dostupan kupcima za kontakt (string)
    - geolokacija -> geografske koordinate dućana (stribg)
    - recenzija -> ocjena dućana na Google Maps (double) -> JSON double sprema kao number
    - država -> država u kojoj se dućan nalazi (string)
    - poštanski_broj -> poštanski broj dužana (int)
    - vlasnici -> navedeni trenutni vlasnik/ci dućana (string)
