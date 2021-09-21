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
    admin_name.send_keys("Sel_Test")

    admin_sur = chrdriver.find_element_by_id("cognome")
    admin_sur.clear()
    admin_sur.send_keys("Admin")

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
    admin_usr="AmministratoreTest"

    chrdriver.find_element_by_id("autenticazione-0").click() #sirio
    chrdriver.find_element_by_id("Salva").click()  # sirio

    return admin_usr

def project_manager (chrdriver: webdriver.Chrome, admin_usr, password, password1):
    tests.enter_password_double_check(chrdriver, admin_usr, password, password1,
                                      "https://telecardiologia.cardiocalm.com/clinicavicinaweb-staging/admin")

    chrdriver.find_element_by_xpath("/ html / body / nav / div[2] / ul[1] / li[4] / a").click()
    chrdriver.find_element_by_xpath("/html/body/nav/div[2]/ul[1]/li[4]/ul/li[2]/a").click()
    chrdriver.find_element_by_xpath("/ html / body / div[5] / div / div / div / div[2] / div / form / input").click()

    # filliig New Administrator
    pm_name = chrdriver.find_element_by_id("nome")
    pm_name.clear()
    pm_name.send_keys("Sel_Test")

    pm_sur = chrdriver.find_element_by_id("cognome")
    pm_sur.clear()
    pm_sur.send_keys("ProjMan")

    pm_ddn = chrdriver.find_element_by_id("datadinascita")
    pm_ddn.clear()
    pm_ddn.send_keys("20-11-1998")

    pm_ldn = chrdriver.find_element_by_id("luogodinascita")
    pm_ldn.clear()
    pm_ldn.send_keys("CardioCalm")

    pm_mail = chrdriver.find_element_by_id("indirizzo_email")
    pm_mail.clear()
    pm_mail.send_keys("selenium.test.cc@gmail.com")

    pm_cel = chrdriver.find_element_by_id("numero_cellulare")
    pm_cel.clear()
    pm_cel.send_keys("1234567890")

    pm_usr = chrdriver.find_element_by_id("username")
    pm_usr.clear()
    pm_usr.send_keys("PMtest")
    pm_usr="PMtest"

    chrdriver.find_element_by_id("dati_sensibili").click()
    chrdriver.find_element_by_id("autenticazione-0").click()  # sirio
    chrdriver.find_element_by_xpath("/ html / body / div[5] / div / div / div / div[3] / form / div / div[3] / fieldset / select / option[1]").click()
    chrdriver.find_element_by_id("Salva").click()  # sirio
    chrdriver.find_element_by_xpath("    / html / body / nav / div[2] / ul[2] / li[2] / form / button").click()

    return pm_usr

def refertatore (chrdriver: webdriver.Chrome, admin_usr, password, password1):
    tests.enter_password_double_check(chrdriver, admin_usr, password, password1,
                                      "https://telecardiologia.cardiocalm.com/clinicavicinaweb-staging/admin")

    chrdriver.find_element_by_xpath("/ html / body / nav / div[2] / ul[1] / li[4] / a").click()
    chrdriver.find_element_by_xpath("/ html / body / nav / div[2] / ul[1] / li[4] / ul / li[3] / a").click()
    chrdriver.find_element_by_xpath("/ html / body / div[5] / div / div / div / div[2] / div / form / input").click()

    ref_name = chrdriver.find_element_by_id("nome")
    ref_name.clear()
    ref_name.send_keys("Sel_Test")

    ref_sur = chrdriver.find_element_by_id("cognome")
    ref_sur.clear()
    ref_sur.send_keys("Refertatore")

    ref_ddn = chrdriver.find_element_by_id("datadinascita")
    ref_ddn.clear()
    ref_ddn.send_keys("20-11-1998")

    ref_ldn = chrdriver.find_element_by_id("luogodinascita")
    ref_ldn.clear()
    ref_ldn.send_keys("CardioCalm")

    ref_mail = chrdriver.find_element_by_id("indirizzo_email")
    ref_mail.clear()
    ref_mail.send_keys("selenium.test.cc@gmail.com")

    ref_cel = chrdriver.find_element_by_id("numero_cellulare")
    ref_cel.clear()
    ref_cel.send_keys("1234567890")

    ref_usr = chrdriver.find_element_by_id("username")
    ref_usr.clear()
    ref_usr.send_keys("Reftest")
    ref_usr = "Reftest"

    chrdriver.find_element_by_id("firma_digitale").click()
    chrdriver.find_element_by_xpath("/ html / body / div[5] / div / div / div / form[1] / div / div[2] / fieldset / dd[4] / select / option[2]").click()
    chrdriver.find_element_by_xpath("/html/body/div[5]/div/div/div/form[1]/div/div[5]/fieldset/div/input").click()

    return ref_usr

