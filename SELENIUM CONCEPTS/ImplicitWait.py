from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.wait import WebDriverWait

# url='https://www.geeksforgeeks.org'
# chrome_options = Options()
# chrome_options.add_experimental_option("detach",True)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
#                           options=chrome_options)
# driver.get(url)
# driver.maximize_window()

driver = webdriver.Chrome()
driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()
driver.implicitly_wait(5)
time.sleep(3)
ele=driver.find_element(By.XPATH,"//a[normalize-space()='Trending Now']")

print("element is ",ele)
driver.implicitly_wait(3)
ele.click()
driver.implicitly_wait(3)
actual_text=driver.find_element(By.XPATH,"//h1[@id='gfg-trending-heading-para1']").text
time.sleep(3)
expected_text='Trending Now On GeeksforGeeks'
try:
    if actual_text.__eq__(expected_text):
        print("Text Matched")
except Exception as err:
    print("Text not Matched",err)
