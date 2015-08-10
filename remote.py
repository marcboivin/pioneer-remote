import telnetlib
import json


class Remote:
	def __init__ (self, IP, commands_json):
		self.json_commands = commands_json
		self.ip = IP
		self.commands = False
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

					#assert "$ " in r, "Timeout waiting for prompt!"

					tn.write(asciidata + "\r\n")

					tn.close()

					return True

			return False

		except:
			return False

	def get_allowed_commands(self):
		json_data=open(self.json_commands).read()
		data = json.loads(json_data)
		# Hardcoded value, should be passed as parmeter.
		# Will be the next feture
		self.commands = data["PIONEERSC1228"]["commands"]

