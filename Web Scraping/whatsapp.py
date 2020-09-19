from myselenium import Chrome,random_wait
from team_creds import password,name_verify

class Whatsapp(Chrome):
    def __init__(self):
        Chrome.__init__(self)
        self.login_link = "https://web.whatsapp.com/"
        self.driver.get(self.login_link)
        input("please scan the QR code and then press enter")

a = Whatsapp()
