from selenium import webdriver
import json
import  new_structure, os, call_to_test

desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

################################### INFORMAZIONI IMPORTANTI ########################################à
mail_ricezione_test = "selenium.test.cc@gmail.com"
password = "SeleniumTest123456"
path_diario = desktop_path + '\Diario.pdf'
path_esame = desktop_path + '\SeleniumTestCarica.pdf'
#os.mkdir(desktop_path + '\selenium_screenshots')
path_schreenshots=desktop_path + '\selenium_screenshots'

#nomi_struttura
new_admin="amministratore_test"
new_projectmanager="projectmanager_test"
new_cardiologo="cardiologo_test"
new_operatore="operatore_test"
new_struttura="struttura_test"
new_api="api_test"


###############################################################################################

# Opening Web Browser
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()


usernames, psw = new_structure.complete_structure(driver, mail_ricezione_test, password,
                                                  new_admin=new_admin,
                                                  new_projectmanager=new_projectmanager,
                                                  new_cardiologo=new_cardiologo,
                                                  new_operatore=new_operatore,
                                                  new_struttura=new_struttura,
                                                  new_api=new_api)

with open(desktop_path+"\CredenzialiTest.txt", 'w') as f:
    for key, value in usernames.items():
        f.write('%s:%s\n' % (key, value))
        f.write("psw_"+key+": "+ psw + "\n")



'''
usernames=["Opertest09","RefTest09"]
pwd="cardiocalm123456"

p1,p2=call_to_test.basic_tests_operatore(driver, usernames[0], pwd, path_diario, path_esame, path_schreenshots)
p1=["TestSelenium_CaricaE_PDF","TestSelenium_CaricaE_PDF"]
p2=["TestSelenium_CaricaE", "TestSelenium_CaricaE"]
#call_to_test.basic_tests_refertatore(driver,usernames[1],"pippo1234",path_diario,path_schreenshots,p1,p2)
'''
#driver.close()

