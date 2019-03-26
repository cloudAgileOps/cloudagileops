from locust import HttpLocust, TaskSet, task


class UserTasks(TaskSet):
    
    @task
    def getreport(self):
        self.client.get("/report")
    
class WebsiteUser(HttpLocust):
    """
    Locust user class that does requests to the locust web server running on localhost
    """
    host = "http://127.0.0.1:8089"
    min_wait = 2000
    max_wait = 5000
    task_set = UserTasks
