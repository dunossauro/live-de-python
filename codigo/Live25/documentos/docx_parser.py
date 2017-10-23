"""
http://www.lfd.uci.edu/~gohlke/pythonlibs/.
pip install python_docx-0.8.6-py2.py3-none-any.whl
"""
from docx import Document

document = Document('Lista_samurai_X.docx')
for para in document.paragraphs:
    print(para.text)
