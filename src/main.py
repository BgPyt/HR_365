from fastapi import FastAPI
from src.currency_converter.router import router as currency_router
import uvicorn


app = FastAPI()
app.include_router(currency_router)

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)
