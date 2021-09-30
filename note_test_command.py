from selenium import webdriver
from selenium.webdriver import ActionChains
import  tests

chrdriver = webdriver.Chrome()
chrdriver.implicitly_wait(30)
chrdriver.maximize_window()

chrdriver.get("https://telecardiologia.cardiocalm.com/testing/")

from_element =chrdriver.find_element_by_xpath("//select[@id='tipi_esame']/option[text()='ECG']")
to_element= chrdriver.find_element_by_xpath("//select[@id='tipi_esame']/option[text()='PDF']")
action = ActionChains(chrdriver)
click = ActionChains(chrdriver)
action.click_and_hold(from_element).move_to_element(to_element).perform()
chrdriver.find_element_by_id("username").click()
