from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from backend.services.rag_chain import answer_query
from backend.services.ingest import process_file

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "DeepDIP backend running"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    return process_file(file)

@app.post("/query/")
async def query_endpoint(query: str):
    return answer_query(query)
