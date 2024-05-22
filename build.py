import json
import os
import sys

from build_android import BuildAndroidTask
from modify_hotupdate import ModifyHotUpdateTask
class Build(object):

    def __init__(self,args):
        self.args = args
    
    def run(self):
        jsonFile = "./build_params.json"
        if(os.path.exists(jsonFile)):
            self.build_params = json.loads(open(jsonFile).read())
            self.__build()
        else:
            print("build_params file not exist")
            exit(0)
    def __build(self):
        self.__modifyHotUpdate()
        if(self.build_params.get("Platform") == "android"):
            self.__build_android()
    def __modifyHotUpdate(self):
        mhot = ModifyHotUpdateTask(self.build_params)
        mhot.run()
    def __build_android(self):
        job = BuildAndroidTask(self.build_params)
        job.run()
if __name__ == '__main__':
    task = Build(sys.argv)
    task.run()
