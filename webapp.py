from flask import Flask
from remote import Remote 
from flask import render_template
import ConfigParser
import redis
import threading


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

@app.route('/')
def main_interface():
	return render_template("main_interface.html")

@app.route('/run/<cmd>')
def exec_command(cmd):
	r = redis.Redis()
	r.publish('remote', cmd)

	return "Sent {} in the queue".format(cmd)

@app.route('/cmd/list')
def list_commands():
	return get_allowed_commands()

def get_allowed_commands():
	config = ConfigParser.ConfigParser()
	config.readfp(open('allowed_commands.yml'))
	print(config)

class Listener(threading.Thread):
	def __init__(self, r, channels):
	    threading.Thread.__init__(self)
	    self.redis = redis.Redis()
	    self.pubsub = self.redis.pubsub()
	    self.pubsub.subscribe(channels)
	    self.remote = Remote(app.config["PIONEER"])

	def work(self, item):
			if item["type"] == "message":
				print item['channel'], ":", item['data']
				self.remote.send_cmd(item['data'])

	def run(self):
	    for item in self.pubsub.listen():
	        if item['data'] == "KILL":
	            self.pubsub.unsubscribe()
	            print self, "unsubscribed and finished"
	            break
	        else:
	            self.work(item)

if __name__ == '__main__' :
	print("Starting Redis event loop")
	r = redis.Redis()
	client = Listener(r, ['remote'])
	client.start()
	
	app.run()