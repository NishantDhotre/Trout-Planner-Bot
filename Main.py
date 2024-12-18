import subprocess

# ==========================
# 1. ENTRY POINT FOR THE APPLICATION
# ==========================

if __name__ == "__main__":
    # Start FastAPI backend in a subprocess
    print("Starting FastAPI backend...")
    subprocess.Popen(["uvicorn", "backend.agent_api:app",
                     "--host", "0.0.0.0", "--port", "8000"])

    # Start Streamlit app in a separate subprocess
    print("Starting Streamlit frontend...")
    subprocess.run(["streamlit", "run", "frontend/chat_interface.py"])
