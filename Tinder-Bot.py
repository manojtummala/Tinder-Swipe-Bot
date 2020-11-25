from selenium import webdriver
from time import sleep
from secrets import username, password
from selenium.webdriver.chrome.options import Options

class TinderBot():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications");

        self.driver = webdriver.Chrome(chrome_options = options)
        # self.driver = webdriver.Chrome()

    def site(self):
        self.driver.get('https://tinder.com')

    def login(self):
        sleep(4)
        login_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button') 
        login_btn.click()

        sleep(3)

        google_btn = bot.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div/div/button') 
        google_btn.click()

        sleep(4)

        base_window = self.driver.window_handles[0]
        sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[1]) 

        sleep(1)
        
        email_input = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        email_input.send_keys(username) 
        next_btn1 = self.driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
        next_btn1.click()

        sleep(1)

        pass_input = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        pass_input.send_keys(password) 
        next_btn = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button')
        next_btn.click()

        sleep(2)

        self.driver.switch_to.window(base_window)

        sleep(4)

        try:
            popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            popup_1.click()
        except Exception:
            try:
                for i in range (5):
                    popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
                    popup_1.click()
            except Exception:
                pass

        try:
            popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            popup_2.click()
        except Exception:
            pass
        
        
        

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button')
        dislike_btn.click()
        
    def auto_swipe(self):
        from random import random
        while(True):
            sleep(0.5)
            try:
                rand = random()
                if rand < .73:
                    self.like()
                else:
                    self.dislike()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()
    def close_popup(self):
        sleep(0)
        try:
            popup = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
            popup.click()
        except Exception:
            pass
        try:
            popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div[3]/button[2]')
            popup_3.click()
        except Exception:
            pass
        try:
            popup_4 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[2]')
            popup_4.click()
        except Exception:
            pass
        try:
            popup_5 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
            popup_5.click()
        except Exception:
            pass
        try:
            popup_6 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[2]')
            popup_6.click()
        except Exception:
            pass
        
        

    def close_match(self):
        try:
            match = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[4]/button')
            match.click()
        except Exception:
            pass
        
        






bot = TinderBot()
bot.site()
bot.login()
bot.auto_swipe()



        





