from fastapi import FastAPI

app = FastAPI(
    title="Sumarizer API",
    version="0.0.1",
    description="Third brain for your notes",
)


@app.get("/health")
async def health_check() -> dict:
    return {"status": "ok"}
