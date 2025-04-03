from fastapi import BackgroundTasks
import pytest
from typing import List

pytestmark = pytest.mark.asyncio

async def test_background_tasks_add_task():
    """Test the BackgroundTasks.add_task method."""
    background_tasks = BackgroundTasks()
    
    task_results: List[str] = []
    
    def sample_task(message: str):
        task_results.append(message)
    
    background_tasks.add_task(sample_task, "test message")
    
    await background_tasks()
    
    assert task_results == ["test message"]

async def test_background_tasks_add_multiple_tasks():
    """Test adding multiple tasks to BackgroundTasks."""
    background_tasks = BackgroundTasks()
    
    task_results: List[str] = []
    
    def sample_task_1(message: str):
        task_results.append(f"Task 1: {message}")
    
    def sample_task_2(message: str):
        task_results.append(f"Task 2: {message}")
    
    background_tasks.add_task(sample_task_1, "hello")
    background_tasks.add_task(sample_task_2, "world")
    
    await background_tasks()
    
    assert task_results == ["Task 1: hello", "Task 2: world"]

async def test_background_tasks_with_async_function():
    """Test BackgroundTasks with async functions."""
    background_tasks = BackgroundTasks()
    
    task_results: List[str] = []
    
    async def async_task(message: str):
        task_results.append(f"Async: {message}")
    
    background_tasks.add_task(async_task, "async test")
    
    await background_tasks()
    
    assert task_results == ["Async: async test"]
