import csv
import requests
import asyncio
from io import StringIO
from fastapi import HTTPException
from schema import ReportPayload, UrlValidation, CsvAnalyticsHeader, ResponseValidation
from enums import GenAIServicesEnum
from service.base import GenAIProcessor

class ServiceManager:

    # This dictionary will simulate a "pending" session waiting for LLM response.
    pending_sessions = {}

    @staticmethod
    async def process_report(service_name: GenAIServicesEnum, payload: ReportPayload):
        # Since we do not have access to the LLM API keys, we'll return dummy analytics
        dummy_analytics = {
            "session_id": payload.session_id,
            "transcript_analytics": {"dummy_key": "dummy_value"}
        }
        return dummy_analytics

    @staticmethod
    async def process_report_csv(service_name: GenAIServicesEnum, payload: UrlValidation):
        # Simulate a waiting period for LLM response
        # Store the request in pending_sessions to simulate a wait state
        session_id = payload.session_id
        ServiceManager.pending_sessions[session_id] = payload

        # Simulating waiting for LLM response
        await asyncio.sleep(5)  # 5 seconds wait to simulate asynchronous waiting
        
        # Return a placeholder message saying that the system is waiting for LLM response
        return {
            "status": "waiting_for_llm",
            "message": f"Session {session_id} is now waiting for LLM response.",
            "session_id": session_id
        }

    @staticmethod
    async def process_llm_response(session_id: str, llm_response: str):
        # Retrieve the original request stored in pending_sessions
        if session_id not in ServiceManager.pending_sessions:
            raise HTTPException(status_code=404, detail=f"Session {session_id} not found.")

        payload = ServiceManager.pending_sessions[session_id]

        # Validate and download the CSV file
        try:
            response = requests.get(payload.file.file_url)
            response.raise_for_status()
        except requests.RequestException as e:
            raise HTTPException(status_code=400, detail=f"Failed to download file: {str(e)}")

        # Parse the CSV content
        content = response.content.decode('utf-8')
        csv_reader = csv.reader(StringIO(content))

        # Read headers and descriptions from the first two rows of the CSV
        try:
            headers = next(csv_reader)  # Row 1: Headers
            descriptions = next(csv_reader)  # Row 2: Descriptions
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error reading CSV: {str(e)}")

        # Create a list of CsvAnalyticsHeader objects
        analytics_headers = [
            CsvAnalyticsHeader(header=header, description=description)
            for header, description in zip(headers, descriptions)
        ]

        # Incorporate LLM response into analytics (This can be more complex as needed)
        dummy_analytics = {header.header: f"LLM analysis: {llm_response}" for header in analytics_headers}

        # Prepare the response
        response_data = ResponseValidation(
            session_id=session_id,
            transcript=payload.transcript,
            transcript_analytics=dummy_analytics
        )

        # Remove the session from pending after completion
        del ServiceManager.pending_sessions[session_id]

        return response_data
