from unittest import TestCase, mock, main
from acomplamento_exemplo import page_content


class StubGet:
    @property
    def content(self):
        return b'<html> ... </html>'


class TestPageContent(TestCase):
    def test_page_content_deve_ser_chamada_com_http(self):
        esperado = '<html> ... </html>'

        with mock.patch('acomplamento_exemplo.get', return_value=StubGet()):
            result = page_content('bababa', False)

        self.assertEqual(esperado, result)

if __name__ == '__main__':
    main()
