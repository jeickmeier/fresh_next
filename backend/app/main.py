import uvicorn
from fastapi import FastAPI

from endpoints import genai, risk

def start() -> None:

    app = FastAPI(
        title="Gen UI Backend",
        version="1.0",
        description="A simple api server",
    )

    app.include_router(genai.router)
    app.include_router(risk.router)

    print("Starting server...")
    uvicorn.run(app, host="0.0.0.0", port=3001)


if __name__ == "__main__":
    start()