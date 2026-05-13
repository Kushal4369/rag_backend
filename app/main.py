from fastapi import FastAPI

app = FastAPI(
    title="Production RAG System",
    version="1.0.0"
)

@app.get("/")
async def health_check():
    return {
        "status": "healthy",
        "message": "RAG system running"
    }
