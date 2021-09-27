import time
from selenium import webdriver
import email_managment
import  new_users, tests

password = "cardiocalm123456"
password1 = "pippo1234"

def complete_structure(chrdriver: webdriver.Chrome, mail, mailpassword):
    chrdriver.get("https://telecardiologia.cardiocalm.com/clinicavicinaweb-testing/")

    ################################# NEW ADMINISTRATOR ###########################################################
    
    #delete emails from gmail
    email_managment.delete_all_emails(mail, mailpassword)
    # Creazione nuovo utente
    admin_usr = new_users.administrator(chrdriver, password, password1, "Admintest")
    time.sleep(3.0)
    #read one time password mail
    admin_psw = email_managment.read_password_from_emails(mail, mailpassword)
    #enter reset password
    chrdriver=tests.enter_password_double_check(chrdriver,admin_usr,admin_psw,admin_psw,"https://telecardiologia.cardiocalm.com/clinicavicinaweb-testing/index/cambio-Password")
    #newpassword
    search_field = chrdriver.find_element_by_id("nuova_password")
    search_field.clear()
    search_field.send_keys(password)

    search_field = chrdriver.find_element_by_id("ridigita_nuova_password")
    search_field.clear()
    search_field.send_keys(password)
    chrdriver.find_element_by_id("cambio_password").click()
    chrdriver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li[2]/form/button").click()
    ################################################# PROJECT MANAGER  ###############################################
    
    email_managment.delete_all_emails(mail, mailpassword)
    pm_usr=new_users.project_manager(chrdriver, admin_usr, password, password1)
    time.sleep(3.0)
    pm_tmp_psw=email_managment.read_password_from_emails(mail, mailpassword)

    search_field = chrdriver.find_element_by_id("username")
    search_field.send_keys(pm_usr)
    search_field = chrdriver.find_element_by_id("password")
    search_field.send_keys(pm_tmp_psw)
    # newpassword
    search_field = chrdriver.find_element_by_id("nuova_password")
    search_field.clear()
    search_field.send_keys(password)

    search_field = chrdriver.find_element_by_id("ridigita_nuova_password")
    search_field.clear()
    search_field.send_keys(password)
    chrdriver.find_element_by_id("cambio_password").click()
    chrdriver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li[2]/form/button").click() #logout

  ###################################### REFERTATORE #################################################################

    email_managment.delete_all_emails(mail, mailpassword)
    ref_usr = new_users.refertatore(chrdriver, admin_usr, password, password1)
    time.sleep(5)
    ref_tmp_pasw = email_managment.read_password_from_emails(mail, mailpassword)

    search_field = chrdriver.find_element_by_id("username")
    search_field.send_keys(ref_usr)
    search_field = chrdriver.find_element_by_id("password")
    search_field.send_keys(ref_tmp_pasw)
    # newpassword
    search_field = chrdriver.find_element_by_id("nuova_password")
    search_field.clear()
    search_field.send_keys(password)

    search_field = chrdriver.find_element_by_id("ridigita_nuova_password")
    search_field.clear()
    search_field.send_keys(password)
    chrdriver.find_element_by_id("cambio_password").click()
    chrdriver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li[2]/form/button").click()  # logout
############################################ NEW STRUCTURE ######################################################

    username_old_admin = "Amministratore"
    oper_usr,rs_nome,rs_cognome = new_users.struttura(chrdriver, username_old_admin, password, password1)

####################################### ADMIN SOLO API ###########################################

    # delete emails from gmail
    email_managment.delete_all_emails(mail, mailpassword)
    # Creazione nuovo utente
    api_usr = new_users.administrator(chrdriver, password, password1, "Apitest")
    time.sleep(3.0)
    # read one time password mail
    api_psw = email_managment.read_password_from_emails(mail, mailpassword)
    # enter reset password
    chrdriver = tests.enter_password_double_check(chrdriver, api_usr, api_psw, api_psw,
                    "https://telecardiologia.cardiocalm.com/clinicavicinaweb-testing/index/cambio-Password")
    # newpassword
    search_field = chrdriver.find_element_by_id("nuova_password")
    search_field.clear()
    search_field.send_keys(password)

    search_field = chrdriver.find_element_by_id("ridigita_nuova_password")
    search_field.clear()
    search_field.send_keys(password)
    chrdriver.find_element_by_id("cambio_password").click()
    chrdriver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li[2]/form/button").click() #return home

    return {"admin": admin_usr, "pm": pm_usr, "refertatore":ref_usr, "admin_api":api_usr, "oper":oper_usr}, password














