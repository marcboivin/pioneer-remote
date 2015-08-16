class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'default-secret'
    


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    # Where is the file containning all the devices and their commands
    DEVICE_FILE = "./static/js/devices.json" 

class TestingConfig(Config):
    TESTING = True