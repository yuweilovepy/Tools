"""
import os
cmd = 'ls'
res = os.popen(cmd)
output_str = res.read()   # 获得输出字符串
print(output_str)


adb_proc = subprocess.Popen(cmd_list,
                            stdin = subprocess.PIPE,
                            stdout = subprocess.PIPE,
                            stderr = subprocess.PIPE,
                            shell = False)
(__output,__error) = adb_proc.communicate()
self.__return = adb_proc.returncode

其中shell=False的时候cmd_list是一个列表，shell=True的时候cmd_list是一个字符串，即要执行的命令，例如

subprocess.Popen(["adb","-s","device_id"], shell=Fale)
subprocess.Popen("adb -s device_id", shell=True)

"""

import subprocess,sys



cmd1='netsh interface ip set dns "以太网" source=static addr=172.16.0.18'

cmd2='netsh interface ip set dns name="以太网" source=dhcp'

while True:
	env=input("change_dns(1-on/2-off):")
	if env=="1":
		res=subprocess.Popen(cmd1)
		if res is None:
			print("执行失败!")
		else:
			print("%s:执行成功！" % cmd1)
	elif env=="2":
		res=subprocess.Popen(cmd2)
		if res is None:
			print("执行失败!")
		else:
			print("%s:执行成功！" % cmd2)
	else:
		sys.exit()