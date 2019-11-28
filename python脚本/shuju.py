import requests


# url="https://txst.yunjiglobal.com/popadmin/admin/user/login"
# headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
# }
# data={"account":"ceshilangh","password":"dNjm+yHvIzkpb95AkyF7zw=="}




base_url=r"https://txst.yunjiglobal.com/outssoadmin/user/add"



	
headers={'cookie':'cuid=401f63dc-31bf-45d7-9f1d-7e73880f5f34; \
	userId=%E5%85%B0%E5%85%89%E8%BE%89; \
	LATELY_SHOPID=6325475; ecology_p=VEdkb01EQTFNa0I1ZFc1cWFRPT0=; \
	username=testWB0052; ticket=sso.c398f712-60f5-420e-9850-4a17500b79d4;\
	ThinkingDataJSSDK_cross=%7B%22distinct_id%22%3A%2216ae259d8783e7-00f5f2ded38b6d-3d644601-2073600-16ae259d8796e8%22%2C%22device_id%22%3A%2216b110c31dd981-06c79d09e43917-3d644601-2073600-16b110c31de625%22%2C%22account_id%22%3A%22%22%7D; \
	CURRENT_URL=http%3A//t.yunjiglobal.com/yjbuyer/detail%3FitemId%3D1000635%26shopId%3D6325475%26spikeActivityId%3D0; JESSIONID="outUser:eb2fd8ec-d4c7-4dff-a2d5-8a0817e60efa"',
 }
	
data={"loginAccount":"login123" ,
	"name":"loginname123",
	"phone":"13387212527",
	"email":"123@qq.com",
	"password":"123456",
	"repeatPassword":"123456",
	"roleIdList":[224]
	}
	
# for i in range(3,40):
	# data={"loginAccount":"khkjh12%d" % i,
	# "name":"sdsds%d" % i,
	# "phone":"13387212527",
	# "email":"123@qq.com",
	# "password":"123456",
	# "repeatPassword":"123456",
	# "roleIdList":[224]}
	
	# try:
	
conn=requests.session()
r=conn.post(base_url,data=data,headers=headers)
print(r.status_code)
print(r.url)


		# print("add 成功")
		
	# except Exception as e:
		# print("失败")
