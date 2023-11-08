from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://demos.telerik.com/kendo-ui/treeview/animation")
driver.maximize_window()
time.sleep(3)
