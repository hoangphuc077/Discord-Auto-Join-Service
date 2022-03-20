import string
import sys
import random
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from random_username.generate import generate_username
from fake_useragent import UserAgent
import re, csv
from random import uniform, randint

def password_gen(length=8, chars= string.ascii_letters + string.digits + string.punctuation):
        return ''.join(random.choice(chars) for _ in range(length))  
    
def gather_proxy():
    proxies = []
    with open('config/proxies.txt', 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        for line in lines:
            proxies.append(line.replace('\n', ''))
    return proxies
def main(): 
    proxies = gather_proxy()
    if proxies:
        proxy = random.choice(proxies)
    usernames = generate_username(1)
    print(usernames[0])
    username = usernames[0]
    password = password_gen()
    email = username + "@kryptobirdie.com"
    print(email)


    options = webdriver.ChromeOptions()
    if proxies:
        if proxy:
            print(proxy)
            options.add_argument('--proxy-server=%s' % proxy)
    # options.add_argument('--incognito')

    # driver = webdriver.Chrome(ChromeDriverManager().install())
    s=Service(ChromeDriverManager(version='99.0.4844.51').install())
    # s=Service(executable_path=r"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
    driver = webdriver.Chrome(options=options, service=s)
    driver.get('https://discord.com')
    time.sleep(2)
    
    driver.find_element(by=By.XPATH, value="//button[text()='Open Discord in your browser']").click()
    time.sleep(.5)
   
    # driver.find_element(by=By.ID, value="button-ZGMevK buttonDark-3a8taR buttonLarge-3z9xOS gtm-click-class-open-button marginTop24-3ZXBpg").click()
    driver.find_element(by=By.XPATH, value="//input[@type='text']").send_keys(username)

    actions = ActionChains(driver)
    time.sleep(.5)
    # Locating to the first date input then the discord will navigate the focuse to the next input
    # driver.find_elements_by_class_name('css-1hwfws3')[0].click() 
    actions.send_keys(Keys.ENTER)
    actions.perform() # All the actions are pending and needs to perform all at once 

    checker = input(" Submit your form manually. Have you put the date? [y/n] > ") # Fixed typo

    if checker == "y":
        token = driver.execute_script("let popup; popup = window.open('', '', `width=1,height=1`); if(!popup || !popup.document || !popup.document.write) console.log('Please allow popups'); window.dispatchEvent(new Event('beforeunload')); token = popup.localStorage.token.slice(1, -1); popup.close(); return token")
    elif checker =="n":
        sys.exit()

    with open('output/login.txt', 'a', encoding='UTF-8') as login_file:
        login_file.write(username + ':   ' + email + ':   ' + password + ':   ' + token + '\n')
    

    driver.get('https://discord.gg/rzynTzBE')
    input("ready to quit [y/n] > ") # Fixed typo
main()

# # get captcha key
# site_key = 'f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34'
# url = "https://discordapp.com/register"
# API_KEY = "CAPMONSTER API KEY"
# s = requests.Session()
# data_post = {
#     "clientKey": API_KEY,
#     "task":
#         {
#             "type": "HCaptchaTaskProxyless",
#             "websiteURL": url,
#             "websiteKey": site_key
#         }
# }
# captcha_id = s.post("https://api.capmonster.cloud/createTask", json=data_post).json()
# data_get = {
#     "clientKey": API_KEY,
#     "taskId": captcha_id['taskId']
# }
# captcha_answer = s.get("https://api.capmonster.cloud/getTaskResult", json=data_get).json()
# while captcha_answer['status'] == "processing":
#     time.sleep(5)
#     captcha_answer = s.get("https://api.capmonster.cloud/getTaskResult", json=data_get).json()
# captcha_token = captcha_answer["solution"]["gRecaptchaResponse"]
# driver.execute_script(f'document.getElementsByName("g-recaptcha-response")[0].innerText="{captcha_token}";') # put captcha token into g-recaptcha-response textarea
# driver.execute_script(f'document.getElementsByName("h-captcha-response")[0].innerText="{captcha_token}";')

# # code to submit captcha token