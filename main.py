from selenium import webdriver
import  new_structure, email_managment


mail_ricezione_test = "selenium.test.cc@gmail.com"
password = "SeleniumTest123456"

# Opening Web Browser
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

admin_usr=new_structure.complete_structure(driver, mail_ricezione_test, password)


#driver.close()