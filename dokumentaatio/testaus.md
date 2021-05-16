# Testausdokumentti

Sovelluksen automatisoituun testaamiseen on käytetty unittest. Kaikki paitsi käyttöliittymän luokat ovat testattu tällä tavalla. Sovellusta on myös testattu manuaalisesti. 

## Automatisoidut testit

### Tulostaulun testaus

Tulostaulun testit luovat tiedostoja jotka vastaavat kelvollisia ja epäkelvollisia totuustauluja, ja testaa näillä Save-luokkaa. Näin oikeaa ohjelman käyttämä totuustaulu ei muutu.

### Pelin logiikka

Pelin logiikka tapahtuu Level-luokassa. Sille ei ole tehty testejä missä peli pelataan loppuun, koska en ole vielä keksinyt järkevää tapaa toteuttaa sellaista testiä.


### Testauskattavuus

Haarautumiskattavuus on 91%.

![covreport](./kuvat/covreport.png)

## Järjestelmätestaus

Sovellusta on testattu Linux- ja Windows-ympäristössä. Kaikki [määrittelydokumentissa](https://github.com/000hcl/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md) listatut toiminnallisuudet on testattu ja toimivat molemmissa ympäristöissä.
