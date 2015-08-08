import telnetlib


class Remote:
	def __init__ (self, IP):
		self.ip = IP

	def send_cmd(self, cmd):
		try:
			#Assume UTF-8 data, could be dedection based	
			udata=cmd.decode("utf-8")
			asciidata=udata.encode("ascii","ignore")

			tn = telnetlib.Telnet(self.ip, 24)

			r = tn.read_until("$ ", 0.1)

			#assert "$ " in r, "Timeout waiting for prompt!"

			tn.write(asciidata + "\r\n")

			tn.close()
			return True
		except:
			return False

	def connect_to_celery_queue(self, params):
		return True
