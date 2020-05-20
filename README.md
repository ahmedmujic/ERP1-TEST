# ERP1 
KORISNIČKI ZAHTJEVI –ERP 1-
Napraviti aplikaciju koja će biti primjenljiva za sve kompanije koje se bave prodajom, kako roba široke potrošnje tako i ostalih roba. Ova aplikacija treba omogućiti intuitivan pristup i korištenje od strane svih struktura unutar određene firme. Svaki modul aplikacije uveliko treba olakšati svakodnevno poslovanje preduzeća do 1500 radnika. Svaki modul aplikacije mora da bude sa jasnim GUI-em, intuitivan i pri tome da ima mogućnost brze komunikacije s drugim modulima. Potrebno je dizajnirati i implementirati sljedeće module: 
•	eMenadžment
•	Prodaja
•	Nabavka
•	Knjigovodstvo
•	Izvještaji
•	Dashboard
•	Glavna knjiga
Projektom je neophodno i predvidjeti moguću nadogradnju softvera na ostale grane trenutne firme i predvidjeti isto prilikom dizajniranja i implementiranja. Potrebno je i predvidjeti sve interface prema ostalim temama u cilju povećanja modularnosti samog programa. 
Korisnici sistema će biti:
•	Registrovani korisnici 
•	Neregistrovani korisnici
Registorvani korisnici će imati ovlasi određene direktno njihovom „rolom“ u sistemu, s tim u vezi potrebno je predvidjeti sljedeće role sa njihovim ovlastima:
•	Administrator (direktori)
•	Glavni blagajnik
•	Knjigovođa
•	Glavni komercijalista
Prijavu na sistem će imati knjigovođe i direktori, dok će i neregistrovani korisnici imati mogućnost interakcije sa sistemom. Korisnik prilikom prijave dobija mogućnost upravljanja onim za šta je ovlašten i shodno tome upravlja sistemom. Dakle ne prikazuju se iste informacije direktoru, knjigovođi i blagajniku. U sistemu pregled svih modula će imati direktori i knjigovođe, dok ostali korisnici će pregledati one module za koje su ovlašteni. 
Registracija
Svaki korisnik za identifikacionim brojem će imati mogućnost prijave na sistem, dakle prijavu kao korisnici će imati samo zaposlenici kompanije (knjigovođe i direktori), dok ostali će da budu ili prijavljeni kao guest user-i, iz ovog se izuzimaju lica koja vrše kontrole (svako lice koje vrši  kontrolu će biti u stanju da se prijavi u cilju sprovođenja mjera kontrole – npr. poreska inspekcija će imati svoj nalog preko kojeg može da prati promet bez potrebe dolaska na adresu firme). 
Prilikom registracije je potrebno unijeti osnovne, dok su neki podaci opcionalni. Osnovni podaci su: 
•	Ime
•	Prezime
•	Identifikacioni broj radnika
•	Broj ugovora
•	Lozinke
Opcionalni podaci: 
Postavljanje email adrese (u slučaju da dođe do zaboravljanja lozinke radi bržeg procesa se koristi email u suprotnom se šalje zahtjev administratoru za promjenom lozinke koju on vrši)

Dashboard
Početna stranica daje uvid korisniku u sve važne faktore za poslovanje kopanije a to su: 
•	Stanje budžeta
•	Tok novca po mjesecima
•	Dugovanja i dužnici
•	Pregled troškova
Budžet
Budžet je osnovni planski dokument kompanije koji predstavlja prihode i rashode u posmatranom budućem periodu koji se mogu očekivati. Drugim riječina, vrši se planiranje mogućih troškova i zarade na određenom vremenskom periodu (godišnjem) po određenim kontima. Usvajanjem budžeta sistem će pratiti izvršavanje budžeta na osnovu ulaznih i izlaznih računa tokom cijele godine, odnosno shodno prometu izlaznih i ulaznih računa vršit će se varijacije iznosa budžeta. Suština ove komponente je praćenje troškova. Dobro ostvaren budžet je neophodan za raspodjelu ostvarene dobiti. Infromacije o budžetu je potrebno prikazati na početno stranici nakon registracije rola direktora i knjigovođe.  
Nabavka
Svako preduzeće posjeduje plan nabavki koje želi da vrši, prilikom čega aplikacija mora da ima mogućnost unosa cjelokupnog plana nabavke sa sljedećim stavkama: 
•	Artikli
•	Cijena
•	Opis 
•	Ugovor (da li će se sklapati ili ne prilikom nabavke)
•	Datum isporuke
Artikli mogu da podrazumijevaju materijalna dobra, međutim mogu i podrazumijevati vršenje neke usluge (npr. popravak računarske opreme, korištenje softvera itd.). Nabavke se mogu vršiti na dva načina: internom nabavkom unutar firme i javnom nabavkom, samim tim potrebno je i evidentirati o kojoj vrsti nabavke je riječ. Ukoliko je riječ o javnoj nabavci firma raspisuje tender o javnoj nabavci gdje je potrebno dati pregled tendera koji će biti dostupan svim neregistrovanim korisnicima. Potrebno je omogućiti upload .pdf-a na početnu stranicu sa tenderskom dokumentacijom koju će moći pregledati svi partneri kao i potencijalni partneri. Prilikom odabira određene tenderske dokumentacije, ponuđaču će se ponuditi forma za unos ponude koju treba popuniti sljedećim podacima: 
•	Naziv firme
•	Sjedište 
•	OIB 
•	Ponuda u obliku .pdf fajla
Pregled svih ponuda će biti dostupan registrovanim korisnicima, nakon čega će biti u mogućnosti da sve ponude preuzme i proslijedi komisiji za validaciju ponuda.
Ukoliko je riječ o internoj nabaci, komercijala istražuje tržište i bira najpovoljnijeg partnernera pri čemu se odabir partnera viši unutar komercijalne službe terenskim istraživanjem. Nakon odabira najpoboljnijeg ponuđača, ukoliko je nabavka vezana ugovorom, aplikacija daje mogućnost pregleda za određenu nabavku ugovora o toj nabavci, ukoliko nabavka nije vezana ugovorom ista se korisniku prikazuje sa informacijom da nabavka nije vezana ugovorom. 
Modul nabavka mora da sadrži pregled svih nabavljača, odnosno potencijalnih nabavljača. Aplikacija mora dati mogućnost pregleda svih dobavljača pri čemu informacije o svakom dobavljaču moraju da sadrže sljedeće stavke:
•	Naziv dobavljača
•	Ime i prezime predstavnika firme
•	E-mail predstavnika dobavljača
•	Država
•	Adresa
•	Grad
Pored svih informacija o dobavljaču potrebno je da se vrši kontrola dugovanja svakog dobavljača. Npr. potrebno je kontrolisati ukoliko dobavljač posjeduje neka dugovanja prema firmi, da se plaćanje prebija preko dugovanja u skladu sa dogovorom predstavnika firmi. Dakle umjesto klasičnog plaćanja i skidanja novca sa računa kompanije, potrebno je izvršiti update dugovanja u iznosu računa. Potrebno je i predvidjeti načine plaćanja, da li će biti u materijalnim dobrima (artikli i usluge) ili pak novac. 
Nakon odobravanja nabavke aplikacija mora imati mogućnost unosa računa koji je dobijen od strane nabavljača (partnera). Nakon unosa dobijene od strane ponuđača, faktura se sprema u modul ulaznih računa i daje joj se atribut ulazna faktura.
Svaki ulazni račun se sastoji od:
•	broj računa i datum izdavanja
•	ime i prezime (naziv), adresa, OIB ili PDV identifikacijski broj poreznog obveznika koji je isporučio robu ili obavio uslugu
•	ime i prezime (naziv), adresa, OIB ili PDV identifikacijski broj poreznog obveznika kome je isporučena roba ili obavljena usluga
•	količina i uobičajeni trgovački naziv isporučenih dobara te vrsta, količina ili opseg obavljenih usluga,
•	datum isporuke dobara ili obavljenih usluga,
•	jedinična cijena bez PDV-a, odnosno iznos naknade za isporučena dobra i obavljene usluge, razvrstane po stopi PDV-a,
•	popusti,
•	stopa PDV-a,
•	iznos PDV-a razvrstan po stopi PDV-a, 
•	zbrojni iznos naknade i PDV-a,
dodatne napomene (napomena o prijenosu porezne obveze ili napomena o osnovi oslobođenja).  Ukoliko ne posjeduje neke od navedenih elemenata sistem neće dozvoliti unos računa, što označava da isti nije valjan i daj potrebno o tome obavijestiti pošiljaoca računa. Prvobitno se određuje koji je tip računa, tj da li je to isporuka dobara i usluga ili avans. Potom se evidentira patner kao i iznos fakture sa porezom. Na osnovu ove dvije stavke, sistem prepoznaje kako treba da popuni sve ostale iznose. Nakon toga dolazi do kontiranje stavke. Ukoliko se promijeni neko od pravila knjiženja/kontiranja, dolazi do ponovnog kontiranja. Na kraju se sprema knjiženje te račun dobiva status „poknjiženo“.
Prodaja
Modul prodaja treba biti usko vezan uz modul nabavke, svaka prodaja kao i nabavka mora da ima pregled ponude odnosno sastavljanje ponude. Sistem mora imati mogućnost da po otvaranju blagajne, blagajnik evidentira njeno početno stanje, odnosno on je u sistem dužan unijeti depozit (novac sa kojim se započinje poslovanje). Nakon pripremnih radnji, blaganik vrši opsluživanje klijenata/kupaca pri čemu svakom izdaje fiskalni račun. Po završetku radnog vremena, blagajnik obavlja obradu finansijskih dokumenata, tj. zaključivanje dnevnika blagajne. To se odnosi na podnošenje izvještaja u posebnoj formi koja sadrži datum, redni broj izvještaja, saldo dnevnog prometa, te iznos PDV-a kojeg je pravno ili fizčko lice dužno platiti. Ovo će se vršiti njegovom prijavom na sistem gdje će on u obliku forme unositi depozit blagajne odnosno unijeti informacije na kraju radnog dana a sistem će sam da generiše izvještaj koji će biti dostupan u modulu izvještaji.
Sitem mora i da ima mogućnost da korisnik (komercijalista) izvrši kreiranje ponude za partnere, prilikom čega bilježi sljedeće stavke: 
•	artikle ponude
•	jedinica
•	cijena po jedinici artikla
•	datum ponude
•	datum isteka ponude
•	taksa
Nakon što korisnik odabere partnera sistem automatski šalje ponudu partneru putem email servisa.
Ukoliko partner prihvati ponudu i izda mu se račun korisniku se daje mogućnost unosa u sistem ovog izlaznog računa. Račun odnosno faktura se automatski generiše po template-u koji frima posjeduje. Nakon generisanja računa, sistem vrši cloud printanje, kojeg preuzima glavni blagajnik i uručuje klijentu. Izlazni račun mora da sadrži sljedeće stavke:
•	redni broj,
•	broj fakture/računa,
•	datum fakture,
•	naziv kupca-PDV obveznika (ili naznaka o gotovinskoj isplati),
•	identifikacioni broj kupca za indirektne poreze (smao za kupce-PDV obveznike),
•	iznos fakture,
•	iznos interne poreske fakture u vanposlovne svrhe,
•	iznos fakture za izvozne isporuke,
•	iznos fakture za ostale isporuke oslobođene PDV-a,
•	osnovica za obračun PDV-a kupcima
Ukoliko ne posjeduje neke od navedenih elemenata sistem neće dozvoliti unos računa, što označava da isti nije valjan i daj potrebno izvršiti reviziju istog. Ukoliko je riječ o validnom računu on ulazi u glavnu knjigu. Ti poslovni događaji odnose se ne samo na promjene na prihodima i rashodima nego i na imovini, na obvezama i potraživanjima, i na kapitalu. Tačnije, pored rednog broja, broja računa, datuma knjiženja, broja i datuma knjigovdstvene isprave, prometa (da li je ta stavka prihod ili su to troškovi firme), postoji i stavka konto. Konto predstavlja opis knjiženja. Konto je šifra prema kojoj svaki računovođa zna na osnovu čega je određena stavka proknjižena (npr.nekretnine, sirovina, roba,…). Standardna stopa PDV-a na oporezivi promet dobara i usluga i uvoz dobara u Bosnu i Hercegovinu iznosi 17%. Samim tim se lahko može izračunati stavke u računima: iznos fakture bez PDV-a i iznos stope PDV-a, gdje tako firma ima uvid u plaćanje poreza državi, što sistem treba da radi automatski.
I ovaj modul daje pregled svih partnera (mušterija) u slučaju da naša firma duguje partneru preko izlaznog računa se može vršiti „prebijanje“ duga. Potrebno je korisniku i omogućiti pregled svih servisa (usluga) i artikala koji mogu biti predmet prodaje i svaki mora da ima sljedeće atribute:
•	šifra
•	naziv
•	opis 
•	cijena
•	konto
•	dobavljač (za artikle) 
•	tip (za usluge)

Izvještaji
Jedan od modula aplikacije je i finanskijski izvještaj koji se radni na više vremenskih nivoa u zavisnosti od dogovora. Finanskijski račun u sistemu bi trebao da bude dio glavne knjige.  On objedinjuje i prezentuje poslovni uspjeh firme. Odnosno na osnovu informacija koje se nalaze u glavnoj knjizi sistem bi trebao da u svakom trenutku da prikaz informacija o tome kako firma posluje. Formalno završni finansijski račun se prezentuje jedanput godišnje za poslovanje u prethodnoj godini, ali i pored toga potrebno je obezbjediti da se finansijski izvještaj može izdati i pogledati bilo kada kako bi se utvrdilo poslovanje firme.
Finansijski izvještaji moraju da pruže informaciju o :
1.	Imovini 
2.	Obavezama
3.	Kapitalu
4.	 Prihodima i rashodima, uključujući dobitke i gubitke
5.	Doprinosima od raspodjele vlasnicima koji djeluju u svojstvu vlasnika
6.	Tokovima gotovine entiteta
Ono bez čega nema finansijskog izvještaja su bilans uspjeha i bilans stanja. Bilans stanja predstavlja grupisani, sumarni pregled sredstava i njihovih izvora u vrijednosnim tj. novčanim pokazateljima. Bilans je prikaz imovine preduzeća u jednom određenom trenutku, dakle fiksirani trenutak neprekidnog radnog procesa koji se odvija u preduzeću, odnosno pokazuje stanje imovine i vlasništva nad imovinom određenog dana. Bilans stanja kao tabelarni prikaz ima dvije strane: lijevu koja se obilježava sa aktiva i desnu čiji je naziv pasiva.. U aktivu se unose sva sredstva, a u pasivu izvori sredstava odnosno obaveze stvorene po bilo kom osnovu. Aktiva je uvijek jednaka pasivi, odnosno, sredstva uvijek moraju biti jednaka svojim izvorima.
Druga vitalna komponenta finansijskog izvještaja koju mora sistem da sadrži je bilans uspjeha.
Osnovni cilj sastavljanja bilansa uspjeha sastoji se u izračunavanju ostvarenog periodičnog rezultata. U tu svrhu u bilansu uspjeha prikazuju se prihodi i rashodi jednog preduzeća nastali u određenom vremenskom periodu. Dakle, sadržinu bilansa uspjeha čine prihodi i rashodi. Za prihode možemo reći da su pozitivan tok vrednosti, a za rashode negativan tok vrednosti u preduzeću.  
Prihodi kao sastavni dio bilansa uspjeha razvrstani su u četiri grupe i to:
•	Poslovni prihodi nastaju od prodaje trgovinske robe, proizvoda i usluga, prihodi od subvencija, dotacija, regresa, kompenzacija i sl.  
•	Finansijski prihodi čine uglavnom prihodi od kamata i dividendi.  
•	Neposlovni i vanredni prihodi nastaju po osnovi prodaje hartija od vrednosti, osnovnih sredstava, materijala, viškovi, smanjenja obaveza prema komitentima i državnim organima.  
•	Revalorizacioni prihodi nastaju po osnovu revalorizacije sljedećih delova aktive: osnovna sredstva
Rashodi mogu biti: 
•	Poslovni rashodi: nabavna vrednost prodate robe, troškovi materijala, troškovi zarada, troškovi proizvodnih usluga, troškovi amortizacije, nematerijalni troškovi. 
•	Finansijski rashodi: rashodi po osnovu kamata, negativne kursne razlike itd.  
•	Neposlovni i vanredni rashodi: rashodi koji nastaju kao posledica nepredviđenih poslovnih događaja na koje preduzeće ne može da utiče (manjkovi sredstava, kazne i sl.),  
•	Revalorizacioni rashodi: rashodi koji nastaju po osnovu revalorizacije kapitala. 
Glavna knjiga
Najvažniji modul aplikacije je glavna knjiga koja bi trebala da pruži uvid korisniku u sljedeće: 
•	Pregled računa (izlaznih/ulaznih)
•	Pregled svih ugovora
•	Pregled konta
Dakle sistem prilikom evidencije prihoda ili rashoda, odnosno prilikom izdavanja izlaznih ili ulaznih računa sve račune smješta u modul glavne knjige. Korisnik mora imati mogućnost pregleda svih računa po kategoriji ili potkategoriji (npr. izlazni računi sortirani po cijeni uzlazno itd.) 
Potrebno je i omogućiti pregled svih ugovora sklopljenih u okviru firme pri čemu se pretraga može vršiti na više osnova: 
•	Po tipu ugovora
•	Aktivni/neaktivni
•	Po datumu isteka (uzlazno/silazno) 
•	Po partnerima
Pregled konta podrazumijeva: 
•	Naziv konta
•	Šifra pod kojom se određeni konto vodi u glavnoj knjizi
Računovodstvo
Aplikacija daje korisniku mogućnost pregleda svih izvršenih transakcija po računu.  Transakcija se vrši na način da se upišu sve potrebne stavke, a to su: broj transakcijskog računa primaoca, iznos transakcije, svrha doznake, te šifra plaćanja koja odgovara tekstualnom dijelu svrhe doznake. Transakcija je okončana kada korisnik od banke, preko sistema, dobije potvrdu o uspješnosti transakcije i jedinstveni identifikator naloga  koji se kasnije može koristiti za reklamaciju. Korisnik, također, prima obavijesti o svakoj izmjeni stanja transakcijskog računa, tj. ukoliko neko uplati novac na račun korisnik ima mogućnost pregleda uplate. Sve transakcije se pohranjuju i korisnik ima mogućnost pregleda  izvršenih transakcija, a na kraju radnog dana se pravi izvještaj svih transakcija koje se zatim prosljeđuju računovođi na knjiženje. Transakciju mogu izvršiti samo korisnici koji imaju dozvoljene permisije za to u protivnom je dostupan samo pregled svih, kako transakcija tako i transakcijskih računa koje firma posjeduje. Bitno je napomenuti da određena firma može posjedovati veći broj transakcijskih računa pa je potrebno to i evidentirati.
Transakcija sadrži sljedeće elemente:
•	Broj 
•	Iznos
•	Primalac (partner)
•	Datum
•	Tip

