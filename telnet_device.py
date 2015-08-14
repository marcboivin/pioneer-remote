import telnetlib
import json
import redis
import threading

class TelnetDevice(threading.Thread):

	def __init__ (self, IP, device_json_path, model_name):
		threading.Thread.__init__(self)
		self.json_path = device_json_path
		self.ip = IP
		self.commands = False
		self.model_name = model_name
		self.get_allowed_commands()

		# Starting the pubsub queue
		print "{} starting redis queue".format(self.model_name)
		self.redis = redis.Redis()
		self.pubsub = self.redis.pubsub()
		self.pubsub.subscribe([self.model_name])

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

	# Pass the redis item form a queue, must be from the model_name queue
	# The function will do the work only if the requiresments are met
	def from_redis_queue(self, item):
		if item["type"] == "message" and item["channel"] == self.model_name:
			self.send_cmd(item['data'])

	def run(self):
		print "{} recieved command".format(self.model_name)
		for item in self.pubsub.listen():
			if item['data'] == "KILL":
				self.pubsub.unsubscribe()
				print self, "unsubscribed and finished"
				break
			else:
				self.from_redis_queue(item)

	def get_allowed_commands(self):
		json_data=open(self.json_path).read()
		data = json.loads(json_data)
		# Search in the JSON file for the model name
		try:
			self.commands = data[self.model_name]["commands"]
		except :
			print "Device {} not found in the device file".format(self.model_name)

