from fastapi import FastAPI

app = FastAPI(root_path="/api")

@app.get("/")
def read_root():
    return {"version": "1.0.0"}
