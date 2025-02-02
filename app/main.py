from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Load student marks from marks.json
with open("marks.json") as f:
    student_marks = json.load(f)

@app.get("/api")
async def get_marks(name: list[str] = Query(...)):
    marks = []
    for student in name:
        if student in student_marks:
            marks.append(student_marks[student])
        else:
            raise HTTPException(status_code=404, detail=f"Student {student} not found")
    return {"marks": marks}
