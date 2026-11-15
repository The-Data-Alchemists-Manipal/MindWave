from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from nlp_model import MOMGenerator
import uvicorn

app = FastAPI(title="MOM Generator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

generator = MOMGenerator()

class TranscriptPayload(BaseModel):
    transcript: str

@app.post("/generate-mom")
async def create_mom(payload: TranscriptPayload):
    try:
        mom_result = generator.generate_mom(payload.transcript)
        return {"mom": mom_result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)