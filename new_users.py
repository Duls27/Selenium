from selenium import webdriver
from selenium.webdriver import ActionChains
import  tests


def administrator (link_piattaforma,chrdriver: webdriver.Chrome, password, password1,username):
    username_old_admin = "Amministratore"
    successful_url = link_piattaforma +"admin"
    chrdriver = tests.enter_password_double_check(chrdriver, username_old_admin, password, password1, successful_url)

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
    admin_usr.send_keys(username)
    admin_usr=username

    if username=="Apitest1":
        chrdriver.find_element_by_id("autenticazione-2").click() #sirio
    else:
        chrdriver.find_element_by_id("autenticazione-0").click()

    chrdriver.find_element_by_id("Salva").click()  # sirio

    return admin_usr

def project_manager (link_piattaforma,chrdriver: webdriver.Chrome, admin_usr, password, password1,new_projectmanager):
    successful_url=link_piattaforma+"admin"
    tests.enter_password_double_check(chrdriver, admin_usr, password, password1,successful_url)

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
    pm_usr.send_keys(new_projectmanager)
    pm_usr = new_projectmanager

    chrdriver.find_element_by_id("dati_sensibili").click()
    chrdriver.find_element_by_id("autenticazione-0").click()  # sirio
    chrdriver.find_element_by_xpath("/ html / body / div[5] / div / div / div / div[3] / form / div / div[3] / fieldset / select / option[1]").click()
    chrdriver.find_element_by_id("Salva").click()  # sirio
    chrdriver.find_element_by_xpath("    / html / body / nav / div[2] / ul[2] / li[2] / form / button").click()

    return pm_usr

def refertatore (link_piattaforma,chrdriver: webdriver.Chrome, admin_usr, password, password1,cardiologo):
    successful_url = link_piattaforma + "admin"
    tests.enter_password_double_check(chrdriver, admin_usr, password, password1, successful_url)

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
    ref_usr.send_keys(cardiologo)
    ref_usr = cardiologo

    from_element = chrdriver.find_element_by_xpath("//select[@id='tipi_esame']/option[text()='ECG']")
    to_element = chrdriver.find_element_by_xpath("//select[@id='tipi_esame']/option[text()='PDF']")
    action = ActionChains(chrdriver)
    action.click_and_hold(from_element).move_to_element(to_element).perform()

    chrdriver.find_element_by_id("firma_digitale").click()
    chrdriver.find_element_by_xpath("//*[@id='gruppo_centri_raccolta_ecg']/option[1]").click()
    chrdriver.find_element_by_xpath("/ html / body / div[5] / div / div / div / form[1] / div / div[2] / fieldset / dd[4] / select / option[2]").click()
    chrdriver.find_element_by_xpath("/html/body/div[5]/div/div/div/form[1]/div/div[5]/fieldset/div/input").click()

    return ref_usr

def struttura (link_piattaforma,chrdriver: webdriver.Chrome, admin_usr, password, password1,new_operatore,new_struttura):
    successful_url = link_piattaforma+"admin"
    tests.enter_password_double_check(chrdriver, admin_usr, password, password1, successful_url)

    chrdriver.find_element_by_xpath("/html/body/nav/div[2]/ul[1]/li[3]/a").click()
    chrdriver.find_element_by_xpath("/ html / body / nav / div[2] / ul[1] / li[3] / ul / li[2] / a").click()
    chrdriver.find_element_by_id("Nuovo").click()

    nome = chrdriver.find_element_by_id("nome")
    nome.clear()
    nome.send_keys(new_struttura)

    indirizzo = chrdriver.find_element_by_id("indirizzo")
    indirizzo.clear()
    indirizzo.send_keys("Radaelli")

    civico = chrdriver.find_element_by_id("civico")
    civico.clear()
    civico.send_keys("27")

    cap = chrdriver.find_element_by_id("cap")
    cap.clear()
    cap.send_keys("25018")

    comune = chrdriver.find_element_by_id("comune")
    comune.clear()
    comune.send_keys("Montichiari")

    provincia = chrdriver.find_element_by_id("provincia")
    provincia.clear()
    provincia.send_keys("Brescia")

    tel = chrdriver.find_element_by_id("telefono")
    tel.clear()
    tel.send_keys("1234567890")

    email = chrdriver.find_element_by_id("email")
    email.clear()
    email.send_keys("selenium.test.cc@gmail.com")

    chrdriver.find_element_by_id("stato-1").click()

    chrdriver.find_element_by_xpath("//select[@id='id_gruppo']/option[text()='GRUPPO TEST']").click()

    #operatore

    chrdriver.find_element_by_id("upload_exam").click()
    nome_oper = chrdriver.find_element_by_id("nome_operatore_site")
    nome_oper.clear()
    nome_oper.send_keys("Sel_Test")

    cognome_oper = chrdriver.find_element_by_id("cognome_operatore_site")
    cognome_oper.clear()
    cognome_oper.send_keys("Operatore_Struttura")

    username_oper = chrdriver.find_element_by_id("username_operatore_site")
    username_oper.clear()
    username_oper.send_keys(new_operatore)
    username_oper=new_operatore

    email_oper = chrdriver.find_element_by_id("email_operatore_site")
    email_oper.clear()
    email_oper.send_keys("selenium.test.cc@gmail.com")

######Referente Sanitario

    nome_rs = chrdriver.find_element_by_id("nome_referente_tecnico")
    nome_rs.clear()
    nome_rs.send_keys("Sel_Test")
    rs_nome="Sel_Test"

    cognome_oper = chrdriver.find_element_by_id("cognome_referente_tecnico")
    cognome_oper.clear()
    cognome_oper.send_keys("Ref_Sanitario")
    rs_cognome= "Ref_Sanitario"

    email_rs = chrdriver.find_element_by_id("email_referente_tecnico")
    email_rs.clear()
    email_rs.send_keys("selenium.test.cc@gmail.com")

    colore = chrdriver.find_element_by_id("referto_colore")
    colore.clear()
    colore.send_keys("#9966CC")

    chrdriver.find_element_by_id("Salva").click()

    chrdriver.find_element_by_xpath("// *[ @ id = 'navbar'] / ul[2] / li[2] / form / button").click()

    return username_oper, rs_nome, rs_cognome












