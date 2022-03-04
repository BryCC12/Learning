from unittest import TestLoader,TestSuite, runner
from pyunitreport import HTMLTestRunner     #Genera el reporte correspondiente
from Assertions import AssertionsTest       #Llama nuestras clases de pruebas
from SearchTest import SearchTest

assertions_test=TestLoader().loadTestsFromTestCase(AssertionsTest)          #Carga las pruebas a realizar
search_test=TestLoader().loadTestsFromTestCase(SearchTest)                  #Carga las pruebas a realizar

Smoke_Test=TestSuite([assertions_test,search_test]);                        #Lista de pruebas

kwargs={"output":'Smoke_Test'}                                              #Parametros para generar el reporte
runner=HTMLTestRunner(**kwargs)                                             #Pasando los argumentos
runner.run(Smoke_Test)                                                      #Corriendo las pruebas con la TestSuite