from selenium import webdriver
import email_managment
import  new_users, tests

password = "cardiocalm123456"
password1 = "pippo1234"

def complete_structure(chrdriver: webdriver.Chrome, mail, mailpassword):
    chrdriver.get("https://telecardiologia.cardiocalm.com/clinicavicinaweb-staging/")

    #delete emails from gmail
    #email_managment.delete_all_emails(mail, mailpassword)
    # Creazione nuovo utente
    #admin_usr=new_users.administrator(chrdriver, password, password1)
    admin_usr="AmministratoreTest"
    #read one time password mail
    admin_psw=email_managment.read_password_from_emails(mail, mailpassword)
    #enter reset password
    chrdriver=tests.enter_password_double_check(chrdriver,admin_usr,admin_psw,admin_psw,"https://telecardiologia.cardiocalm.com/clinicavicinaweb-staging/index/cambio-Password")

    #newpassword
    search_field = chrdriver.find_element_by_id("nuova_password")
    search_field.clear()
    search_field.send_keys(password)

    search_field = chrdriver.find_element_by_id("ridigita_nuova_password")
    search_field.clear()
    search_field.send_keys(password)

    chrdriver.find_element_by_id("continua").click()
    #return new admin info
    return (admin_usr, password)


