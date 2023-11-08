from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://demos.telerik.com/kendo-ui/treeview/dragdrop")
driver.maximize_window()
time.sleep(3)
src_ele=driver.find_element(By.XPATH,"//span[text()='Occasional Furniture']")
trgt_ele=driver.find_element(By.XPATH,"//span[text()='Kids Storage']")
act=ActionChains(driver)
act.drag_and_drop(src_ele,trgt_ele).perform()
time.sleep(5)
