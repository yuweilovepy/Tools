'''
迭代器
生成器
装饰器
上下文管理器
'''

class Foo(object):
	
	
	def __init__(self,name,status=1):
		self.name=name
		self.status=status
	
	@property
	def caiyi(self):
		print("{}-like-{}".format(self.name,self.status))
		
	
	@caiyi.setter
	def caiyi(self,status):
		pass
		

if __name__=="__main__":
	Foo("xiaolan").caiyi()

		