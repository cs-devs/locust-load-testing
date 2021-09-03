# Multiple project file structure

* project
  * [project name]
    * json
    * task
 

# Build the locust script via task.json file
* Static token variable: $token


       {
          "task_name":"dump",
          "path" : "/dump",
          "weight":1,
          "method":"get",
          "headers":
          {
             "Authorization" : "$token", 
             "Cache-control" : "disable",
             "Cookie" : "abc"
          },
          "data" : ""
       }

# Build a task file from a project
* python3 create.py --build-project [project name]
 
 # Run locust
 * python3 run.py [project name]
