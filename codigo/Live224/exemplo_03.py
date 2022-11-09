from rich import print
from rich.markdown import Markdown


text = '''
# Título

Essa é a live de Python

## Não esqueça!

1. Deixar o **like**
2. *Se inscrever no canal*

### h3

> Iuhuuuu

```py
def xpto():
    return 42
```

'''

print(Markdown(text))
