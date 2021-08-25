import time
import requests
import os
import random
import json


def tokenGenerator(token_var, expire_time, method, param, url):

    while True:
        
        #os.environ[token_var] =str(random.choice("ABCDEFGH"))    
        if method == "post":
             http = requests.post(url, data = param)
             os.environ[token_var] = str(json.loads(http.content.decode())['token'])#str(token_var) + str(random.choice("ABCDEFGH")) 
             print(os.getenv(token_var))
        time.sleep(5)
        