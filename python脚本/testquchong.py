def get_datalist(filename):
	with open(filename,"r") as f:
		data=[]
		for line in f:
			data.append(line.strip())
	return data


data=get_datalist(r"C:\Users\17249\Desktop\data.txt")
a = {}
for i in data:
	a[i] = data.count(i)

for key,value in a.items():
		if value!=1:
			print(key,"====>",value)