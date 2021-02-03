import os, json
from dotenv import load_dotenv


class Config:
    __instance__ = None


    def __init__(self):
        """ Constructor."""
        if Config.__instance__ is None:
            load_dotenv()
            self.SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
            self.SECRET_KEY = os.environ.get('SECRET_KEY')
            Config.__instance__ = self
            
        else:
            raise Exception("You cannot create another Config class")

    @staticmethod
    def get_instance():
        """ Static method to fetch the current instance."""
        if not Config.__instance__:
            Config()
        return Config.__instance__
    