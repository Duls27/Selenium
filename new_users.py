from selenium import webdriver
import  tests


def administrator (chrdriver: webdriver.Chrome, password, password1):
    username = "Amministratore"
    successful_url = "https://telecardiologia.cardiocalm.com/clinicavicinaweb-staging/admin"
    chrdriver = tests.enter_password_double_check(chrdriver, username, password, password1, successful_url)

    chrdriver.find_element_by_link_text("Gestione Utenti").click()
    chrdriver.find_element_by_link_text("Amministratori").click()
    chrdriver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[2]/div[2]/form/input").click()

#filliig New Administrator
    admin_name = chrdriver.find_element_by_id("nome")
    admin_name.clear()
    admin_name.send_keys("Sel_Test_Admin")

    admin_sur = chrdriver.find_element_by_id("cognome")
    admin_sur.clear()
    admin_sur.send_keys("Sel_Test_Admin")

    admin_ddn = chrdriver.find_element_by_id("datadinascita")
    admin_ddn.clear()
    admin_ddn.send_keys("20-11-1998")

    admin_ldn = chrdriver.find_element_by_id("luogodinascita")
    admin_ldn.clear()
    admin_ldn.send_keys("CardioCalm")

    admin_mail = chrdriver.find_element_by_id("indirizzo_email")
    admin_mail.clear()
    admin_mail.send_keys("selenium.test.cc@gmail.com")

    admin_cel = chrdriver.find_element_by_id("numero_cellulare")
    admin_cel.clear()
    admin_cel.send_keys("1234567890")

    admin_usr = chrdriver.find_element_by_id("username")
    admin_usr.clear()
    admin_usr.send_keys("AmministratoreTest")

    chrdriver.find_element_by_id("autenticazione-0").click() #sirio
    #chrdriver.find_element_by_id("Salva").click()  # sirio

    return admin_usr


