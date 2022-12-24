from locust import HttpUser, task

class HookUser(HttpUser):
    @task
    def hook_redis_callback(self):
        self.client.post("/hook")

    @task
    def hook_with_sleep_callback(self):
        self.client.post("/hook/sleep")
    #
    # @task
    # def hook_sqlite_callback(self):
    #     self.client.post("/hooksqlite")

    # @task
    # def hook_mysql_callback(self):
    #     self.client.post("/hookmysql")

