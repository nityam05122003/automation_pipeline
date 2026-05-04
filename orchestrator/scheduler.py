"""Scheduler utilities for the automation pipeline."""

import threading
import time

from orchestrator.orchestrator import run_pipeline


def _scheduled_pipeline_loop(interval_seconds: int = 3600) -> None:
    """Run the pipeline repeatedly in a background thread."""
    while True:
        print("Scheduler triggered pipeline run")
        try:
            run_pipeline()
        except Exception as exc:
            print(f"Scheduled pipeline failed: {exc}")
        time.sleep(interval_seconds)


def start_scheduler(interval_seconds: int = 3600) -> None:
    """Start the background scheduler thread."""
    thread = threading.Thread(
        target=_scheduled_pipeline_loop,
        args=(interval_seconds,),
        daemon=True,
    )
    thread.start()
    print("Pipeline scheduler started")
