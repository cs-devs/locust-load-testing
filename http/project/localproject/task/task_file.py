from locust import HttpUser, between, task
import os
import threading
from modules.http import tokenGenerator

class WebsiteUser(HttpUser):
    wait_time = between(0, 5)


    @task(3)
    def login(self):
        self.client.post('/login', data={'username': 'admin', 'password': 'admin'}, headers={'Authorization': '123abc', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(3)
    def _privatebrowserstats(self):
        self.client.post('/_private/browser/stats', data={'{"stats":[{"webVitalTimings":[{"name":"https://github.com/cs-devs/locust-load-testing/blob/rico-multiproject-support/README.md","cls":0}],"timestamp":1630629434350,"loggedIn":true},{"webVitalTimings":[{"name":"https://github.com/cs-devs/locust-load-testing/blob/rico-multiproject-support/README.md","lcp":2422.399}],"timestamp":16306 29434352,"loggedIn":true}]}': ''}, headers={'Authorization': '123abc', 'authority': 'api.github.com', 'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"', 'sec-ch-ua-mobile': '?1', 'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36', 'content-type': 'text/plain;charset=UTF-8', 'accept': '*/*', 'origin': 'https://github.com', 'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'no-cors', 'sec-fetch-dest': 'empty', 'referer': 'https://github.com/', 'accept-language': 'en-US,en;q=0.9', 'cookie': '_ga=GA1.2.1344473559.1602423255; _octo=GH1.1.241395878.1603172846; logged_in=yes; dotcom_user=ricopollantecs; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; tz=Asia%2FManila'})

