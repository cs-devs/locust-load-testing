import os, fnmatch
import sys

def findProject(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


for filename in findProject('project', 'task_file.py'):
    if filename.split("/")[1] == sys.argv[1]:
        task="python3 -m locust -f " + str(filename)
        print(task)
        os.system(task)