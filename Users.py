import tests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def oper (chrdriver: webdriver.Chrome):
    password = "cardiocalm123456"
    password1 = "pippo1234"
    username = "clinicavicina_oper"
    successful_url="https://telecardiologia.cardiocalm.com/clinicavicinaweb-staging/opersite"

    chrdriver=tests.enter_password_double_check(chrdriver,username,password,password1,successful_url)

    pnome, pcognome=tests.test_Carica_Esame(chrdriver)
    pnome_pdf, pcognome_pdf=tests.test_Carica_Esame_PDF(chrdriver)
    tests.test_ilmioaccount(chrdriver, "cardiocalm123456")

    return pnome, pcognome, pnome_pdf, pcognome_pdf

def refertatore (chrdriver: webdriver.Chrome):
    password = "cardiocalm123456"
    password1 = "pippo1234"
    username = "f.balzano"
    successful_url="https://telecardiologia.cardiocalm.com/clinicavicinaweb-staging/cardio"

    chrdriver=tests.enter_password_double_check(chrdriver,username,password,password1,successful_url)

    tests.test_Referta_Esame(chrdriver)
