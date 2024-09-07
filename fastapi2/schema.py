from pydantic import BaseModel, HttpUrl
from typing import List, Dict, Any

class ReportPayload(BaseModel):
    session_id: str
    transcript: List[Dict[str, str]]
    transcript_analytics_prompt: str

class CsvAnalyticsHeader(BaseModel):
    header: str
    description: str

class FileData(BaseModel):
    file_url: HttpUrl
    file_name: str

class UrlValidation(BaseModel):
    file: FileData
    session_id: str
    transcript: List[Dict[str, str]]

class ResponseValidation(BaseModel):
    session_id: str
    transcript: List[Dict[str, str]]
    transcript_analytics: Dict[str, Any]
