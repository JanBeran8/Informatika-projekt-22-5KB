# Informatika-projekt-22-5KB

Zpracovávají des. Jan Beran a des. Lubomír Horký:

téma č. 2 - Realizujte API generátor pomocí knihovny FastAPI s autentizací pomocí OAuth. Generujte kód na základě struktury dat v databázi (MS SQL, Postgress).


ÚKOLY:
1) Vygenerovat modely (třídy) založené na "base models" POUZE STRUKTURU NE DATA ! ✔️
2) Předělat vygenerovanou SQL strukturu na strukturu Python kódu (BaseModels) ✔️
3) Každá třída bude mít endpointy
- Create - ✔️
- Update - ❌ - Nejtezsi DOHLEDAT !
- Delete - ✔️ - Najit jak vypada (odpoved nejaky MSG) ✔️
- Read_Multiple - ✔️ (opravit u UZIVATEL - divná chyba, jede jen když se nepřekročí počet vytvořených uživatelů v limitu✔️ když se chybně zadá do databáze s hodnotou null ,tak nastane chyba u cteni prvku z databaze !! (mozna osetrit?))
- Read - ✔️ (opravit u UZIVATEL - divná chyba mělo by jet ???) ✔️

Schemas vygenerovat zvlášť to texťáku - ✔️

-------------------------------------------------------------------------
POŽADAVKY:
--
- Výsledný projekt je uložený na public úložišti Github (ihned od začátku). - ✔️
- WEB Root API či UI je konfigurovatelný (URI). - ❓
- Klíčové funkcionality jsou popsány a demonstrovány pomocí notebooku v Jupyteru. - ❌
- Je definovaný dockerfile / compose.yml pro spuštění výsledného projektu v prostředí docker. - ❌
- Docker images jsou publikovány na hub.docker.com - ❌
- Je nastavena otevřená licence (MIT). - ✔️

------------------------------------------------------------------------    
DODELAT v programu:
Podívat se znovu na CRUD operace a tvoření endpointů podle https://fastapi.tiangolo.com/tutorial/sql-databases/

------------------------------------------------------------------------
