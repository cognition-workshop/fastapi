from locust import HttpUser, task, between
import json


class FastAPIUser(HttpUser):
    wait_time = between(1, 3)
    
    @task(3)
    def test_docs_endpoint(self):
        """Test the docs endpoint"""
        self.client.get("/docs")
    
    @task(2)
    def test_openapi_endpoint(self):
        """Test OpenAPI schema endpoint"""
        self.client.get("/openapi.json")
    
    @task(1)
    def test_redoc_endpoint(self):
        """Test ReDoc endpoint"""
        self.client.get("/redoc")
    
    def on_start(self):
        """Called when a user starts"""
        pass
