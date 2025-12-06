from locust import HttpUser, task, between

class StressUser(HttpUser):
    wait_time = between(0.5, 1)

    @task
    def everything(self):
        self.client.get("/")
        self.client.get("/index.html")