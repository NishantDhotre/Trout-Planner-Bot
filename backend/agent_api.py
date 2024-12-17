from fastapi import FastAPI


app = FastAPI()

@app.post("/agent")
async def agent_endpoint(message: dict):
    user_input = message.get("message", "")
    response = {"response": f"You said: {user_input}"}
    return response