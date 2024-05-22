
import subprocess
class BuildAndroidTask(object):
    def __init__(self,args):
        self.build_params = args
    def __create_android_project(self):
        ProjectPath = self.build_params.get('ProjectPath')
        CocosPath = self.build_params.get('CocosPath')
        params = '''configPath=./config_json/buildConfig_android.json'''
        command = f"{CocosPath} --project {ProjectPath} --build {params}"
        try:
            # 在命令行中执行构建命令，并捕获输出
            subprocess.run(command, shell=True, check=True)
            print("构建成功！")
        except subprocess.CalledProcessError as e:
            if e.returncode == 36:
                print("构建成功！")
            else:
                print(f"构建失败：{e}")
                print(f"构建失败：{e.returncode}")
    def run(self):
        self.__create_android_project()
