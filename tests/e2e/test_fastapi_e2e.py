import os
import time
from multiprocessing import Process

import pytest
import requests


class FastAPIServer:
    def __init__(self, host="127.0.0.1", port=8001):
        self.host = host
        self.port = port
        self.process = None
        self.base_url = f"http://{host}:{port}"

    def start(self):
        def run_server():
            os.system(
                f"uvicorn tests.e2e.test_app:app --host {self.host} --port {self.port}"
            )

        self.process = Process(target=run_server)
        self.process.start()

        for _ in range(30):
            try:
                response = requests.get(f"{self.base_url}/health", timeout=1)
                if response.status_code == 200:
                    return True
            except Exception:
                time.sleep(1)
        return False

    def stop(self):
        if self.process:
            self.process.terminate()
            self.process.join(timeout=5)
            if self.process.is_alive():
                self.process.kill()


@pytest.fixture(scope="module")
def fastapi_server():
    server = FastAPIServer()
    if server.start():
        yield server
    else:
        pytest.skip("Could not start FastAPI server for E2E tests")
    server.stop()


class TestFastAPIE2E:
    def test_server_startup_and_health(self, fastapi_server):
        response = requests.get(f"{fastapi_server.base_url}/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"

    def test_complete_user_journey(self, fastapi_server):
        base_url = fastapi_server.base_url

        health_response = requests.get(f"{base_url}/health")
        assert health_response.status_code == 200

        item_data = {
            "name": "E2E Test Item",
            "price": 99.99,
            "description": "End-to-end test item",
        }

        create_response = requests.post(f"{base_url}/items/", json=item_data)
        assert create_response.status_code == 200
        created_item = create_response.json()
        item_id = created_item["item"]["id"]

        get_response = requests.get(f"{base_url}/items/{item_id}")
        assert get_response.status_code == 200
        retrieved_item = get_response.json()
        assert retrieved_item["item"]["name"] == item_data["name"]

        list_response = requests.get(f"{base_url}/items/")
        assert list_response.status_code == 200
        items_list = list_response.json()
        assert items_list["total"] >= 1

    def test_api_performance_under_load(self, fastapi_server):
        base_url = fastapi_server.base_url

        response_times = []
        for _ in range(10):
            start_time = time.time()
            response = requests.get(f"{base_url}/health")
            end_time = time.time()

            assert response.status_code == 200
            response_times.append(end_time - start_time)

        avg_response_time = sum(response_times) / len(response_times)
        assert avg_response_time < 0.1, (
            f"Average response time too high: {avg_response_time}s"
        )

    def test_error_handling_e2e(self, fastapi_server):
        base_url = fastapi_server.base_url

        invalid_item_response = requests.post(
            f"{base_url}/items/", json={"invalid": "data"}
        )
        assert invalid_item_response.status_code == 422

        nonexistent_response = requests.get(f"{base_url}/items/999999")
        assert nonexistent_response.status_code == 200
