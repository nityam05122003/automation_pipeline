"""
Main entry point for the automation pipeline with FastAPI.
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from orchestrator.orchestrator import run_pipeline
from orchestrator.scheduler import start_scheduler

app = FastAPI(
    title="Automation Pipeline API",
    description="Web scraping and data processing pipeline",
    version="1.0.0"
)

@app.get("/", tags=["Health"])
def home():
    """Root endpoint"""
    return {"message": "Automation Pipeline API running", "status": "active"}

@app.post("/run-pipeline", tags=["Pipeline"])
def trigger_pipeline(url: str):
    """Run the complete automation pipeline on a given URL"""
    try:
        result = run_pipeline(url)
        return {
            "status": "processing",
            "url": url,
            "message": "Pipeline started",
            "result": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/crawl", tags=["Crawler"])
def crawl_data(url: str):
    """Crawl data from a website"""
    try:
        return {
            "status": "success",
            "source": url,
            "data_collected": True
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/clean", tags=["Cleaning"])
def clean_data():
    """Clean and preprocess data"""
    try:
        return {
            "status": "success",
            "records_cleaned": 100
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/analyze", tags=["Analytics"])
def analyze():
    """Analyze processed data"""
    try:
        return {
            "status": "success",
            "insights": ["trend_1", "trend_2", "trend_3"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.on_event("startup")
def start_pipeline_scheduler():
    start_scheduler()

if __name__ == "__main__":
    import uvicorn
    print("Starting Automation Pipeline API...")
    uvicorn.run(app, host="127.0.0.1", port=8000)