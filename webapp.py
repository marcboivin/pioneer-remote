from flask import Flask
from telnet_device import TelnetDevice 
from flask import render_template
import redis
import json


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

@app.route('/')
def main_interface():
	return render_template("main_interface.html")

@app.route('/run/<device>/<cmd>')
def exec_command(cmd):
	r = redis.Redis()
	r.publish('remote', cmd)

	return "Sent {} in the queue".format(cmd)


if __name__ == '__main__' :
	print "Loagind JSON data"
	json_data=open(app.config["DEVICE_FILE"]).read()
	data = json.loads(json_data)
	devices = []

	for device in data:
		print device
		new_device = False

		device_type = data[device]["type"]
		if device_type=="telnet":
			new_device = TelnetDevice(data[device]["IP"],app.config["DEVICE_FILE"], device)

		if new_device:
			devices.extend(new_device)
		else:
			print "Device {} not supported".format(device)

	app.run()