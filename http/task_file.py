from locust import HttpUser, between, task
import os
import threading
from modules.http import tokenGenerator

thread = threading.Thread(target=tokenGenerator, args=('john',30,'post',{'username': 'admin2', 'password': 'admin2'},'http://127.0.0.1:5000/login',))
thread.start()

class WebsiteUser(HttpUser):
    wait_time = between(0, 5)


    @task(1)
    def dump(self):
        self.client.get('/dump', headers={'Authorization' : os.getenv('john'),'Cache-control': 'disable', 'Cookie': 'abc'})

