from selenium import webdriver

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
    #chrdriver.find_element_by_id("Invia").click()

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
    #chrdriver.find_element_by_id("Invia").click()

