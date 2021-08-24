import json

task_set = open ("./json/task.json", "r").read()

#,
      #{
     #    "task_name":"task_donothing",
     #    "path" : "/do_nothing",
      #   "weight":3,
      #   "method":"get",
      #   "headers":{"cookie" : "abc"},
      #   "data":""
      #}


task_set = json.loads(task_set)

def addTasks(json):
    save_py = open("task_file.py", "w")
    _header = "from locust import HttpUser, between, task\n"
    _class = "class WebsiteUser(HttpUser):\n    wait_time = between(0, 5)\n\n"
    save_py.write(_header)
    save_py.write(_class)

    for task in json['tasks']:
        print(task)
        _get = "        self.client.get('%s', headers=%s)\n\n" % (task['path'], task['headers'])
        _post = "        self.client.post('%s', data=%s, headers=%s)\n\n" % (task['path'] , task['data'],task['headers'] )

        
        
        _func = "    @task(%s)\n    def %s(self):\n" % (task['weight'],task['task_name'])

        
        save_py.write(_func)
        if task['method'] == "get":
            save_py.write(_get)
        elif task['method'] == "post":
            save_py.write(_post)
        print("\nTask created successfully\n")


addTasks(task_set)