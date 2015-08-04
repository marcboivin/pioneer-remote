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
    PIONEER = "192.168.56.223"
    KODI = ["192.168.56.225", "192.168.56.182"]

class TestingConfig(Config):
    TESTING = True