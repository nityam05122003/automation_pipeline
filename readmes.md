<!-- Automated Web Data Pipeline with API-Based Orchestration -->

The increasing availability of web data has made automated data pipelines an essential component of modern data engineering systems. Organizations often require systems that can collect data from external sources, process and clean the data, perform analytical calculations, and generate structured reports automatically. This project implements an automated web data pipeline that performs these tasks through a modular architecture and exposes the functionality through an API service. The system is built using Python and the web framework FastAPI, which allows users to trigger the pipeline programmatically.

This code is a simple web crawler used to collect raw data from a website.
It sends an HTTP request to a given URL, parses the webpage using BeautifulSoup, extracts all paragraph text from the HTML, and saves that data into a file called data.txt inside a raw_data folder. This file can later be used for further processing in a data pipeline.

The core objective of this project is to design a simplified yet practical representation of a data engineering workflow. The system automatically collects textual data from a target website, stores the raw content, performs data cleaning operations, analyzes the processed data, and generates a summary report. Each stage of the pipeline is separated into independent modules, which improves maintainability, scalability, and extensibility. The execution of these modules is controlled through an orchestration layer that ensures each step runs sequentially and only after the previous stage has successfully completed.

The architecture of the system is divided into multiple logical layers. The first layer is the API layer, implemented using FastAPI, which exposes REST endpoints that allow users or external systems to trigger the pipeline. This layer acts as the entry point to the system. Once a user sends a request containing the target website URL, the API forwards the request to the orchestration layer. The orchestration layer acts as the controller that manages the execution order of all tasks within the pipeline. It ensures that data collection occurs before cleaning, and cleaning occurs before analytics generation.

The second layer of the architecture is the data ingestion layer, which is responsible for collecting raw data from the web. In this stage, the system sends an HTTP request to the target website using Requests. The HTML response received from the server is then processed using BeautifulSoup, which parses the HTML document and extracts relevant textual content such as paragraphs. The extracted content is stored as raw data in a designated storage directory. This step ensures that the original data is preserved before any transformations are applied.

After the data has been collected, the pipeline moves to the data processing layer. In this stage, the system performs data cleaning operations to remove unnecessary characters, whitespace, and other inconsistencies that may affect analysis. The cleaning process is implemented using Python’s built-in text processing and regular expression tools. By normalizing the text and removing unwanted symbols, the system ensures that the data becomes structured and easier to analyze. The cleaned data is then stored separately from the raw data to maintain a clear distinction between original and processed information.

Once the data cleaning stage is complete, the pipeline proceeds to the analytics layer. In this stage, the processed data is analyzed to generate useful statistics and insights. The analytics module calculates metrics such as the number of paragraphs extracted from the webpage, the total word count of the cleaned dataset, and other textual statistics. These calculations are implemented using pandas, which provides efficient data processing and analytical capabilities. The results of these calculations are compiled into a summary report and stored in a reports directory. This report provides a quick overview of the dataset and can be used for further analysis or monitoring purposes.

The orchestration layer is responsible for coordinating the execution of all modules in the pipeline. Instead of running each script manually, the orchestrator automates the workflow by invoking each stage in a predefined order. When the pipeline is triggered through the API, the orchestrator first calls the crawling module, followed by the cleaning module, and finally the analytics module. This sequential execution ensures that each stage receives the correct input from the previous stage. In large-scale production environments, orchestration is typically handled by dedicated workflow management tools such as Apache Airflow, Prefect, or Dagster. However, for the purposes of this project, orchestration is implemented using a lightweight Python pipeline controller.

The storage layer of the system is organized into multiple directories to maintain separation between different stages of the pipeline. Raw data collected from websites is stored in a raw data folder. After the cleaning process, the transformed data is saved in a clean data folder. Finally, analytical outputs and summary results are stored in a reports directory. This structure ensures transparency in the pipeline workflow and allows developers to inspect intermediate outputs when debugging or extending the system.

The system also includes an automatic API documentation interface generated by FastAPI. The documentation is presented using Swagger UI, which allows users to interactively test the pipeline endpoints directly from a web browser. This feature improves usability and simplifies integration with other services.

In addition to its current capabilities, the architecture is designed to support several future improvements. For example, the pipeline can be enhanced with background task processing using Celery, which allows long-running jobs to execute asynchronously without blocking API responses. Message brokers such as Redis can also be integrated to manage task queues and distributed workers. For deployment and containerization, the application can be packaged using Docker, enabling consistent execution across different environments. In large-scale data platforms, storage could also be extended to cloud object storage services such as Amazon S3.

Overall, this project demonstrates the design and implementation of a modular data pipeline using modern Python tools and web technologies. By combining web scraping, data processing, analytics generation, and API-based orchestration, the system provides a simplified representation of real-world data engineering workflows. The modular architecture allows individual components to be modified or replaced without affecting the entire system, making it a flexible foundation for more advanced data processing platforms.




<!-- Complete System Architecture (Automation Pipeline) -->



                        ┌─────────────────────────────┐
                        │          CLIENT              │
                        │ (Browser / Postman / Curl)  │
                        └──────────────┬──────────────┘
                                       │
                                       │ HTTP Request
                                       ▼
                        ┌─────────────────────────────┐
                        │           FASTAPI            │
                        │   (API Layer / Entry Point)  │
                        │                              │
                        │  /start-pipeline             │
                        │  /pipeline-status            │
                        │  /report                     │
                        └──────────────┬──────────────┘
                                       │
                                       │ triggers
                                       ▼
                        ┌─────────────────────────────┐
                        │        ORCHESTRATOR          │
                        │ (Workflow Controller Layer)  │
                        │                              │
                        │ Libraries:                   │
                        │ • Apache Airflow             │
                        │ • Prefect                    │
                        │ • Custom DAG Executor        │
                        │                              │
                        │ Responsible for:             │
                        │ • Task scheduling            │
                        │ • Task dependencies          │
                        │ • Retry mechanism            │
                        │ • Logging                    │
                        └──────────────┬──────────────┘
                                       │
             ┌─────────────────────────┼──────────────────────────┐
             │                         │                          │
             ▼                         ▼                          ▼

┌────────────────────┐    ┌────────────────────┐     ┌────────────────────┐
│  CRAWLING LAYER    │    │  CLEANING LAYER    │     │  ANALYTICS LAYER   │
│                    │    │                    │     │                    │
│ crawl_data()       │    │ clean_data()       │     │ analyze_data()     │
│                    │    │                    │     │                    │
│ Libraries Used     │    │ Libraries Used     │     │ Libraries Used     │
│ • requests         │    │ • pandas           │     │ • pandas           │
│ • BeautifulSoup    │    │ • regex            │     │ • numpy            │
│ • lxml             │    │ • string utils     │     │                    │
│                    │    │                    │     │ Calculates:        │
│ Extract website    │    │ Removes            │     │ • Paragraph count  │
│ content            │    │ • HTML tags        │     │ • File count       │
│                    │    │ • extra spaces     │     │ • Word count       │
└───────────┬────────┘    └───────────┬────────┘     └───────────┬────────┘
            │                         │                          │
            ▼                         ▼                          ▼

   ┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
   │   RAW DATA      │      │   CLEAN DATA    │      │   REPORT DATA   │
   │   STORAGE       │      │   STORAGE       │      │                 │
   │                 │      │                 │      │                 │
   │ raw_data/       │      │ clean_data/     │      │ report.json     │
   │ page1.txt       │      │ page1_clean.txt │      │ report.csv      │
   │ page2.txt       │      │ page2_clean.txt │      │                 │
   └─────────────────┘      └─────────────────┘      └─────────────────┘


                    ▼
       ┌─────────────────────────────┐
       │        LOGGING SYSTEM        │
       │                              │
       │ Libraries:                   │
       │ • Python logging             │
       │ • loguru                     │
       │                              │
       │ Logs every stage:            │
       │ crawling → cleaning → report │
       └─────────────────────────────┘



<!-- Folder Architecture of the Project -->


automation_pipeline/
│
├── app/
│   ├── main.py
│   └── api_routes.py
│
├── crawler/
│   └── crawler.py
│
├── cleaning/
│   └── clean.py
│
├── analytics/
│   └── analyze.py
│
├── orchestrator/
│   ├── dag.py
│   └── executor.py
│
├── raw_data/
│
├── clean_data/
│
├── reports/
│
├── utils/
│   └── logger.py
│
├── requirements.txt
└── README.md



<!-- Component -->
FastAPI
Airflow
BeautifulSoup
Pandas
File Storage
Local Reports



<!-- Alternative -->
Flask / Django
Prefect / Luigi
Scrapy
Polars
S3 / MinIO
Database (PostgreSQL)

<!-- Complete Pipeline Flow -->


User Request
     │
     ▼
FastAPI Endpoint
     │
     ▼
Pipeline Orchestrator
     │
     ▼
Crawler Module
     │
     ▼
Store Raw Data
     │
     ▼
Cleaning Module
     │
     ▼
Store Clean Data
     │
     ▼
Analytics Module
     │
     ▼
Generate Report
     │
     ▼
Return Results to API


<!-- Continuous Automation Flow -->


Scheduler
   │
   ▼
Start Pipeline
   │
   ▼
Crawl Data
   │
   ▼
Clean Data
   │
   ▼
Analyze Data
   │
   ▼
Generate Report
   │
   ▼
Wait (Interval)
   │
   ▼
Run Again