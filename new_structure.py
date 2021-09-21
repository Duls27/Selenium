import time

from selenium import webdriver
import email_managment
import  new_users, tests

password = "cardiocalm123456"
password1 = "pippo1234"

def complete_structure(chrdriver: webdriver.Chrome, mail, mailpassword):
    chrdriver.get("https://telecardiologia.cardiocalm.com/clinicavicinaweb-staging/")

    '''
    #delete emails from gmail
    email_managment.delete_all_emails(mail, mailpassword)
    # Creazione nuovo utente
    admin_usr=new_users.administrator(chrdriver, password, password1)
    #read one time password mail
    admin_psw=email_managment.read_password_from_emails(mail, mailpassword)
    #enter reset password
    chrdriver_admin=tests.enter_password_double_check(chrdriver,admin_usr,admin_psw,admin_psw,"https://telecardiologia.cardiocalm.com/clinicavicinaweb-staging/index/cambio-Password")

    #newpassword
    search_field = chrdriver_admin.find_element_by_id("nuova_password")
    search_field.clear()
    search_field.send_keys(password)

    search_field = chrdriver_admin.find_element_by_id("ridigita_nuova_password")
    search_field.clear()
    search_field.send_keys(password)
    chrdriver_admin.find_element_by_id("cambio_password").click()
    '''
    #Project Manager
    #da rimuovere una volta ultimato
    admin_usr="AmministratoreTest"
    ###########################
    #email_managment.delete_all_emails(mail, mailpassword)
    pm_usr=new_users.project_manager(chrdriver, admin_usr, password, password1)
    time.sleep(5)
    pm_tmp_pasw=email_managment.read_password_from_emails(mail, mailpassword)

    search_field = chrdriver.find_element_by_id("username")
    search_field.send_keys(pm_usr)
    search_field = chrdriver.find_element_by_id("password")
    search_field.send_keys(pm_tmp_pasw)
    # newpassword
    search_field = chrdriver.find_element_by_id("nuova_password")
    search_field.clear()
    search_field.send_keys(password)

    search_field = chrdriver.find_element_by_id("ridigita_nuova_password")
    search_field.clear()
    search_field.send_keys(password)
    chrdriver.find_element_by_id("cambio_password").click()






