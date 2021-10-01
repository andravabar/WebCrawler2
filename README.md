# WebCrawler

#### 2021∕22 projekt nr 1 "Web Crawler" toimus ajavahemikul 30.09 - 01.10.2021.

Meie tiim **"WebCrawler2"** koosnes 3 erineva kursuse õpilastest: TAK-19, TA-20 ja TA-21

**Tiimiliikmed TAK-19:** 
Erki Leemet / Karl Jäme

**Tiimiliikmed TA-20:**
Rainis-Ross Tiirik / Andra Vabar 

**Tiimiliikmed TA-21:**
Riivo Matt / Liisi Kuusküll / Olev Kuris

## Kust me pärit oleme?
Kõik tiimi liikmed on pärit Eestist ning õpivad Kuressaare Ametikoolis tarkvara arenduse erialal.

## Projekti idee ja eesmärk
* Projekti eesmärk on ehitada web-crawler, mis jälgib aktsia hinna muutusi protsentides. Kui hind tõuseb või langeb kasutaja poolt sätestatud %-lävendi, siis programm saadab teavituse e-maili peale.

## Töökäik
Esimese projektipäeva esimesel tunnil tutvusime üksteisega, kuna päris mitmele oli see elu esimene projekt Ametikoolis ning inimesed veel tundmatud. Kui ülevaade inimeste oskustest ja teadmistest olemas, arutasime millisest teemast võiks töö teha. 

Enamuse heakskiidul otsustasime teha webcrawleri, mis jälgiks Balti börsil noteeritud väärtpaberite hindasid. Esmane idee oli võtta valikusse ainult teatud aktsiad, mille hinda jälgida ning kui soovitud aktsia hind satub kasutajale sobivale tasemele (kas aktsia müümiseks või ostmiseks), siis programm saadaks välja vastavasisulise e-maili. Üsna peagi saime aru, et otstarbekam oleks jälgida mitte üksikute aktsiate hinna kõikumisi, vaid hoopis terve börsi lõikes hinna muutust protsentides, et saada teavitusi kogu Balti börsi anomaaliatest.
Ideaalmaailmas oleks tahtnud ehitada ka kasutajaliidese, kus aktiveerida/deaktiveerida programm, lisaks kus kasutaja saaks muuta %-väärtusi.

Esimese prototüübi joonistasime üles interaktiivsel tahvlil, kuhu püüdsime teha täisversiooni kasutajaliidesest.
![alt text](https://github.com/andravabar/WebCrawler2/blob/main/IMG_4675.jpg)
![alt text](https://github.com/andravabar/WebCrawler2/blob/main/IMG_4676.jpg)

Kui protüüp "paberil" oli valmis, tegime oma tiimile erinevad suhtluskanalid (Slackis, Teamsis), kus jagada linke, pilte ja ekraani. Githubis sai tehtud projekt, kuhu hakkasime genereerima teemaga seotud issues'd. 

Pärast seda jagasime tiimisiseselt ülesanded laiali, kes mille kallal tööle saaks asuda. Paralleelselt hakkasime tööle koodi kirjutamisega ning Figmas kasutajaliidese disainimisega. Mõlema tööga jätkasime päeva lõpuni ning täiendasime teise projektipäeva lõunani.

Programm on kirjutatud Pythonis, mille lõpp-funktsionaalsus päeva lõpuks oli see, et programm saatis välja e-maili nendest aktsiatest, mis programmi käivitamise hetkel olid hinnas kukkunud -5% või tõusnud +5%:
![alt text](https://github.com/andravabar/WebCrawler2/blob/main/img_20211001_113348.jpg)

Oleksime muidugi tahtnud juurde saada ka funktsionaalsust, kus programm jookseks pidevalt teatud intervalli tagant (15min), kuid seda ei jõudnud arendada. 

Teisel projektipäeval alustasime ka html/css'ga, kus kasutasime Tailwind tööriistu, kuid paraku ei jõudnud selle protsessig nii kaugele, et midagi avalikkusele näidata.


## Suhtluskanalid: 
- Teams
- Slack

## Töövahendid ja lingid: 
- Github
- VS Code
- Tailwind
- Figma [Prototüüp](https://www.figma.com/file/mnKabqqzYbmXBixxMAv6sO/Untitled?node-id=0%3A1)

## Küsimused projekti kohta
 - Üks pehme oskus, mida õppisin ja endas arendasin
 - Üks tehniline oskus, mida õppisin ja endas arendasin
 - Kas oleksid tahtnud täita mingit muud ülesannet selles meeskonnas

**Rainis-Ross Tiirik:**

**Andra Vabar:**
 - panna meeskond tööle nii, et kõik meeskonnaliikmed tunneksid, et nad on vajalikud ja kasulikud. Lisaks olin õpetajarollis, et anda esmakursuslastele võimalikult arusaadavalt ja lihtsalt sissejuhatus erinevatest kanalitest/toolidest, mida me siin koolis kasutame. Püüdsin ennast tagasi hoida, et mitte oma ideid ja nägemusi peale suruda, vaid kuulata ja usaldada oma tiimiliikmeid ja minna kaasa nende flow'ga.
 - paarikoodimine, sh clone/push/pull/stash meeldetuletus
 - suuers pildis ma ei leia, et oleksin midagi muud saanud tiimi heaks teha, aga oleksin tahtnud rohkem tegeleda koodimisega, kui administratiivsete argimuredega.

**Erki Leemet:**
 - suhtlemine, tiimitöö
 - web scrapemine
 - Ma olin rahul enda ülesandega.

**Karl Jäme:**

**Riivo Matt:**
 - kriitiline mõtlemine, meeskonnatöö
 - figma
 - ei 

**Liisi Kuusküll:**
 - Tutvusin figmaga. 
 - Tehnilisi oskusi veel ei ole. Tiimi kaaslased jagasid enda ekraani, et näidata ka teistele, mida nad teevad.
 - Jäin enda ülesandega rahule.

**Olev Kuris:** 
 - Õppisin tiimitööd.
 - Tegin esmast tutvust figma ja githubiga. 
 - Ei oleks tahtnud mingit muud ülesannet.


