from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def test_Carica_Esame(chrdriver: webdriver.Chrome):

    chrdriver.find_element_by_link_text("Carica").click()
    chrdriver.find_element_by_link_text("Esame").click()

    chrdriver.find_element_by_xpath("//select[@name='sel_tipiesame']/option[text()='ECG - ECG']").click()
    chrdriver.find_element_by_xpath("//select[@name='inp_sel_sla']/option[text()='ECG ext 24h']").click()

    paziente_nome = chrdriver.find_element_by_id("inp_nome_paziente")
    paziente_nome.clear()
    paziente_nome.send_keys("TestSelenium_CaricaE")

    paziente_cognome = chrdriver.find_element_by_id("inp_cognome_paziente")
    paziente_cognome.clear()
    paziente_cognome.send_keys("TestSelenium_CaricaE")

    terapia = chrdriver.find_element_by_id("inp_terapia")
    terapia.clear()
    terapia.send_keys("TestSelenium_CaricaE")

    note = chrdriver.find_element_by_id("inp_note")
    note.clear()
    note.send_keys("TestSelenium_CaricaE")

    path_esame = "C:/Users/simon/Desktop/SeleniumTestCarica.pdf"
    chooseFile = chrdriver.find_element_by_id("file_exam")
    chooseFile.send_keys(path_esame)

    path_diario = "C:/Users/simon/Desktop/Diario.pdf"
    chooseFile = chrdriver.find_element_by_id("file_diary")
    chooseFile.send_keys(path_diario)

    chrdriver.save_screenshot(filename="C:/Users/simon/Desktop/ScreenShotSelenium/CaricaEsame.png")
    chrdriver.find_element_by_id("Invia").click()

    return (paziente_nome, paziente_cognome)

def test_Carica_Esame_PDF(chrdriver: webdriver.Chrome):

    chrdriver.find_element_by_link_text("Carica").click()
    chrdriver.find_element_by_link_text("Esame PDF").click()

    paziente_nome = chrdriver.find_element_by_id("inp_nome_paziente")
    paziente_nome.clear()
    paziente_nome.send_keys("TestSelenium_CaricaE_PDF")

    paziente_cognome = chrdriver.find_element_by_id("inp_cognome_paziente")
    paziente_cognome.clear()
    paziente_cognome.send_keys("TestSelenium_CaricaE_PDF")

    terapia = chrdriver.find_element_by_id("inp_terapia")
    terapia.clear()
    terapia.send_keys("TestSelenium_CaricaE_PDF")

    note = chrdriver.find_element_by_id("inp_note")
    note.clear()
    note.send_keys("TestSelenium_CaricaE_PDF")

    path_esame = "C:/Users/simon/Desktop/SeleniumTestCarica.pdf"
    chooseFile = chrdriver.find_element_by_id("file_exam")
    chooseFile.send_keys(path_esame)

    path_diario = "C:/Users/simon/Desktop/Diario.pdf"
    chooseFile = chrdriver.find_element_by_id("file_diary")
    chooseFile.send_keys(path_diario)

    chrdriver.save_screenshot(filename="C:/Users/simon/Desktop/ScreenShotSelenium/CaricaEsamePDF.png")
    chrdriver.find_element_by_id("Invia").click()

    return (paziente_nome, paziente_cognome)

def test_ilmioaccount (chrdriver: webdriver.Chrome, password):

    chrdriver.find_element_by_link_text("Il mio account").click()

    try:
        id_user = chrdriver.find_element_by_id("id_utente_disabled")
        id_user.clear()
        id_user.send_keys("14")
    except:
        pass

    utente_nome = chrdriver.find_element_by_id("nome")
    nome = utente_nome.get_attribute("value")
    utente_nome.clear()
    utente_nome.send_keys(nome)

    utente_cognome = chrdriver.find_element_by_id("cognome")
    cognome = utente_cognome.get_attribute("value")
    utente_cognome.clear()
    utente_cognome.send_keys(cognome)

    utente_datanascita = chrdriver.find_element_by_id("datadinascita")
    utente_datanascita.clear()
    try:
        utente_datanascita.send_keys("letters") #non dovrebbe accettarle
    except:
        utente_datanascita.send_keys("20-11-1998")

    utente_ldn = chrdriver.find_element_by_id("luogodinascita")
    utente_ldn.clear()
    utente_ldn.send_keys("123 luogodinascita")

    utente_mail = chrdriver.find_element_by_id("indirizzo_email")
    mail = utente_mail.get_attribute("value")
    utente_mail.clear()
    utente_mail.send_keys(mail)

    utente_cell = chrdriver.find_element_by_id("numero_cellulare")
    cell = utente_cell.get_attribute("value")
    utente_cell.clear()
    utente_cell.send_keys(cell)

    utente_tel = chrdriver.find_element_by_id("numero_telefono_fisso")
    tel = utente_tel.get_attribute("value")
    utente_tel.clear()
    utente_tel.send_keys(tel)

    utente_user = chrdriver.find_element_by_id("username")
    user = utente_user.get_attribute("value")
    utente_user.clear()
    utente_user.send_keys(user)

    utente_oldp = chrdriver.find_element_by_id("password_old")
    utente_oldp.clear()
    utente_oldp.send_keys(password)

    utente_p = chrdriver.find_element_by_id("password")
    utente_p.clear()
    utente_p.send_keys(password)

    utente_cp = chrdriver.find_element_by_id("conferma_password")
    utente_cp.clear()
    utente_cp.send_keys(password)

def test_Referta_Esame(chrdriver: webdriver.Chrome):
    print("Da implementareeee")

def enter_password_double_check(chrdriver: webdriver.Chrome, username, password, password1, successful_url):
    search_field = chrdriver.find_element_by_id("username")
    search_field.clear()
    search_field.send_keys(username)

    search_field = chrdriver.find_element_by_id("password")
    search_field.clear()
    search_field.send_keys(password)
    search_field.submit()
    check_url = chrdriver.current_url

    if check_url != successful_url:
        search_field = chrdriver.find_element_by_id("username")
        search_field.clear()
        search_field.send_keys(username)
        search_field = chrdriver.find_element_by_id("password")
        search_field.clear()
        search_field.send_keys(password1)
        search_field.submit()
        check_url = chrdriver.current_url

    return chrdriver
