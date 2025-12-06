from locust import HttpUser, task, between

class LoadUser(HttpUser):
    wait_time = between(1, 2)

    @task(3)
    def homepage(self):
        self.client.get("/")

    @task(1)
    def assets(self):
        self.client.get("/assets/favicon.png")