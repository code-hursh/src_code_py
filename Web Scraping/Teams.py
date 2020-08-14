from myselenium import Chrome,random_wait
from team_creds import password,name_verify

class Teams(Chrome):
    def __init__(self,_uid):
        Chrome.__init__(self)
        self.login_link = r"https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=abf2f370-e523-41da-ae73-b75d77bf98d2&&client-request-id=e64de797-18b6-4d7e-8823-c241b4fb3dca&x-client-SKU=Js&x-client-Ver=1.0.9&nonce=14b0d61d-d96e-41a8-a1bb-51cb17807d01&domain_hint="
        random_wait()
        self.driver.get(self.login_link)
        self.login(_uid,r'//*[@id="i0116"]',password[_uid],r"//input[@type='password']",temp = False,temp_path = r'//*[@id="idBtn_Back"]')
        random_wait()
        self.fxpath('//a[@class = "use-app-lnk"] ').click()
        self.Menus = []
        random_wait()
        # you are logged in :)
    def init_menus(self):
        random_wait()
        self.Menus = self.fxpaths(r'//button[@class = "app-bar-link app-bar-button  app-bar-selected" or @class = "app-bar-link app-bar-button "]')

    def activity_init(self):
        if not self.Menus:

            self.init_menus()
        self.Activity = self.Menus[0]

    def chat_init(self):
        if not self.Menus:

            self.init_menus()
        self.Chat = self.Menus[1]

    def teams_init(self):
        if not self.Menus:

            self.init_menus()
        self.Teams = self.Menus[2]

    def calender_init(self):
        if not self.Menus:

            self.init_menus()
        self.Calender = self.Menus[4]

    def gotoTeam(self,name):
        self.teams_init()
        self.Teams.click()
        self.Teams.click()
        team_cards = self.fxpaths(r"//div[@class='team-card']")
        team_names = self.fxpaths(r"//h1[@class ='team-name-text' or @class = 'team-name-text team-name-unread']")
        self.team_names = [i.text for i in team_names]
        select = 0
        try:
            for i in self.team_names:
                if name_verify[name.casefold()] in i:
                    break
                else:
                    select += 1
            team_cards[select].click()
        except:
            print('team not found')

    def gotofiles(self):
        drop_down = self.fxpath(r'//*[@id="settingsDropdown"]')
        drop_down.click()
        file = self.fxpath(r'//*[@id="files"]/div/a/span/span')
        file.click()
        random_wait(8)


    def returnfolders(self):
        folders = self.fxpaths(r"//button[@data-automationid = 'FieldRenderer-name']")
        return folders

    def enterdir(self,name):
        folders = []
        while True:
            try:
                r = 0
                folders = self.returnfolders()
                for folder in folders:
                        print('iterating')
                        if name in folder.text.casefold():
                            break
                        else:
                            r += 1
                folders[r].click()
                break
            except:
                folders = []
                continue

    def download(self,index):
        button = self.fxpath(r'//button[@title="Show actions"]')
        random_wait(3)
        download_button = self.fxpaths(r'//button[@name="Download"]')[-1]
        download_button.click()

if __name__ == '__main__':
    a = Teams('xii012@ssshss.edu.in')
    a.gotoTeam('en')
    a.gotofiles()
    a.enterdir('audio class')

# the downloading method is made, now you will have to make a system to locate the file and the difference of the files in your present desktop and the main website

# learn how to simultaneously run two files together at a time
