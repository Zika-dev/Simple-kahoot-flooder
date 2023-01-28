from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import os
from time import sleep

chrome_options = Options() 
#chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('log-level=3')
PATH = '/driver/chromedriver.exe'
driver = webdriver.Chrome(PATH, options=chrome_options)
name = 'Mike Hawk'
os.system('cls')
pin = input('Enter game pin: ')
amount = input('Enter amount of bots: ')

for i in range(1,int(amount)+1):
    if(i%int(amount)+1==0):
        break
    pageLoaded = False
    failed = 0
    print(f'Bot number {i}')
    driver.switch_to.new_window('https://kahoot.it/')
    driver.get("https://kahoot.it/")
    print('Entering website...')
    search = driver.find_element(By.ID, 'game-input')
    print('Entering pin...')
    search.send_keys(pin)
    search.send_keys(Keys.RETURN)
    print('Entering nickname...')
    while pageLoaded == False:
        try:
            search = WebDriverWait(driver, 0.1).until(EC.presence_of_element_located((By.ID, 'nickname')))
        except TimeoutException:
            if failed >= 15:
                print('Timeout')
                quit()
            failed=failed+1
            print('Waiting for page to load...')
        else:
            pageLoaded = True
    search = driver.find_element(By.ID, 'nickname')
    search.send_keys(name)
    search.send_keys(Keys.RETURN)
    print('Bot joined successfully')
else:
    os.system('cls')
    print("Done!")
    os.system('pause')