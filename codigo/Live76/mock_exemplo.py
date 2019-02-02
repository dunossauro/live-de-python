from unittest import TestCase, main
from unittest.mock import patch
from acomplamento_exemplo import page_content


class FakeGet:
    @property
    def content(self):
        return b'<html> ... </html>'


class TestPageContent(TestCase):
    def test_page_content_deve_ser_chamada_com_http(self):
        esperado = '<html> ... </html>'

        with patch(
            'acomplamento_exemplo.get', return_value=FakeGet()
        ) as mocked:
            result = page_content('bababa', False)

        self.assertEqual(esperado, result)
        mocked.assert_called_with('http://bababa', None)


if __name__ == '__main__':
    main()
