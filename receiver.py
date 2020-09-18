import serial, json

# port might be different
ser = serial.Serial('/dev/pts/7')

response = ser.readline().decode()

print(response)

jsonData = json.loads(response)

def getDescProp (obj):
	return obj['desc']

products = map(getDescProp, jsonData)

print(f'Products:\n{list(products)}\n')