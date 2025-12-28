from pydantic import BaseModel
from typing import List


class QuestionRequest(BaseModel):
    patient_id: str
    question: str


class QAItem(BaseModel):
    question: str
    answer: str
    embedding: List[float]


class PatientData(BaseModel):
    history: str
    qa: List[QAItem] = []

