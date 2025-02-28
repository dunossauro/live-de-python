from mimesis import Person
from mimesis.locales import Locale

provider = Person(locale=Locale.PT_BR)


def test_create_user(client):
    # arrange
    dummy_data = {
        'username': provider.username(),
        'email': provider.email(),
        'password': provider.password()
    }

    # act
    client.post('/users', json=dummy_data)
