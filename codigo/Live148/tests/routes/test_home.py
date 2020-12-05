def test_home_retorna_status_code_200(client):
    response = client.get("/")
    assert response.status_code == 200


def test_home_retorna_texto_ola(client):
    response = client.get("/")
    assert response.text == "ola"


def test_echo_retorna_status_code_200(client):
    response = client.get("/echo")
    assert response.status_code == 200


def test_home_retorna_texto_echo_man(client):
    response = client.get("/echo")
    assert response.text == "echo man!"
