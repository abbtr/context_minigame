import uvicorn
from src import create_fastapi_app  

app = create_fastapi_app()

if __name__ == "__main__":
    # Start the FastAPI app using Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)