from locust import HttpLocust, TaskSet, task, between

from _locust.handle_redirect import redirect_handle


class WebsiteTasks(TaskSet):

    def on_start(self):
        _pass = {"pass": "1234"}
        self.client.post('/get-auth', json=_pass)

    @task
    def test_simple_get_request(self):
        self.client.get('/get-complex-object', params={"returnObject": "True"})

    @redirect_handle
    @task
    def test_nao_autorizado_cookie(self):
        with self.client.get('/nao-autorizado-cookie', catch_response=True) as _req:
            return _req


class WebsiteUser(HttpLocust):
    host = 'http://localhost:5000'
    task_set = WebsiteTasks
    wait_time = between(5, 15)
