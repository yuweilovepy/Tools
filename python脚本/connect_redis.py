import redis

#有毛用
class ConnectRedis(object):

	
	def __init__(self,host,port):
		self.host=host
		self.port=port
	
	
	def connect_redis(self):
		try:
			pool = redis.ConnectionPool(host=self.host, port=self.port)  
			r = redis.Redis(connection_pool=pool)
			#pipe = r.pipeline(transaction=False)
		except Exception as e:
			print(e)
		return r
		
		

class ActionRedis(ConnectRedis):
	
	def __init__(self,host,port,args):
		super().__init__(host,port)
		self.args=args
		
	
	# 获取name对应的hash中键值对的个数
	def hlen_key(self):
		return super().connect_redis().hlen(self.args)
		
		
	# 删除name 对应的hash中对应的个数
	def del_key(self):
		return super().connect_redis().Del(self.args)
		
		
	# 获取所有的哈希
	def getall_key(self):
		return super().connect_redis().hgetall(self.args)
		
		
		
 # 阿里云redis host='172.30.255.189', port=14159
 # 腾讯云redis host=172.16.0.9:14159

env={"aly":["172.30.255.189",14161],"txy":["172.16.0.9",6380]}

CHOOSEENV=input("CHOOSE_ENV:")

for i,v in env.items():
	if i==CHOOSEENV.lower():
		host,port=v

a=ActionRedis(host,port,"hgetall ALL_IN_SERVICE")

print(a.getall_key())
#查询用户信息         hgetall USER_INFO_${consumerId}  13012880
#查询用户的绑定关系   hgetall IN_LINK_${consumerId}
#查询客服信息         hget SERVICE_INFO ${empId}
#查询在线全部客服列表 hgetall ALL_IN_SERVICE
#查询客服正在服务的会话列表  hgetall IN_SERVICE_${empId}
#查询客服的历史记录       hgetall QUEUE_HISTORY${empId}
#查看忙碌状态客服列表  hgetall IN_BUSY
#查询兜底排队         hgetall QUEUE_BOTTOM
#正常队列排队信息     hgetall QUEUE_UP_${queueId}    # queueId  队列id

# 用户信息  hgetall USER_INFO_$(consid)
#查询技能组 GROUP_XX   XX-技能组id

#ZRANGE USER_QUEUE_UP_INFO_13012880 0 -1  查看用户排队时间   通过用户id 查询



#ZRANGE POP_USER_QUEUE_UP_INFO_ST36202213015569 0 -1 WITHSCORES



# ZRANGE CUSTOMER_SERVICE_WORK_ORDER_ZSET_83 0 -1 WITHSCORES  # 工单查服务量的





# print(type(a.getall_key()))

for key,value in a.getall_key().items():
	print(key.decode("utf-8"),"===>",value.decode("utf-8"))
	


	
	





