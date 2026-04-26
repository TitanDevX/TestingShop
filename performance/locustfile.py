from locust import HttpUser, task

class ShopUser(HttpUser):

    @task
    def get_products(self):
        self.client.get("/products")

    @task
    def create_order(self):
        self.client.post("/order", json={
            "product_id": 1,
            "quantity": 1
        })