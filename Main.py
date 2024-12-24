import subprocess
import time

# ==========================
# ENTRY POINT FOR THE APPLICATION
# ==========================


def start_backend():
    """Starts the FastAPI backend."""
    print("Starting FastAPI backend...")
    return subprocess.Popen(
        ["uvicorn", "backend.agent_api:app", "--host", "0.0.0.0", "--port", "8000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )


def start_frontend():
    """Starts the Streamlit frontend."""
    print("Starting Streamlit frontend...")
    return subprocess.Popen(
        ["streamlit", "run", "frontend/chat_interface.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )


def shutdown_process(process, name):
    """Terminates a subprocess."""
    if process and process.poll() is None:
        print(f"Shutting down {name}...")
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            print(f"{name} did not terminate, killing it...")
            process.kill()


if __name__ == "__main__":
    backend_process = None
    frontend_process = None

    try:
        # Start the backend
        backend_process = start_backend()
        time.sleep(2)  # Give backend some time to start

        # Start the frontend
        frontend_process = start_frontend()

        # Keep the main thread alive to monitor processes
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nReceived KeyboardInterrupt, shutting down...")
    finally:
        # Ensure both processes are terminated properly
        shutdown_process(backend_process, "FastAPI backend")
        shutdown_process(frontend_process, "Streamlit frontend")
        print("All processes terminated. Goodbye!")
