import Users
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def Staging (chrdriver: webdriver.Chrome):
    chrdriver.get("https://telecardiologia.cardiocalm.com/clinicavicinaweb-staging/")
#Test sull' operatore
    #pnome, pcognome, pnome_pdf, pcognome_pdf=Users.oper(chrdriver)
#Test refertatore
    Users.refertatore(chrdriver)





