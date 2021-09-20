from selenium import webdriver
import ClinicaVicina

# Opening Web Browser
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

ClinicaVicina.Staging(driver)


#driver.close()