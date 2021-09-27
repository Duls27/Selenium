from selenium import webdriver
import  new_structure, os

desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

################################### INFORMAZIONI IMPORTANTI ########################################à
mail_ricezione_test = "selenium.test.cc@gmail.com"
password = "SeleniumTest123456"
path_diario = desktop_path + '\Diario.pdf'
path_esame = desktop_path + '\SeleniumTestCarica.pdf'
path_schreenshots=os.mkdir(desktop_path + '\selenium_screenshots')

###############################################################################################

# Opening Web Browser
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

usernames, password = new_structure.complete_structure(driver, mail_ricezione_test, password)
usernames_file = open(desktop_path+"\CredenzialiTest.txt", "a")
usernames_file.write(usernames)
usernames_file.write("Same pwd for all: "+ password)
usernames_file.close()




driver.close()

