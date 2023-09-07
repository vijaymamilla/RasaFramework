from fastapi import FastAPI, Request
from typing import Dict

app = FastAPI()


@app.get("/api/v1/health", summary="Health check", description="Check if the API is up.")
async def get_health_check_status() -> Dict:
    """Generate a health check response for the applications."""
    return {"status": "UP", "details": "Application is running normally."}

if __name__ == '__main__':
    print('main function called')