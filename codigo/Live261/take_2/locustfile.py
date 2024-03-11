"""
Como rodar:

1. Ative o ambiente virtual
2. `locust --headless --users 15 --spawn-rate 3 -H http://localhost`
"""
from locust import HttpUser, between, task


class LoadTest(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_root(self):
        self.client.get('/user')

    @task
    def post_tiao(self):
        self.client.post(
            '/user',
            json={
                'username': 'Tião do gás',
                'email': 'dasdas@email.com',
                'senha': 'xeggaaaa',
            },
        )

    @task
    def get_spam(self):
        self.client.get('/user/1')
