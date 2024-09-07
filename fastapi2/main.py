# main.py

from fastapi2.controllers import app

if __name__ == "__main__":  
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)



# {
#     "session_id": "12345",
#     "transcript": [
#         {"user": "Hi", "bot": "Hello, how can I help you?"},
#         {"user": "I need help with my order", "bot": "Sure, can you provide your order number?"}
#     ],
#     "transcript_analytics_prompt": {
#         "prompt_id": "001",
#         "prompt": "Analyze the tone and topics of this conversation."
#     }
# }

# {
#   "file": {
#     "file_url": "https://raw.githubusercontent.com/Yash-Y91/fastapi2/Yash-Y91-patch-1/fastapi2/example.csv",
#     "file_name": "example.csv"
#   },
#   "session_id": "12345",
#   "transcript": [
#     {"user": "Hi", "bot": "Hello, how can I help you?"},
#     {"user": "I need help with my order", "bot": "Sure, can you provide your order number?"}
#   ]
# }
