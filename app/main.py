from fastapi import FastAPI

app = FastAPI(title="AI Skill Gap Analyzer")


@app.get("/health")
def health():
    return {"status": "ok"}