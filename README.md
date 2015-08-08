# Pioneer remote control

The goal of this projet is to provide a web based remote control for telnet
AV appliances. Right now, I'm supporting only the Pioneer SC-1228. But as I
gather, most pioneer work the same way.

## Status of this project

Right now it "works," but it's very crude. No UI yet, only buttons.

The vagrant machine does not yet work. Well it works just not in any usable 
way for this project.

## Setting up
Only dev settings are documented, but it should be enough to run behind your 
home router.

### Dependencies
* Python 2.7.x
* Python pip
* Redis on localhost

### How to 
 * Modify the DevelopmentConfig class of the config.py file (the PIONEER variable) to fit the IP of your amplifier
 * Start the redis erver (something like service start redis)
 * In the root folder of the app run :
		$ pip install -r dependencies.txt
 * Then run 
 		$ python webapp

 * Navigate to http://localhost:5000/ and voilà!

 ## Contributing

 If you'd like to help me, or just tell me how awful a python dev I am, please
 feel free to submit a pull request. When the first version is complete, I will 
 use git-flow, so please do.

 ### Styling
 I try to follow PEP8 as much as possible. My Python lint is set that way 
 anyways.



