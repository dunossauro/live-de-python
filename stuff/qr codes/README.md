# Como gerar os QR codes

Usamos o CLI do [segno](https://segno.readthedocs.io/en/latest/):

```bash
pipx install segno
```

Para criar:

```bash
segno <URL> --output=<name>.png --scale 30 --light=transparent --dark=#2a2a2a
```
