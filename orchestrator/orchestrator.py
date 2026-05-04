import time

from crawler.crawler import run_crawler
from cleaning.clean import run_cleaning
from analytics.analyze import run_analysis


from orchestrator.dag import dag
from orchestrator.executor import execute_dag


MAX_RETRIES = 10
RETRY_DELAY = 5


def run_with_retry(task, task_name):

    for attempt in range(1, MAX_RETRIES + 1):

        try:
            print(f"Running {task_name} | Attempt {attempt}")

            task()

            print(f"{task_name} completed successfully")

            return

        except Exception as e:

            print(f"{task_name} failed: {e}")

            if attempt == MAX_RETRIES:
                print(f"{task_name} failed after {MAX_RETRIES} retries")
                raise

            print(f"Retrying in {RETRY_DELAY} seconds...")
            time.sleep(RETRY_DELAY)


def run_pipeline(url: str | None = None):

    print("Starting DAG Pipeline")
    if url:
        print(f"Pipeline received URL: {url}")

    execute_dag(dag)

    print("Pipeline Finished")

    print("Pipeline Finished")