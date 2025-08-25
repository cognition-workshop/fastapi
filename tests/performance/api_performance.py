import statistics
import time
from typing import Optional

from fastapi import FastAPI
from starlette.testclient import TestClient


def create_test_app():
    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"message": "Hello World"}

    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Optional[str] = None):
        return {"item_id": item_id, "q": q}

    @app.post("/items/")
    def create_item(item: dict):
        return {"item": item, "created": True}

    return app


def benchmark_endpoint(
    client: TestClient, method: str, url: str, data=None, iterations=100
):
    times = []

    for _ in range(iterations):
        start_time = time.time()

        if method.upper() == "GET":
            response = client.get(url)
        elif method.upper() == "POST":
            response = client.post(url, json=data)

        end_time = time.time()

        if response.status_code < 400:
            times.append((end_time - start_time) * 1000)

    if times:
        return {
            "endpoint": f"{method.upper()} {url}",
            "iterations": len(times),
            "avg_response_time_ms": round(statistics.mean(times), 2),
            "min_response_time_ms": round(min(times), 2),
            "max_response_time_ms": round(max(times), 2),
            "median_response_time_ms": round(statistics.median(times), 2),
            "p95_response_time_ms": round(statistics.quantiles(times, n=20)[18], 2)
            if len(times) >= 20
            else None,
        }
    return None


def run_performance_benchmarks():
    app = create_test_app()
    client = TestClient(app)

    benchmarks = [
        ("GET", "/"),
        ("GET", "/items/1"),
        ("GET", "/items/1?q=test"),
        ("POST", "/items/", {"name": "Test Item", "price": 10.5}),
    ]

    results = []

    print("Running API performance benchmarks...")

    for method, url, *data in benchmarks:
        payload = data[0] if data else None
        result = benchmark_endpoint(client, method, url, payload)
        if result:
            results.append(result)
            print(f"✓ {result['endpoint']}: {result['avg_response_time_ms']}ms avg")

    return results


if __name__ == "__main__":
    results = run_performance_benchmarks()

    print("\n=== Performance Benchmark Results ===")
    for result in results:
        print(f"""
Endpoint: {result["endpoint"]}
Iterations: {result["iterations"]}
Average Response Time: {result["avg_response_time_ms"]}ms
Min Response Time: {result["min_response_time_ms"]}ms
Max Response Time: {result["max_response_time_ms"]}ms
Median Response Time: {result["median_response_time_ms"]}ms
95th Percentile: {result["p95_response_time_ms"]}ms
        """)
