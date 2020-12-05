
def test_users_retorna_status_code_200(client):
    response = client.get("/users/")
    assert response.status_code == 200



def test_users_retorna_lista_de_usuarios(client):
    response = client.get("/users/")
    result = response.json()
    assert result == [
        {
            "email": "du@email.com",
            "id": 1,
            "name": "Dunossauro",
            "password": "1234",
        }
    ]



def test_create_users_retorna_msg(client):   
    data = {
            "email": "du2@email.com",
            "name": "Dunossauro 2",
            "password": "12345",
    }
    response = client.post("/users/",json=data)
    assert response.json() == {"msg": "usuario inserido com sucesso!"}
