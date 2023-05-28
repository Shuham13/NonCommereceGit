import configparser

config = configparser.RawConfigParser()
config.read('C:\\Users\\shubham pate\\PycharmProjects\\NonCommerence 16 may 23\\NonCommerence\\Configuration\\config.ini')


class ReadConfig:

    @staticmethod
    def URL():
        url = config.get('common info', 'url')
        return url

    @staticmethod
    def Email():
        email = config.get('common info', 'email')
        return email

    @staticmethod
    def Password():
        password = config.get('common info', 'password')
        return password
