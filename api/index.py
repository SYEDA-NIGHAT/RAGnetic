from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def home():
    return {"status": "RAGnetic is live 🚀"}

handler = Mangum(app)
