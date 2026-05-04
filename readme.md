# Automation Pipeline API - Complete Documentation

## Overview

**Automation Pipeline API** is a FastAPI-based web service that orchestrates web scraping, data cleaning, and analysis workflows. It provides a RESTful interface for triggering and managing automated data processing pipelines.

**API Version**: 1.0.0  
**Framework**: FastAPI  
**Server**: Uvicorn  
**Host**: 0.0.0.0  
**Port**: 8000

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [API Endpoints Reference](#api-endpoints-reference)
3. [Request/Response Examples](#requestresponse-examples)
4. [Error Handling](#error-handling)
5. [Authentication & Security](#authentication--security)
6. [Rate Limiting](#rate-limiting)
7. [Data Models](#data-models)
8. [Scheduler Integration](#scheduler-integration)
9. [Development Guide](#development-guide)
10. [Deployment Guide](#deployment-guide)
11. [Troubleshooting](#troubleshooting)

---

## Quick Start

### Prerequisites
- Python 3.8+
- pip package manager
- Virtual environment

### Installation Steps

```bash
# 1. Navigate to project directory
cd /Users/nityanandshukla/Desktop/automation_pipeline

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate virtual environment
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Start the API server
python app/main.py
```

### Expected Output
```
Starting Automation Pipeline API...
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete
```

### Test API is Running
```bash
curl http://localhost:8000/
```

---

## API Endpoints Reference

### Endpoint Summary Table

| Method | Endpoint | Purpose | Parameters | Status Code |
|--------|----------|---------|------------|-------------|
| GET | `/` | Health check | None | 200 |
| POST | `/run-pipeline` | Execute full pipeline | url (required) | 200, 500 |
| GET | `/crawl` | Scrape website data | url (required) | 200, 400 |
| POST | `/clean` | Clean data | None | 200 |
| GET | `/analyze` | Analyze processed data | None | 200 |

---

## Request/Response Examples

### 1. Health Check Endpoint

**Route**: `GET /`

**Tags**: `Health`

**Description**: Verify that the API is running and healthy

**Request Format**:
```bash
curl -X GET http://localhost:8000/ \
  -H "Content-Type: application/json"
```

**Python Request**:
```python
import requests

response = requests.get("http://localhost:8000/")
print(response.json())
```

**JavaScript Request**:
```javascript
fetch('http://localhost:8000/')
  .then(res => res.json())
  .then(data => console.log(data));
```

**Response** (Status: 200 OK):
```json
{
  "message": "Automation Pipeline API running",
  "status": "active"
}
```

**Response Headers**:
```
Content-Type: application/json
Content-Length: 67
```

---

### 2. Run Pipeline Endpoint

**Route**: `POST /run-pipeline`

**Tags**: `Pipeline`

**Description**: Execute the complete automation workflow from data collection to analysis

**Parameters**:

| Name | Type | Required | Description | Example |
|------|------|----------|-------------|---------|
| url | string | Yes | Target website URL to process | https://example.com |

**Request Format**:
```bash
curl -X POST http://localhost:8000/run-pipeline \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

**Alternative Query Parameter Format**:
```bash
curl -X POST "http://localhost:8000/run-pipeline?url=https://example.com"
```

**Python Request**:
```python
import requests

url = "http://localhost:8000/run-pipeline"
params = {"url": "https://example.com"}
response = requests.post(url, params=params)
print(response.json())
```

**Response** (Status: 200 OK):
```json
{
  "status": "processing",
  "url": "https://example.com",
  "message": "Pipeline started",
  "result": {
    "records_processed": 150,
    "data_quality": "high",
    "timestamp": "2026-05-04T10:30:00Z"
  }
}
```

**Error Response** (Status: 500 Internal Server Error):
```json
{
  "detail": "Failed to connect to website. Connection timeout after 30 seconds."
}
```

---

### 3. Crawl Endpoint

**Route**: `GET /crawl`

**Tags**: `Crawler`

**Description**: Extract raw data from a specified website

**Parameters**:

| Name | Type | Required | Description | Example |
|------|------|----------|-------------|---------|
| url | string | Yes | Website URL to crawl | https://example.com |

**Request Format**:
```bash
curl -X GET "http://localhost:8000/crawl?url=https://example.com" \
  -H "Content-Type: application/json"
```

**Python Request**:
```python
import requests

url = "http://localhost:8000/crawl"
params = {"url": "https://example.com"}
response = requests.get(url, params=params)
print(response.json())
```

**JavaScript Request**:
```javascript
fetch('http://localhost:8000/crawl?url=https://example.com')
  .then(res => res.json())
  .then(data => {
    console.log('Crawl Status:', data.status);
    console.log('Data Collected:', data.data_collected);
  });
```

**Response** (Status: 200 OK):
```json
{
  "status": "success",
  "source": "https://example.com",
  "data_collected": true
}
```

**Response with Additional Data**:
```json
{
  "status": "success",
  "source": "https://example.com",
  "data_collected": true,
  "records_count": 250,
  "pages_crawled": 5,
  "execution_time_ms": 3400,
  "content_type": "html"
}
```

**Error Response** (Status: 400 Bad Request):
```json
{
  "detail": "Invalid URL format. URL must start with http:// or https://"
}
```

---

### 4. Clean Endpoint

**Route**: `POST /clean`

**Tags**: `Cleaning`

**Description**: Preprocess, validate, and clean collected data

**Parameters**:

| Name | Type | Required | Description |
|------|------|----------|-------------|
| None | - | - | Current implementation processes pre-loaded data |

**Request Format**:
```bash
curl -X POST http://localhost:8000/clean \
  -H "Content-Type: application/json"
```

**Python Request**:
```python
import requests

response = requests.post("http://localhost:8000/clean")
print(response.json())
```

**Response** (Status: 200 OK):
```json
{
  "status": "success",
  "records_cleaned": 100
}
```

**Response with Additional Details**:
```json
{
  "status": "success",
  "records_cleaned": 100,
  "duplicates_removed": 15,
  "invalid_records": 3,
  "data_quality_score": 0.96
}
```

**Note**: Future versions should accept optional data parameter:
```json
{
  "data": [
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25}
  ]
}
```

---

### 5. Analyze Endpoint

**Route**: `GET /analyze`

**Tags**: `Analytics`

**Description**: Generate insights and patterns from cleaned data

**Parameters**:

| Name | Type | Required | Description |
|------|------|----------|-------------|
| None | - | - | Current implementation analyzes pre-processed data |

**Request Format**:
```bash
curl -X GET http://localhost:8000/analyze \
  -H "Content-Type: application/json"
```

**Python Request**:
```python
import requests

response = requests.get("http://localhost:8000/analyze")
print(response.json())
```

**Response** (Status: 200 OK):
```json
{
  "status": "success",
  "insights": [
    "trend_1",
    "trend_2",
    "trend_3"
  ]
}
```

**Response with Detailed Insights**:
```json
{
  "status": "success",
  "insights": [
    "trend_1: 45% increase in user engagement",
    "trend_2: Peak activity between 2-4 PM",
    "trend_3: Mobile users represent 68% of traffic"
  ],
  "data_points_analyzed": 1250,
  "confidence_level": 0.92,
  "analysis_timestamp": "2026-05-04T10:35:00Z"
}
```

**Future Enhancement - With Parameters**:
```bash
curl -X GET "http://localhost:8000/analyze?data_id=dataset_001&period=weekly"
```

---

## Error Handling

### HTTP Status Codes

| Status Code | Meaning | Scenario |
|-------------|---------|----------|
| 200 | OK | Request successful |
| 400 | Bad Request | Invalid URL or malformed request |
| 404 | Not Found | Endpoint does not exist |
| 422 | Unprocessable Entity | Validation error on parameters |
| 500 | Internal Server Error | Server-side processing error |
| 503 | Service Unavailable | Server overloaded or scheduler error |

### Common Error Responses

**Error 1: Invalid URL Format**
```json
{
  "detail": "Invalid URL format. URL must start with http:// or https://"
}
```
**HTTP Status**: 400 Bad Request

**Solution**: Ensure URL includes protocol (http:// or https://)

---

**Error 2: Connection Timeout**
```json
{
  "detail": "Failed to connect to website. Connection timeout after 30 seconds."
}
```
**HTTP Status**: 500 Internal Server Error

**Solution**: 
- Check if website is accessible
- Verify network connection
- Check firewall rules
- Website may be blocking automated requests

---

**Error 3: Missing Required Parameter**
```json
{
  "detail": "Missing required parameter: url"
}
```
**HTTP Status**: 422 Unprocessable Entity

**Solution**: Provide all required parameters in request

---

**Error 4: Server Error During Processing**
```json
{
  "detail": "Exception occurred: unexpected error during data processing"
}
```
**HTTP Status**: 500 Internal Server Error

**Solution**: 
- Check server logs
- Verify orchestrator module exists
- Ensure all dependencies are installed

---

## Authentication & Security

### Current Implementation
- No authentication required (development mode)
- No API key validation

### Production Recommendations

**1. Implement API Key Authentication**:
```python
from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(name="X-API-Key")

@app.get("/")
def home(api_key: str = Security(api_key_header)):
    if api_key != "your-secret-api-key":
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return {"message": "Authenticated"}
```

**2. Implement Bearer Token (JWT)**:
```python
from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthCredentialDetails

security = HTTPBearer()

@app.get("/")
def home(credentials: HTTPAuthCredentialDetails = Depends(security)):
    # Validate JWT token
    pass
```

**3. Enable HTTPS**:
```python
# Production deployment
uvicorn app.main:app \
  --ssl-keyfile=/path/to/key.pem \
  --ssl-certfile=/path/to/cert.pem \
  --host 0.0.0.0 \
  --port 443
```

---

## Rate Limiting

### Current Implementation
- No rate limiting (development mode)

### Production Implementation

**Using Slowapi**:
```bash
pip install slowapi
```

```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

@app.get("/")
@limiter.limit("100/minute")
def home(request: Request):
    return {"message": "Automation Pipeline API running"}
```

### Rate Limit Recommendations

| Endpoint | Limit | Window |
|----------|-------|--------|
| `/` | 1000 | Per minute |
| `/run-pipeline` | 10 | Per minute |
| `/crawl` | 50 | Per minute |
| `/clean` | 100 | Per minute |
| `/analyze` | 100 | Per minute |

---

## Data Models

### Pipeline Result Model

```python
class PipelineResult(BaseModel):
    status: str  # "processing", "success", "failed"
    url: str  # Input URL
    message: str  # Status message
    result: dict  # Actual processing result
    timestamp: str  # ISO 8601 timestamp
    execution_time_ms: int  # Processing duration
```

### Crawl Response Model

```python
class CrawlResponse(BaseModel):
    status: str  # "success" or "failed"
    source: str  # Source URL
    data_collected: bool  # Whether data was collected
    records_count: int  # Number of records
    pages_crawled: int  # Number of pages
    execution_time_ms: int  # Time taken
```

### Clean Response Model

```python
class CleanResponse(BaseModel):
    status: str
    records_cleaned: int
    duplicates_removed: int
    invalid_records: int
    data_quality_score: float  # 0-1 scale
```

### Analyze Response Model

```python
class AnalyzeResponse(BaseModel):
    status: str
    insights: List[str]
    confidence_level: float  # 0-1 scale
    analysis_timestamp: str
```

---

## Scheduler Integration

### How Scheduler Works

The API includes a background scheduler that automatically runs pipeline tasks:

```python
@app.on_event("startup")
def start_pipeline_scheduler():
    start_scheduler()
```

### Scheduler Features

**1. Automatic Startup**:
- Scheduler starts when API server starts
- Runs background pipeline jobs

**2. Configurable Jobs**:
Located in `orchestrator/scheduler.py`:
```python
# Example: Run pipeline every hour
scheduler.add_job(run_pipeline, 'interval', hours=1)

# Example: Run at specific time daily
scheduler.add_job(run_pipeline, 'cron', hour=2, minute=0)
```

**3. Scheduler States**:

| State | Description | Lifecycle |
|-------|-------------|-----------|
| Stopped | Scheduler not running | Initial |
| Starting | Scheduler initializing | On server startup |
| Running | Active and executing jobs | Normal operation |
| Paused | Temporarily halted | Manual pause |
| Stopped | Scheduler shut down | Server shutdown |

### Manual Scheduler Control

```python
from orchestrator.scheduler import start_scheduler, stop_scheduler, pause_scheduler

# Start scheduler
start_scheduler()

# Stop scheduler
stop_scheduler()

# Pause scheduler
pause_scheduler()
```

---

## Development Guide

### Project Structure

```
automation_pipeline/
├── app/
│   ├── __init__.py
│   └── main.py              ← FastAPI application
├── orchestrator/
│   ├── __init__.py
│   ├── orchestrator.py      ← Pipeline logic
│   └── scheduler.py         ← Scheduler logic
├── tests/
│   ├── test_api.py
│   └── test_endpoints.py
├── requirements.txt
├── .env
└── README.md
```

### Development Setup

```bash
# 1. Install development dependencies
pip install -r requirements.txt
pip install pytest pytest-cov black flake8

# 2. Format code
black app/ orchestrator/

# 3. Lint code
flake8 app/ orchestrator/

# 4. Run tests
pytest tests/ -v --cov
```

### Adding New Endpoints

**Step 1**: Define route in `app/main.py`
```python
@app.get("/new-endpoint", tags=["NewFeature"])
def new_endpoint(param: str):
    """Description of endpoint"""
    return {"status": "success"}
```

**Step 2**: Test endpoint
```bash
curl http://localhost:8000/new-endpoint?param=value
```

**Step 3**: Add unit test in `tests/test_api.py`
```python
def test_new_endpoint():
    response = client.get("/new-endpoint?param=value")
    assert response.status_code == 200
```

### Environment Variables

Create `.env` file:
```env
# API Configuration
API_HOST=127.0.0.1
API_PORT=8000
DEBUG=True

# Scheduler
SCHEDULER_ENABLED=True
SCHEDULER_INTERVAL=3600

# Scraper
REQUEST_TIMEOUT=30
MAX_RETRIES=3
USER_AGENT=Mozilla/5.0 (compatible; AutomationPipeline/1.0)
```

Load in code:
```python
from dotenv import load_dotenv
import os

load_dotenv()
DEBUG = os.getenv("DEBUG", False)
API_PORT = int(os.getenv("API_PORT", 8000))
```

---

## Deployment Guide

### Development Server

```bash
python app/main.py
```

Starts on `http://0.0.0.0:8000`

### Production Deployment

**Option 1: Gunicorn + Uvicorn**
```bash
pip install gunicorn

gunicorn app.main:app \
  -w 4 \
  -k uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000
```

**Option 2: Docker**

Create `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:
```bash
docker build -t automation-pipeline .
docker run -p 8000:8000 automation-pipeline
```

**Option 3: Docker Compose**

Create `docker-compose.yml`:
```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
      - SCHEDULER_ENABLED=True
    restart: unless-stopped
    volumes:
      - ./logs:/app/logs
```

Run:
```bash
docker-compose up -d
```

### Environment for Production

Update `.env`:
```env
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=False
SCHEDULER_ENABLED=True
REQUEST_TIMEOUT=60
```

---

## Troubleshooting

### Issue 1: Module Import Error

**Error**:
```
ModuleNotFoundError: No module named 'orchestrator'
```

**Cause**: Not running from project root or module not installed

**Solution**:
```bash
# Ensure in correct directory
cd /Users/nityanandshukla/Desktop/automation_pipeline

# Reinstall dependencies
pip install -e .
```

---

### Issue 2: Port Already in Use

**Error**:
```
Address already in use: ('0.0.0.0', 8000)
```

**Cause**: Another process using port 8000

**Solution (Mac)**:
```bash
# Find process
lsof -i :8000

# Kill process
kill -9 <PID>

# OR use different port
python -m uvicorn app.main:app --port 8001
```

---

### Issue 3: Scheduler Not Starting

**Error**: Scheduler doesn't run background jobs

**Solution**:
1. Check if scheduler module exists: `orchestrator/scheduler.py`
2. Verify startup event runs: Add debug print
   ```python
   @app.on_event("startup")
   def start_pipeline_scheduler():
       print("DEBUG: Scheduler starting...")
       start_scheduler()
   ```
3. Check scheduler logs for errors

---

### Issue 4: CORS Errors

**Error**:
```
Access to XMLHttpRequest blocked by CORS policy
```

**Solution**: Add CORS middleware:
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

### Issue 5: Website Returns 403 Forbidden

**Error**: Scraper blocked by website

**Solutions**:
- Add User-Agent header
- Implement rate limiting/delays
- Use proxy services
- Respect robots.txt

---

## Performance Tips

1. **Connection Pooling**: Reuse connections
2. **Async Operations**: Use async/await for I/O
3. **Caching**: Cache frequent requests
4. **Batch Processing**: Process data in batches
5. **Logging**: Implement efficient logging

---

## Support & Contact

For issues or questions:
- Check GitHub issues
- Review logs: `tail -f logs/app.log`
- Email: support@automationpipeline.dev

---

**Documentation Version**: 1.0.0  
**Last Updated**: May 4, 2026  
**Status**: Active & Maintained# automation_pipeline
