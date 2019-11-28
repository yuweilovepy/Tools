from pprint import pprint
# *args **kwargs 
def test_arges(**kwargs): 
	for key,value in kwargs.items():
		print("{0}=={1}".format(key,value))

# test_arges(name="value")


# 传参
def chuan_args(arg1,arg2,arg3):
	print("arg1:" ,arg1)
	print("arg2:" ,arg2)
	print("arg3:" ,arg3)


args=("name","args","sex")
chuan_args(*args)
print("")
kwargs={"arg1":"name","arg2":"age","arg3":"sex"}
chuan_args(**kwargs)

print("FENGE".center(30,"#"))

#  生成器 generator  爬虫会用到

def test_generator(n):
	a=b=1
	for i in range(n):
		yield a
		a,b=b,a+b


for i  in test_generator(30):
	print(i)


# MAP  lambda python3 map 返回迭代器

list1=[1,2,3,4] 

list2=(map(lambda x:x*x ,list1))
print(list((list2)))

# 装饰器
from functools import wraps
def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated

@decorator_name
def func():
    return("Function is running")

can_run = True
print(func())
# Output: Function is running

can_run = False
print(func())
# Output: Function will not run