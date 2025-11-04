import os
from unittest.mock import patch

print(os.getcwd())

with patch('os.getcwd', return_value='/fake'):
    print(os.getcwd())

print(os.getcwd())


def xpto():
    return 42

with patch('__main__.xpto', return_value=10):
    print(xpto())
