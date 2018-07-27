# -*- coding:utf-8 -*-

from sys import argv
import requests

EXAMPLE="""
    Eg:python test_argv.py http://www.baidu.com
"""


if len(argv) !=2:
    print EXAMPLE
    exit()
    
script_name,url=argv
if url[0:4] !="http":
    url=r"http://"+url

r=requests.get(url)

print u"接口地址:"+url
print u"状态码:"+str(r.status_code)
print "headers:"
for key,value in r.headers.items():
    print key,value

