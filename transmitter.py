import serial, json

# port might be different
ser = serial.Serial('/dev/pts/6')

products = json.dumps([{
	'code': '0001',
	'desc': 'ASUS Zenbook'
}, {
	'code': '0080',
	'desc': 'GTX 1080 Ti'
}, {
	'code': '4880',
	'desc': 'i9-7800K'
}])

package = f'{products}\n'

ser.write(package.encode())