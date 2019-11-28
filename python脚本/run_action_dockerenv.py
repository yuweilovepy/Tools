#  已管理员运行某一个程序
import subprocess

subprocess.Popen("runas /savecred /user:Administrator action_docker.bat", shell=True)