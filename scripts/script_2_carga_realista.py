from locust import HttpUser, task, between

class LoadUser(HttpUser):
    wait_time = between(1, 2)

    @task(3)
    def homepage(self):
        self.client.get("/")

    @task(1)
    def favicon(self):
        self.client.get("img/Banner%20Tienda%20Online%20Mercado%20Shop%20Mascotas%20Curvo%20Celeste%20y%20Azul.png")
