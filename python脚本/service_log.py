import paramiko
import select
import re
import warnings
warnings.filterwarnings("ignore")

# 实施打印日志
#放到配置文件中

aly_ip_package={"116.62.166.8":['yunjixinyun','yunjixinyunadmin','xinyunmonitorservice','xinyunservice-assembly','imserver-assembly'], \
"116.62.234.15":['popxinyunservice-assembly','popxinyunadmin','workorderservice-assembly'],'47.96.158.187':['xinyunmonitorservice-assembly'],\
"116.62.196.200":["immessagedao-assembly",'xinyuncanalconsumer-assembly'],'47.110.76.84':['xinyunmq-assembly'],'47.97.218.111':["xinyunmonitoradmin"]}

txy_ip_package={"212.64.94.75":['yunjixinyun','yunjixinyunadmin','xinyunservice-assembly'], \
'212.64.52.21':['userother-assembly','xinyunmonitorservice-assembly','xinyunmonitorjob-assembly'], \
'212.64.65.170':['popxinyunservice-assembly','popxinyunadmin','workorderservice-assembly'], \
'212.64.74.58':['immessagedao-assembly','xinyuncanalconsumer-assembly'],
'172.81.214.211':["xinyunmq-assembly"]} #'xinyuncanalconsumer-assembly'  tar 包


####################################################################  xinyunservice-assembly   不用手动去布包###################### 测试自动部署
#  212.64.74.58  此id是腾讯云临时加入的


switch=False
while not switch:
	env=input("CHOOSE ENV:") 
	ENV=env.upper()
	if ENV=="ALY":
		packagelist=aly_ip_package
		switch=True
	elif ENV=="TXY":
		packagelist=txy_ip_package
		switch=True
	else:
		print("输入有误请重新输入")
		



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
[13]=======>xinyunmonitoradmin\n
""")

choosepack={1:"yunjixinyun",2:"yunjixinyunadmin",3:"xinyunmonitorservice",4:"xinyunservice-assembly",
5:"imserver-assembly",6:"popxinyunservice-assembly",7:"popxinyunadmin",8:"workorderservice-assembly",
9:"xinyunmonitorservice-assembly",10:"immessagedao-assembly",11:"xinyuncanalconsumer-assembly",
12:"xinyunmq-assembly",13:"xinyunmonitoradmin"
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


panduan=True
while panduan:
	switch1=True
	while switch1:
		num=input("CHOOSE NUM:")
		if int(num) in [1,2,3,4,5,6,7,8,9,10,11,12,13]:
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
		
		
	
tar=['xinyunmonitorservice','xinyunservice-assembly','popxinyunservice-assembly','xinyunmonitorservice-assembly','immessagedao-assembly',
	"immessagedao-assembly",'xinyuncanalconsumer-assembly','workorderservice-assembly',"xinyunmq-assembly",'imserver-assembly'
]

war=['yunjixinyunadmin','yunjixinyun','popxinyunadmin']

if package_name in tar:
	path=path="/usr/local/yunji/logs/%s/stdout.log" % package_name.split("-")[0]
elif package_name in war:
	path="/usr/local/yunji/tomcat/%s/logs/catalina.out" % package_name.split("-")[0]
else:
	print("not in packagelit,please add...")
	


def link_server_client(serverip,package_name):
    # 进行连接 print('------------开始连接服务器(%s)-----------' % serverip)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print('------------开始认证......-----------')
    client.connect(hostname=serverip, port=22, username='root', password='Yunjiidc2018')
    print('------------认证成功!.....-----------')  # 开启channel 管道
    transport = client.get_transport()
    channel = transport.open_session()
    channel.get_pty()  # 执行命令
    tail = 'tail -f -n 1000 %s' % path #将命令传入管道中,
    try:
        channel.exec_command(tail)
    except Exception as e:
        print(e)
    while True:  # 判断退出的准备状态
        if channel.exit_status_ready():
            break
        try:  # 通过socket进行读取日志，个人理解，linux相当于客户端，我本地相当于服务端请求获取数据（此处若有理解错误，望请指出。。谢谢）
            rl, wl, el = select.select([channel], [], [])
            if len(rl) > 0:
                recv = channel.recv(1024)  # 此处将获取的数据解码成gbk的存入本地日志
                print(recv.decode('utf-8', 'ignore'))
                # text_save(recv.decode('utf-8', 'ignore'), 'lgh.txt')  # 键盘终端异常
        except KeyboardInterrupt:
            print("Caught control-C")
            channel.send("\x03")  # 发送 ctrl+c channel.close()
            client.close()  # 文件存储
    client.close()

# def text_save(self, content, filename, mode='a+'):
#     # Try to save a list variable in txt file.
#     file = open(filename, mode)
#     for i in content:
#         file.write(i)
#         file.close

if __name__ == '__main__':
    # serverip=get_serverip()
    link_server_client(ip,package_name)