import telnetlib
import json


class TelnetDevice:
	def __init__ (self, IP, device_json_path, model_name):
		self.json_path = device_json_path
		self.ip = IP
		self.commands = False
		self.model_name = model_name
		self.get_allowed_commands()

	def send_cmd(self, cmd):
		try:
			# Valdation the action against the allow action list
			for action in self.commands:
				if action["action"]== cmd :

					# Converting to ASCII caus PIONEERR's telnet is from 1904
					udata=cmd.decode("utf-8")
					asciidata=udata.encode("ascii","ignore")

					tn = telnetlib.Telnet(self.ip, 24)

					r = tn.read_until("$ ", 0.1)


					tn.write(asciidata + "\r\n")

					tn.close()

					return True

			return False

		except:
			return False

	def get_allowed_commands(self):
		json_data=open(self.json_path).read()
		data = json.loads(json_data)
		# Search in the JSON file for the model name
		try:
			self.commands = data[self.model_name]["commands"]
		except :
			print "Device {} not found in the device file".format(self.model_name)

