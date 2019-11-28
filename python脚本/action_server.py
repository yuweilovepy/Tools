import paramiko
import warnings
from time import sleep
warnings.filterwarnings("ignore")
import re
from io import StringIO
from io import BytesIO


aly_ip_package={"116.62.166.8":['yunjixinyun','yunjixinyunadmin','xinyunmonitorservice','xinyunservice-assembly'],
"116.62.234.15":['popxinyunservice-assembly','popxinyunadmin'],'47.96.158.187':['xinyunmonitorservice-assembly'],
"116.62.196.200":["immessagedao-assembly",'xinyuncanalconsumer-assembly']}

txy_ip_package={"212.64.94.75":['yunjixinyun','yunjixinyunadmin','xinyunservice-assembly'],
'212.64.52.21':['userother-assembly','xinyunmonitorservice-assembly','xinyunmonitorjob-assembly'],
'212.64.65.170':['popxinyunservice-assembly','popxinyunadmin'],
'212.64.74.58':['immessagedao-assembly','xinyuncanalconsumer-assembly']} #'xinyuncanalconsumer-assembly'  tar 包



#  212.64.74.58  此id是腾讯云临时加入的



env=input("CHOOSE ENV:")
ENV=env.upper()
if ENV=="ALY":
	packagelist=aly_ip_package
elif ENV=="TXY":
	packagelist=txy_ip_package
	


#加一个case判断
print("""
[1]========>yunjixinyun\n
[2]========>yunjixinyunadmin\n
[3]========>xinyunmonitorservice\n
[4]========>xinyunservice-assembly\n
[5]========>imserver-assembly\n
[6]========>popxinyunservice-assembly\n
[7]========>popxinyunadmin\n
[8]========>workorderservice-assembly\n
[9]========>xinyunmonitorservice-assembly\n
[10]=======>immessagedao-assembly\n
[11]=======>xinyuncanalconsumer-assembly\n
[12]=======>xinyunmq-assembly\n
""")

choosepack={1:"yunjixinyun",2:"yunjixinyunadmin",3:"xinyunmonitorservice",4:"xinyunservice-assembly",
5:"imserver-assembly",6:"popxinyunservice-assembly",7:"popxinyunadmin",8:"workorderservice-assembly",
9:"xinyunmonitorservice-assembly",10:"immessagedao-assembly",11:"xinyuncanalconsumer-assembly",
12:"xinyunmq-assembly"
}


#输入数字返回包名
def get_packagename(num):
	for i,v in choosepack.items():
		if i==int(num):
			package=v
			break
		else:
			pass
	return package



#  212.64.74.58  此id是腾讯云临时加入的

panduan=True
while panduan:
	switch1=True
	while switch1:
		num=input("CHOOSE NUM:")
		if int(num) in [1,2,3,4,5,6,7,8,9,10,11,12]:
			switch1=False
		else:
			print("输入有误请重新输入")
	package_name=get_packagename(num)  # 不输入包名直接拿上一个返回值
	'''判断包是否在池子里，若在的话返回key值 菜的一批
	可以用反射的方法mmp
	'''
	value_list=[]
	services_ip=""
	def get_ip():
		global services_ip
		for key,value in packagelist.items():
			for item in value:
				if item==package_name:
					services_ip=key
			value_list.append(value)
		return services_ip
		
	ip=get_ip()
	# 查询 package 是否在value中
	def get_list(value_list):
		a,*b=value_list
		if len(b)==1:
			a.extend(b)
		else:
			a.extend(get_list(b))
		return a
		
	*total,tail=get_list(value_list)
	total.extend(tail)

	if package_name not in total:
		print("=====不存在,检查是否输错或加对应包的名字到ip池子中 ip:['package_name']=====")
	else:
		ip=get_ip()
		panduan=False
		
print("开始认证".center(20,"="))
ssh = paramiko.SSHClient()#创建SSH对象
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())#允许连接不在know_hosts文件中的主机
ssh.connect(hostname=ip, port=22, username='root', password='Yunjiidc2018')#连接服务器
print("认证成功".center(20,"="))

EOF=True
while EOF:
	action=input("命令: ")
	stdin, stdout, stderr = ssh.exec_command(action)   #执行命令并获取命令结果
	# stdin为输入的命令
	# stdout为命令返回的结果
	# stderr为命令错误时返回的结果
	res,err = stdout.read(),stderr.read()
	result = res if res else err
	print(result.decode('utf-8', 'ignore'))
	if action=="quit" or action=="q":
		EOF=False
ssh.close()#关闭连接