import configparser

config = configparser.RawConfigParser()
config.read("../Configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getAppUrl():
        url = config.get("common login info", "url")
        return url

    @staticmethod
    def getEmail():
        email = config.get("common login info", "email")
        return email

    @staticmethod
    def getPassword():
        password = config.get("common login info", "password")
        return password