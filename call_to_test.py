import tests
from selenium import webdriver

#carica esame, carica esame PDF, modifica informazion personali OPERATORE + lettura esami caricati REFERTATORE
def basic_tests_operatore (chrdriver: webdriver.Chrome,usr, pwd, path_diario, path_esame, path_screenshots):
    chrdriver.get("https://telecardiologia.cardiocalm.com/clinicavicinaweb-staging")
    succesfoul_url = "https://telecardiologia.cardiocalm.com/clinicavicinaweb-staging/opersite"
    chrdriver_oper=tests.enter_password_double_check(chrdriver, usr, pwd, pwd, succesfoul_url)
    ncarica, ccarica=tests.test_Carica_Esame(chrdriver_oper,path_screenshots, path_esame, path_diario)
    ncaricapdf, ccaricapdf= tests.test_Carica_Esame_PDF(chrdriver_oper, path_screenshots, path_esame, path_diario)
    tests.test_ilmioaccount(chrdriver_oper, pwd)
    return [ncarica, ccarica], [ncaricapdf, ccaricapdf]

def basic_tests_refertatore(chrdriver: webdriver.Chrome,usr, pwd, path_referto, path_screenshots,p1,p2):
    chrdriver.get("https://telecardiologia.cardiocalm.com/clinicavicinaweb-staging")
    succesfoul_url = "https://telecardiologia.cardiocalm.com/clinicavicinaweb-staging/cardio"
    chrdriver_ref = tests.enter_password_double_check(chrdriver, usr, pwd, pwd, succesfoul_url)
    tests.test_Referta_Esame(chrdriver_ref,path_screenshots, path_referto,p1,p2)




