import json as js
from decouple import config
import time
import os, fnmatch
import argparse




def addTasks(file):
    try:
        task_set = open(file, "r").read()
        task_set = js.loads(task_set)
        token = config("token")
        json = task_set
        task_path = str(file).replace("json/task.json","task/")+"task_file.py"
        save_py = open(task_path, "w")

        _header = "from locust import HttpUser, between, task\nimport os\nimport threading\n"

        _token_generator = "from modules.http import tokenGenerator\n\n"

        _class = "class WebsiteUser(HttpUser):\n    wait_time = between(0, 5)\n\n\n"

        save_py.write(_header)
        save_py.write(_token_generator)
        
        

        try: ### Token dynamic
            token_gen = json['token_generator']
            
            for token_gen in token_gen:
               print(token_gen) 
            #    save_py.write("tokenGenerator('%s', %s, '%s', %s, '%s')\n" % (token["name"],token["expire_time"], token["method"], token["parameter"], token["url"]))
            save_py.write("thread = threading.Thread(target=tokenGenerator, args=('%s',%s,'%s',%s,'%s',))\nthread.start()" % (token_gen["name"],token_gen["expire_time"], token_gen["method"], token_gen["parameter"], token_gen["url"]))
            save_py.write("\n\n")
        except Exception as error:
            print(error)

            

        save_py.write(_class)

        for task in json['tasks']:
            print(task)
            _get = "        self.client.get('%s', headers=%s)\n\n" % (task['url'].replace(json['domain'][0],""), task['headers'])
            _post = "        self.client.post('%s', data=%s, headers=%s)\n\n" % (task['url'].replace(json['domain'][0],"") , task['data'],task['headers'] )
            _put = "        self.client.put('%s', data=%s, headers=%s)\n\n" % (task['url'].replace(json['domain'][0],"") , task['data'],task['headers'] )
            
            
            _func = "    @task(%s)\n    def %s(self):\n" % (task['weight'], task['url'].replace(json['domain'][0],"").replace("/",""))

            #### Token static
            if task['headers']['Authorization'] == "$token":
                headers = {}
                headers["Authorization"] = token
                task['headers'].pop("Authorization")
                headers.update(task['headers'])
                _post = "        self.client.post('%s', data=%s, headers=%s)\n\n" % (task['url'].replace(json['domain'][0],"") , task['data'], headers)
                _get = "        self.client.get('%s', headers=%s)\n\n" % (task['url'].replace(json['domain'][0],""), headers)
                _put = "        self.client.put('%s', data=%s, headers=%s)\n\n" % (task['url'].replace(json['domain'][0],"") , task['data'], headers)
                
            #### Token dynamic
            elif "$token_" in task['headers']['Authorization']:
                token_var = str(task['headers']['Authorization']).replace("$token_","")
                task['headers'].pop("Authorization")
                #print(">>>>>>>>",task['headers'])
        

                _get = "        self.client.get('%s', headers={'Authorization' : os.getenv('%s'),%s})\n\n" % (task['url'].replace(json['domain'][0],""), token_var, str(task['headers']).replace("{","").replace("}",""))

                #     _post = "        self.client.post('%s', data=%s, headers=%s)\n\n" % (task['url'].replace(json['domain'][0],"") , task['data'],{ "Authorization" : "os.getenv(token_var)"})
        
                
    
            save_py.write(_func)
            if task['method'] == "get":
                save_py.write(_get)
            elif task['method'] == "post":
                save_py.write(_post)
            elif task['method'] == "put":
                save_py.write(_put)
            print("\nTask created successfully\n")
        save_py.close()
    except Exception as error:
        #save_py.close()
        print(error)

def seqTasks(file):
    try:
        task_set = open(file, "r").read()
        task_set = js.loads(task_set)
        token = config("token")
        json = task_set
        task_path = str(file).replace("json/task.json","task/")+"task_file.py"
        save_py = open(task_path, "w")

        _header = "from locust import HttpUser, between, task\nimport os\nimport threading\n"

        _token_generator = "from modules.http import tokenGenerator\n\n"

        _class = "class WebsiteUser(HttpUser):\n    wait_time = between(0, 5)\n\n\n"

        save_py.write(_header)
        save_py.write(_token_generator)
        
        

        try: ### Token dynamic
            token_gen = json['token_generator']
            
            for token_gen in token_gen:
               print(token_gen) 
            #    save_py.write("tokenGenerator('%s', %s, '%s', %s, '%s')\n" % (token["name"],token["expire_time"], token["method"], token["parameter"], token["url"]))
            save_py.write("thread = threading.Thread(target=tokenGenerator, args=('%s',%s,'%s',%s,'%s',))\nthread.start()" % (token_gen["name"],token_gen["expire_time"], token_gen["method"], token_gen["parameter"], token_gen["url"]))
            save_py.write("\n\n")
        except Exception as error:
            print(error)

            

        save_py.write(_class)
        _func = "    @task()\n    def task_sequence(self):\n"
        save_py.write(_func)
        for task in json['tasks']:
            print(task)
            _get = "        self.client.get('%s', headers=%s)\n" % (task['url'].replace(json['domain'][0],""), task['headers'])
            _post = "        self.client.post('%s', data=%s, headers=%s)\n" % (task['url'].replace(json['domain'][0],"") , task['data'],task['headers'] )
            _put = "        self.client.put('%s', data=%s, headers=%s)\n" % (task['url'].replace(json['domain'][0],"") , task['data'],task['headers'] )
            
            
            

            #### Token static
            if task['headers']['Authorization'] == "$token":
                headers = {}
                headers["Authorization"] = token
                task['headers'].pop("Authorization")
                headers.update(task['headers'])
                _post = "        self.client.post('%s', data=%s, headers=%s)\n" % (task['url'].replace(json['domain'][0],"") , task['data'], headers)
                _get = "        self.client.get('%s', headers=%s)\n" % (task['url'].replace(json['domain'][0],""), headers)
                _put = "        self.client.put('%s', data=%s, headers=%s)\n" % (task['url'].replace(json['domain'][0],"") , task['data'], headers)
                
            #### Token dynamic
            elif "$token_" in task['headers']['Authorization']:
                token_var = str(task['headers']['Authorization']).replace("$token_","")
                task['headers'].pop("Authorization")
                #print(">>>>>>>>",task['headers'])
        

                _get = "        self.client.get('%s', headers={'Authorization' : os.getenv('%s'),%s})\n" % (task['url'].replace(json['domain'][0],""), token_var, str(task['headers']).replace("{","").replace("}",""))

                #     _post = "        self.client.post('%s', data=%s, headers=%s)\n\n" % (task['url'].replace(json['domain'][0],"") , task['data'],{ "Authorization" : "os.getenv(token_var)"})
        
                
    
            
            if task['method'] == "get":
                save_py.write(_get)
            elif task['method'] == "post":
                save_py.write(_post)
            elif task['method'] == "put":
                save_py.write(_put)
            print("\nTask created successfully\n")
        save_py.close()
    except Exception as error:
        #save_py.close()
        print(error)





def findProject(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename




#
# while True:
#     time.sleep(1)
#     os.environ['pass'] = "000"
#     print(os.getenv('pass'))





parser = argparse.ArgumentParser(description='Locust file creator.')

parser.add_argument('--build-task', type=str, default="", help='Build a task file.')
parser.add_argument('--build-task-seq', type=str, default="", help='Build a task file with task in order')

args = parser.parse_args()


print(args.build_task)
for filename in findProject('project', '*.json'):
    try:
        if filename.split("/")[1] == args.build_task:
            print(filename)
            addTasks(filename)
    except:
        if filename.split("\\")[1] == args.build_task:
            print(filename)
            addTasks(filename)


print(args.build_task_seq)
for filename in findProject('project', '*.json'):
    try:
        if filename.split("/")[1] == args.build_task:
            print(filename)
            addTasks(filename)
    except:
        if filename.split("\\")[1] == args.build_task:
            print(filename)
            addTasks(filename)
