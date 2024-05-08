from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def check(self):
        self.client.get("/check")    
    @task
    def check(self):
        self.client.post("/create", json={'nome': 'Carlos'})
