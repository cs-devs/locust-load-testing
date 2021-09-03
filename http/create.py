import json
from decouple import config
import time
import os

task_set = open ("./json/task.json", "r").read()
task_set = json.loads(task_set)
token = config("token")

def addTasks(json):
    save_py = open("task_file.py", "w")

    _header = "from locust import HttpUser, between, task\nimport os\nimport threading\n"

    _token_generator = "from modules.http import tokenGenerator\n\n"

    _class = "class WebsiteUser(HttpUser):\n    wait_time = between(0, 5)\n\n\n"

    save_py.write(_header)
    save_py.write(_token_generator)

    try: ### Token dynamic
        token_data = json['token_generator']
        
        for token_data in token_data:
           print(token_data) 
        #    save_py.write("tokenGenerator('%s', %s, '%s', %s, '%s')\n" % (token["name"],token["expire_time"], token["method"], token["parameter"], token["url"]))
        save_py.write("thread = threading.Thread(target=tokenGenerator, args=('%s',%s,'%s',%s,'%s',))\nthread.start()" % (token_data["name"],token_data["expire_time"], token_data["method"], token_data["parameter"], token_data["url"]))
        save_py.write("\n\n")
    except Exception as error:
        print(error)
        

    save_py.write(_class)

    for task in json['tasks']:
        print(task)
        _get = "        self.client.get('%s', headers=%s)\n\n" % (task['path'], task['headers'])
        _post = "        self.client.post('%s', data=%s, headers=%s)\n\n" % (task['path'] , task['data'],task['headers'] )

        
        
        _func = "    @task(%s)\n    def %s(self):\n" % (task['weight'],task['task_name'])

        #### Token variables
        if task['headers']['Authorization'] == "$token":
             headers = {}
             headers["Authorization"] = token
             task['headers'].pop("Authorization")
             headers.update(task['headers'])
             _post = "        self.client.post('%s', data=%s, headers=%s)\n\n" % (task['path'] , task['data'], headers)
             _get = "        self.client.get('%s', headers=%s)\n\n" % (task['path'], headers)
            

        elif "$token_" in task['headers']['Authorization']:
             token_var = str(task['headers']['Authorization']).replace("$token_","")
             task['headers'].pop("Authorization")
             print(">>>>>>>>",task['headers'])
       

             _get = "        self.client.get('%s', headers={'Authorization' : os.getenv('%s'),%s})\n\n" % (task['path'], token_var, str(task['headers']).replace("{","").replace("}",""))

              #     _post = "        self.client.post('%s', data=%s, headers=%s)\n\n" % (task['path'] , task['data'],{ "Authorization" : "os.getenv(token_var)"})
       
            
  
        save_py.write(_func)
        if task['method'] == "get":
            save_py.write(_get)
        elif task['method'] == "post":
            save_py.write(_post)
        print("\nTask created successfully\n")


addTasks(task_set)

# while True:
#     time.sleep(1)
#     os.environ['pass'] = "000"
#     print(os.getenv('pass'))