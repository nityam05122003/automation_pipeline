# def execute_dag(tasks):

#     executed = set()

#     def execute(task):

#         for dependency in task.dependencies:
#             if dependency.name not in executed:
#                 execute(dependency)

#         if task.name not in executed:
#             print(f"Running {task.name}")
#             task.func()
#             executed.add(task.name)

#     for task in tasks:
#         execute(task)

import time


def execute_dag(tasks):

    executed = set()

    def execute(task):

        for dependency in task.dependencies:
            if dependency.name not in executed:
                execute(dependency)

        if task.name not in executed:

            attempts = 0

            while attempts <= task.retries:

                try:
                    print(f"Running {task.name} (attempt {attempts+1})")

                    task.func()

                    print(f"{task.name} completed")

                    executed.add(task.name)

                    return

                except Exception as e:

                    attempts += 1

                    print(f"{task.name} failed: {e}")

                    if attempts > task.retries:
                        print(f"{task.name} failed after retries")
                        raise

                    print(f"Retrying {task.name} in {task.retry_delay} seconds")

                    time.sleep(task.retry_delay)

    for task in tasks:
        execute(task)