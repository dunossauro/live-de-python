from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine


def pdf_to_string(pdf_file):
    """
    Converte o pdf para texto.

    Vars:
        - laparams: 0.3 foi o melhor para pegar os negritos e o texto
            não negrito em melhor tempo

    NOTE:
        - LTTextLine: Retira o número das varas
        - LTTextBox: Pega o texto padrão
    """
    fp = open(pdf_file, 'rb')

    parser = PDFParser(fp)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize('')
    rsrcmgr = PDFResourceManager()

    # Configuração das margens
    laparams = LAParams()
    laparams.line_margin = 0.3
    laparams.word_margin = 0.3
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)

    interpreter = PDFPageInterpreter(rsrcmgr, device)

    for page in doc.get_pages():
        interpreter.process_page(page)
        layout = device.get_result()
        for lt_obj in layout:
            # montar uma função para essa validação
            if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                line_text = lt_obj.get_text()
                print(line_text)


pdf_to_string('Lista_samurai_X.pdf')
