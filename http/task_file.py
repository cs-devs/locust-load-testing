from locust import HttpUser, between, task
class WebsiteUser(HttpUser):
    wait_time = between(0, 5)

    @task(1)
    def FeatureFlags_1(self):
        self.client.get('api/FeatureFlags/IsEnabled/5330', headers={'Authorization': '$token', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def FeatureFlags_2(self):
        self.client.get('api/FeatureFlags/IsEnabled/5176', headers={'Authorization': '$token', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def getCountries(self):
        self.client.get('api/geo/countries', headers={'Authorization': '$token', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def FeatureFlags_3(self):
        self.client.get('api/FeatureFlags/IsEnabled/5188', headers={'Authorization': '$token', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def Candidates(self):
        self.client.get('api/Candidates/14466', headers={'Authorization': '$token', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def ProfileStatus(self):
        self.client.get('api/ProfileStatus/Lookup', headers={'Authorization': '$token', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def Countries2(self):
        self.client.get('api/geo/countries/PH', headers={'Authorization': '$token', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def Countries3(self):
        self.client.get('api/geo/countries/PH/regions', headers={'Authorization': '$token', 'Cache-control': 'disable', 'Cookie': 'abc'})

    @task(1)
    def Countries4(self):
        self.client.get('api/geo/countries/PH/region/PAM/cities', headers={'Authorization': '$token', 'Cache-control': 'disable', 'Cookie': 'abc'})

