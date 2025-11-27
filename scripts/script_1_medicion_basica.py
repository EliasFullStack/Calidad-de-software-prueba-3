
from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1, 3)  # Wait 1-3 seconds between requests

    @task(1)  # Weight: execute 3x more than other tasks
    def view_homepage(self):
        self.client.get("/")
        
    @task(1)
    def view_registerpage(self):
        self.client.get("/registro")
        
    @task(1)
    def view_accesopage(self):
        self.client.get("/acceso")
        
    @task(1)
    def view_invetariopage(self):
        self.client.get("/inventario")
    
    @task(1)
    def view_pagopage(self):
        self.client.get("/pago")
    
    @task(1)
    def view_contatopage(self):
        self.client.get("/Contacto")
        
    @task(1)
    def view_blogpage(self):
        self.client.get("/blog")
        
    @task(1)
    def view_nosotrospage(self):
        self.client.get("/Nosotros")
    