from httpx import get

url_base = 'http://localhost:5000/todos/api/tasks'


class TestTask():
    def test_tasks_deve_retornar_200_quando_receber_um_get(self):
        request = get(url_base)
        assert request.status_code == 200


    def test_tasks_deve_retornar_uma_lista_vazia_no_primeiro_request(self):
        """
        Garantir que quando fizer o primeiro request
            Não deve exite nenhum recurso em /tasks
        """
        request = get(url_base)
        assert request.json() == []

    def test_tasks_deve_retornar_400_quando_receber_um_todo_inválido(self):
        not_task = {'titlle': 'Tomar pinga!'}
        request = get(url_base)
        assert request.status_code == 400
