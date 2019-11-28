import json
with open('./serverMessage.json','r') as f:
	data = json.load(f)
	print(data)
