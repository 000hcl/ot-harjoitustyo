# memory


[vaatimusmäärittely](https://github.com/000hcl/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[tuntikirjanpito](https://github.com/000hcl/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)


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
