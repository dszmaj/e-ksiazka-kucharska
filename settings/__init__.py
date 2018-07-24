import environ

root = environ.Path(__file__) - 2
env = environ.Env(
    DEBUG=(bool, False),
)
environ.Env.read_env(root('.env'))

from .common import *
