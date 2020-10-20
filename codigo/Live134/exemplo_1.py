from httpx import get, post, delete

url_base = 'http://localhost:5000/todos/api/tasks'

request = get(url_base)

# assert request.status_code == 200, 'Código da resposta diferente de 200'
# assert request.json() == [], 'Algo de erradonão está certo com esse recurso'

not_task = {'titlle': 'Tomar pinga!'}
bad_task = {'tittle': 'Tomar pinga!'}
good_task = {'titlle': 'Tomar pinga!', 'description': 'Pq é bom', 'done': False}

# request = post(url_base, json=not_task)
# assert request.status_code == 400, 'Código da resposta diferente de 400'

# request = post(url_base, json=bad_task)
# assert request.status_code == 400, 'Código da resposta diferente de 400'

# request = post(url_base, json=good_task)
# assert request.status_code == 201, 'Código da resposta diferente de 201'

# request = delete(url_base + '/2')
# assert request.status_code == 204, 'Código da resposta diferente de 204'
