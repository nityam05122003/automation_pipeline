# from crawler.crawler import run_crawler
# from cleaning.clean import run_cleaning
# from analytics.analyze import run_analysis

# from orchestrator.task import Task


# crawler_task = Task("crawler", run_crawler)
# clean_task = Task("cleaning", run_cleaning)
# analytics_task = Task("analytics", run_analysis)


# clean_task.depends_on(crawler_task)
# analytics_task.depends_on(clean_task)


# dag = [
#     crawler_task,
#     clean_task,
#     analytics_task
# ]

from crawler.crawler import run_crawler
from cleaning.clean import run_cleaning
from analytics.analyze import run_analysis
from orchestrator.task import Task


crawler_task = Task(
    name="crawler",
    func=run_crawler,
    retries=3,
    retry_delay=5
)

clean_task = Task(
    name="cleaning",
    func=run_cleaning,
    retries=2,
    retry_delay=3
)

analytics_task = Task(
    name="analytics",
    func=run_analysis,
    retries=1,
    retry_delay=2
)


clean_task.depends_on(crawler_task)
analytics_task.depends_on(clean_task)


dag = [
    crawler_task,
    clean_task,
    analytics_task
]