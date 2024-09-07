import csv
from io import StringIO
from service.base import GenAIProcessor
from schema import CsvAnalyticsHeader, UrlValidation, ResponseValidation
import json

class LlamaProcessor(GenAIProcessor):
    service_name = "llama"

    async def getAnalytics(self, transcript: str, prompt: str):
        # Implement your analytics logic for Llama here
        return {"dummy_key": "Llama analytics"}

    async def getCsvAnalytics(self, payload: UrlValidation, url_response):
        content = url_response.content.decode('utf-8')
        csv_reader = csv.reader(StringIO(content))

        headers = next(csv_reader)
        descriptions = next(csv_reader)

        analytics_data = [
            CsvAnalyticsHeader(header=header, description=description)
            for header, description in zip(headers, descriptions)
        ]

        # Generate dummy analytics based on the headers
        dummy_analytics = {header.header: f"Dummy analysis for {header.description}" for header in analytics_data}

        return ResponseValidation(
            session_id=payload.session_id,
            transcript=payload.transcript,
            transcript_analytics=dummy_analytics
        )
