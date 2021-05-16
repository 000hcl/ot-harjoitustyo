# memory


[vaatimusmäärittely](https://github.com/000hcl/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[tuntikirjanpito](https://github.com/000hcl/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[arkkitehtuuri](https://github.com/000hcl/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[käyttöohje](https://github.com/000hcl/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[testidokumentti](https://github.com/000hcl/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)

## Asentaminen:

Tarvitset:

- pythonin versio 3.6 (tai uudempi)
- poetry

1. [Lataa viimeisin release](https://github.com/000hcl/ot-harjoitustyo/releases/tag/loppupalautus)
2. Pura zip haluamaasi paikkaan.
3. siirry komentorivillä purattuun kansioon.
4. Käynnistä ohjelma seuraamalla seuraavat ohjeet:


## Kuinka testata/käynnistää ohjelma:

1. Riippuvuudet, suorita:
```bash
poetry install 
```
2. Käynnistys, suorita:
``` bash
poetry run invoke start
```
---

Testaus:
```bash
poetry run invoke test
```

Coverage report:
```bash
poetry run invoke coverage-report
```
---

Lint:
```bash
poetry run invoke lint
```
