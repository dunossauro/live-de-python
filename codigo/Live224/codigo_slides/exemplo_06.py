"""
Exemplo 06

Tracebacks
"""
from rich.traceback import install
install(show_locals=True)

a = 1
b = 'a'

a + b
# ----

from rich.console import Console
console = Console()

try:
    1 + 'a'
except Exception:
    console.print_exception(show_locals=True)
