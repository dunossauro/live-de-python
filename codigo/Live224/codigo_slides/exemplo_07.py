# exemplo_07.py
from rich.console import Console
from rich.markdown import Markdown
console = Console()

texto = '''
# Título do texto

Boas memórias da live de Python

## Passos a seguir

1. **Curta** o vídeo
2. *Se inscreva no canal*'''

console.print(Markdown(texto))
