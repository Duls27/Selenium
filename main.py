from selenium import webdriver
import json
import  new_structure, os, call_to_test

desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

################################### INFORMAZIONI IMPORTANTI ########################################
#link_piattaforma_da_testare
link_piattaforma="https://telecardiologia.cardiocalm.com/testing/"

#mail_ricezione_nuova_struttura_ed_utenti
mail_ricezione_test = "selenium.test.cc@gmail.com"
password_mail= "SeleniumTest123456"

#path_ai_fil_per_esami
path_diario = desktop_path + '\Diario.pdf'
path_esame = desktop_path + '\SeleniumTestCarica.pdf'
path_schreenshots=desktop_path + '\selenium_screenshots'

#nomi_nuova_struttura
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

########################## Per crare struttura completa togliere commento #########################################
'''
usernames, psw = new_structure.complete_structure(link_piattaforma,driver, mail_ricezione_test, password_mail,
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
#################################### Test Basic invio, ricezione, apertura ############################################

#os.mkdir(desktop_path + '\selenium_screenshots')

usernames=[new_operatore,new_cardiologo]
pwd="cardiocalm123456"

#pc,pcPDF=call_to_test.basic_tests_operatore(link_piattaforma,driver, usernames[0], pwd, path_diario, path_esame, path_schreenshots)
pc="CnTYygtV"
pcPDF="N7msclwc"
call_to_test.basic_tests_refertatore(link_piattaforma,driver,new_cardiologo,pwd,path_diario,path_schreenshots, pc)
driver.close()

