from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class BaseConfig(object):
    CACHE_TYPE = os.getenv('CACHE_TYPE')
    CACHE_REDIS_HOST = os.getenv('CACHE_REDIS_HOST')
    CACHE_REDIS_PORT = os.getenv('CACHE_REDIS_PORT')
    CACHE_REDIS_DB = os.getenv('CACHE_REDIS_DB')
    CACHE_REDIS_URL = os.getenv('CACHE_REDIS_URL')
    CACHE_DEFAULT_TIMEOUT = os.getenv('CACHE_DEFAULT_TIMEOUT')

class Config(BaseConfig):
    # Additional configuration variables or overrides go here
    DEBUG = True  # Example: set DEBUG mode to True for development