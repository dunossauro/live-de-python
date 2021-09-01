from unittest import TestCase, mock, main
from acomplamento_exemplo import page_content


class TestPageContent(TestCase):
    def test_page_content_deve_ser_chamada_com_http(self):

        with mock.patch('acomplamento_exemplo.get') as spy:
            page_content('bababa', False)

        spy.assert_called_with('http://bababa', None)


if __name__ == '__main__':
    main()
