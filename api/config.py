#!/usr/bin/env python3
class BaseConfig:
    FLASK_APP = 'api'
    DEBUG = False
    TESTING = False


class LocalConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEVELOPMENT = True
    DEBUG = True


class TestConfig(BaseConfig):
    FLASK_ENV = 'development'
    TESTING = True


class DevelopmentConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEVELOPMENT = True
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEVELOPMENT = False
    FLASK_ENV = 'production'
