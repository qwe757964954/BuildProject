

import json


class ModifyHotUpdateTask(object):
    def __init__(self,args):
        self.build_params = args
    def __updateHotUpdate(self):
        with open('./config_json/buildConfig_android.json','r') as file:
            data = json.load(file)
        data["packages"]["hl-plugin-hot-update"]["hotUpdateVersion"] = self.build_params.get("HotVersion")
        data["packages"]["hl-plugin-hot-update"]["hotUpdateAddress"] = self.build_params.get("HotServer")
        with open('./config_json/buildConfig_android.json','w') as file:
            json.dump(data, file, indent=4)
    def run(self):
        self.__updateHotUpdate()