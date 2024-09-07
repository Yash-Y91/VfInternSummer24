from fastapi import FastAPI, HTTPException
from schema import ReportPayload, UrlValidation
from enums import GenAIServicesEnum
from service_manager import ServiceManager

app = FastAPI()

@app.post("/genAI/{service_name}/reports")
async def generate_report(service_name: GenAIServicesEnum, payload: ReportPayload):
    result = await ServiceManager.process_report(service_name, payload)
    return {"Service": service_name.value, "Message": result}

@app.post("/genAI/{service_name}/reports_csv")
async def generate_report_csv(service_name: GenAIServicesEnum, payload: UrlValidation):
    result = await ServiceManager.process_report_csv(service_name, payload)
    return result

@app.post("/genAI/{session_id}/llm_response")
async def process_llm_response(session_id: str, llm_response: str):
    # Process the response from the LLM after waiting
    result = await ServiceManager.process_llm_response(session_id, llm_response)
    return result
