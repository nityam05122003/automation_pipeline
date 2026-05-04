class Task:

    def __init__(self, name, func, retries=0, retry_delay=0):
        self.name = name
        self.func = func
        self.dependencies = []
        self.retries = retries
        self.retry_delay = retry_delay

    def depends_on(self, task):
        self.dependencies.append(task)