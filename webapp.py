from flask import Flask
from remote import Remote 
from flask import render_template


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

@app.route('/')
def main_interface():
	return render_template("main_interface.html")

@app.route('/run/<cmd>')
def exec_command(cmd):
	pioneer = Remote(app.config["PIONEER"])
	pioneer.send_cmd(cmd)
	return "Ran {} on {}".format(cmd, app.config["PIONEER"])

if __name__ == '__main__' :
	app.run()