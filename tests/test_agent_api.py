import subprocess
import requests
import time

def setup_module(module):
    """Start the FastAPI server."""
    global process
    process = subprocess.Popen(["uvicorn", "backend.agent_api:app", "--host", "127.0.0.1", "--port", "8000"])
    time.sleep(5)  # Allow time for the server to start

def teardown_module(module):
    """Stop the FastAPI server."""
    process.terminate()
    process.wait()

def test_agent_response():
    response = requests.post(
        "http://127.0.0.1:8000/agent",
        json={"message": "Test message"}
    )
    assert response.status_code == 200
    assert response.json()["response"] == "You said: Test message"
