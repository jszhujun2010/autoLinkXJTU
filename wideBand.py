import os
import requests

adsl_account = {"name": "",
                "username": "",
                "password": ""}


class ADSL:

    def __init__(self):
        self.name = adsl_account["name"]
        self.username = adsl_account["username"]
        self.password = adsl_account["password"]

    def connect(self):
        cmd = "rasdial %s %s %s" % (self.name, self.username, self.password)
        try:
            os.system(cmd)
        except:
            print "connection error..."

    def disconnect(self):
        cmd = "rasdial %s /disconnect" % self.name
        try:
            os.system(cmd)
        except:
            print "disconnection error..."

    def reconnect(self):
        self.disconnect()
        self.connect()


class Login:

    def __init__(self):
        self.username = adsl_account["username"]
        self.password = adsl_account["password"]
        self.url = "http://10.6.8.2:16805/srun_portal_pc.php"

    def login(self):
        agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
        headers = {'User-Agent': agent}
        postdata = {'action': 'login', 'ac_id': 1, 'username': self.username,
                    'password': self.password, 'save_me': 1, 'ajax': 1}
        session = requests.session()
        page = session.post(self.url, data=postdata, headers=headers)
        print page.text


def main():
    adsl = ADSL()
    adsl.connect()
    log = Login()
    log.login()
    print "You can access the Internet now..."

if __name__ == "__main__":
    main()
