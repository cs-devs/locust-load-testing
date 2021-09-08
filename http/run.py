import os, fnmatch
import sys

def findProject(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


for filename in findProject('project', 'task_file.py'):
    try:
        if filename.split("/")[1] == sys.argv[1]:
                task="python3 -m locust -f " + str(filename)
                print(task)
                result = os.system(task)
                if result == 9009:
                    task="python -m locust -f " + str(filename)
                    print(task)
                    result = os.system(task)
                    if result == 9009:
                        print("Error: Invalid project")
           

    except:
        if filename.split("\\")[1] == sys.argv[1]:
            task="python3 -m locust -f " + str(filename)
            print(task)
            result = os.system(task)
            if result == 9009:
                    task="python -m locust -f " + str(filename)
                    print(task)
                    result = os.system(task)
                    if result == 9009:
                        print("Error: Invalid project")
           