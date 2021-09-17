import tests
from selenium import webdriver

def Staging (chrdriver: webdriver.Chrome):
    chrdriver.get("https://telecardiologia.cardiocalm.com/clinicavicinaweb-staging/")
    password="cardiocalm123456"
    username="clinicavicina_oper"

    search_field = chrdriver.find_element_by_id("username")
    search_field.clear()
    search_field.send_keys(username)

    search_field = chrdriver.find_element_by_id("password")
    search_field.clear()
    search_field.send_keys(password)
    search_field.submit()

    tests.test_Carica_Esame(chrdriver)
    tests.test_Carica_Esame_PDF(chrdriver)



