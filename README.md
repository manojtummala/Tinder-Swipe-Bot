# Tinder-Swipe-Bot

**Tinder**.. this is the most wodely used site well known to every one...

Now, when you like to automate your Tinder Life  and don't want to be banned.. then there comes my **Tinder Auto Swipe bot**

# Getting Started

first of all for automation install selenium:
```bash
pip install selenium
```

Then you have to download chromdriver or any webdriver that you want to work on

And unzip it and keep it in you **python scripts**(where you have your python file installed) (preferable) [Windows]

If you are on (mac/linux) unzip and move to /usr/local/bin

create a secrets.py file with variables:
```bash
 username = 'your_username'
 password = 'your_password'
 ```
 
 The rest of the code in python script in self explanatory..
 
 The best thing to make it avoid all the possible popups is giving an try except condition.. in this way the bot won't have to stop for some unknown element error.
 ```bash
 try:
     popup = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
            popup.click()
 except Exception:
     pass
 ```
 
 To disable the notifications from chrome you can make use of chromeOptions()
 ```bash
 options = webdriver.ChromeOptions()
 options.add_argument("--start-maximized")
 options.add_argument("--disable-notifications");

 self.driver = webdriver.Chrome(chrome_options = options)
 ```
 
 And importatly add some randomness into the auto_swipe function to not get banned..
 
 And then just sit back get yourself a match with just a bot.
