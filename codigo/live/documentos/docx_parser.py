from docx import Document

doc = Document('Lista_samurai_X.docx')
for para in doc.paragraphs:
    print(para.text)
