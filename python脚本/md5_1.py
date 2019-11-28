import hashlib
m2=hashlib.md5()
m2.update("ywb".encode("utf-8"))
print(m2.hexdigest())



# md5加密 