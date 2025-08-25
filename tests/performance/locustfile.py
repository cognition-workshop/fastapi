from locust import HttpUser, between, task


class FastAPIUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def test_root_endpoint(self):
        response = self.client.get("/")
        if response.status_code != 404:
            print(f"Unexpected status code for /: {response.status_code}")

    @task(2)
    def test_docs_endpoint(self):
        response = self.client.get("/docs")
        if response.status_code != 404:
            print(f"Unexpected status code for /docs: {response.status_code}")

    @task(1)
    def test_openapi_endpoint(self):
        response = self.client.get("/openapi.json")
        if response.status_code != 404:
            print(f"Unexpected status code for /openapi.json: {response.status_code}")

    def on_start(self):
        pass
