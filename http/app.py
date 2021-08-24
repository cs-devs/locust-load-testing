from gevent import monkey
monkey.patch_all()
from flask import Flask
from flask_restful import Resource, Api, request
import json
from flask_cors import CORS
app = Flask(__name__)
api = Api(app)
CORS(app)



def addTasks(task_name, path, weight, method, headers, data):
        save_py = open("task_file.py", "a")
    # _header = "from locust import HttpUser, between, task\n"
    # _class = "class WebsiteUser(HttpUser):\n    wait_time = between(0, 5)\n\n"
    # save_py.write(_header)
    # save_py.write(_class)
        #print(task)
        _get = "        self.client.get('%s', headers=%s)\n\n" % (path,  headers)
        _post = "        self.client.post('%s', data=%s, headers=%s)\n\n" % (path , data, headers )
        _func = "    @task(%s)\n    def %s(self):\n" % (weight,task_name)
        save_py.write(_func)
        if method == "get":
            save_py.write(_get)
        elif method == "post":
            save_py.write(_post)

class CreateTask(Resource):
    def post(self):
        task_name = request.form['task_name'] 
        path = request.form['path']  
        weight = request.form['weight']
        method = request.form['method']
        headers = request.form['headers'] 
        data = request.form['data'] 
        addTasks(task_name,path, weight, method, headers, data)
        return {"message" : "ok"}

class ClearTask(Resource):
    def post(self):
        save_py = open("task_file.py", "w")
        _header = "from locust import HttpUser, between, task\n"
        _class = "class WebsiteUser(HttpUser):\n    wait_time = between(0, 5)\n\n\n\n"
        save_py.write(_header)
        save_py.write(_class)
        return {"message" : "ok"}

class GetTaskList(Resource):
    
    def get(self):
        task_arr = []
        tasks = open("task_file.py", "r")
        loop = 0
        for task in tasks:
            loop = loop + 1
            
            if loop > 4:
                    print(task.replace("@", ""))
                    task_arr.append(task)
        print(loop)
        return {"task" : str(task_arr).replace("\\n","").replace("\\","")}


api.add_resource(CreateTask, "/create/task")
api.add_resource(ClearTask, "/clear/task")
api.add_resource(GetTaskList,"/task/list")

if __name__ == '__main__':
    app.run(debug=True)
