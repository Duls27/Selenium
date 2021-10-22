import tests
from selenium import webdriver

#carica esame, carica esame PDF, modifica informazion personali OPERATORE
def basic_tests_operatore (link_piattaforma,chrdriver: webdriver.Chrome,usr, pwd, path_diario, path_esame, path_screenshots):
    chrdriver.get(link_piattaforma)
    succesfoul_url = link_piattaforma+"opersite"
    chrdriver_oper=tests.enter_password_double_check(chrdriver, usr, pwd, pwd, succesfoul_url)
    nome_paziente_c=tests.test_Carica_Esame(chrdriver_oper,path_screenshots, path_esame, path_diario)
    nome_paziente_cpdf= tests.test_Carica_Esame_PDF(chrdriver_oper, path_screenshots, path_esame, path_diario)
    #tests.test_ilmioaccount(chrdriver_oper, pwd)
    return nome_paziente_c, nome_paziente_cpdf

def basic_tests_refertatore(link_piattaforma,chrdriver: webdriver.Chrome,usr, pwd, path_referto, path_screenshots,paziente):
    chrdriver.get(link_piattaforma)
    succesfoul_url = link_piattaforma+"cardio"
    chrdriver_ref = tests.enter_password_double_check(chrdriver, usr, pwd, pwd, succesfoul_url)
    tests.test_Referta_Esame(chrdriver_ref,path_screenshots, path_referto,paziente)




