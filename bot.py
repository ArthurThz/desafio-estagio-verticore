

import openpyxl
from send_email import sendEmail
from botcity.web import WebBot, Browser, By
from botcity.maestro import *
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():   
    maestro = BotMaestroSDK.from_sys_args()    
    execution = maestro.get_execution()
    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    #Webbot configs
    webbot = WebBot()
    webbot.headless = False   
    webbot.driver_path = "chromedriver_win32/chromedriver.exe"

    #Criação da planilha
    book = openpyxl.Workbook()
    Page_Informacoes = book["Sheet"]
    Page_Informacoes.append(["Gentilico","Capital","Governador","População","IDH"])
    book.save("dados_ibge.xlsx")   
    

    #lista para armazenar os dados a serem coletados
    dados_coletados = []  


    #Funcoes de coleta de dados
    def getGentilico():        
        if not webbot.find_text( "gentilico", matching=0.97, waiting_time=10000):
            not_found("gentilico")              
        webbot.triple_click_relative(1,27)
        webbot.control_c()
        gentilico = webbot.get_clipboard()
        dados_coletados.append(gentilico)

    def getCapital():
        if not webbot.find_text( "find_capital", matching=0.97, waiting_time=10000):
            not_found("find_capital")
        webbot.triple_click_relative(1, 20)
        webbot.control_c()
        capital = webbot.get_clipboard()
        dados_coletados.append(capital)

    
    def getGovernador():
        if not webbot.find_text( "find_governador", matching=0.97, waiting_time=10000):
           not_found("find_governador")
        webbot.triple_click_relative(1, 20)
        webbot.control_c()
        governador = webbot.get_clipboard()
        dados_coletados.append(governador)       

    def getPopulacao():
       if not webbot.find_text( "find_populacao", matching=0.97, waiting_time=10000):
           not_found("find_populacao")
       webbot.double_click_relative(124, 109)
       webbot.control_c()
       populacao = webbot.get_clipboard()
       dados_coletados.append(populacao)

    def getIDH():
        if not webbot.find_text( "open_economia", matching=0.97, waiting_time=10000):
            not_found("open_economia")
        webbot.click()
        if not webbot.find_text( "find_idh", matching=0.97, waiting_time=10000):
            not_found("find_idh")
        webbot.triple_click_relative(277, 45)
        webbot.control_c()
        idh = webbot.get_clipboard()
        dados_coletados.append(idh)          

    
    def searchData(sigla):        
        webbot.browse(f"https://cidades.ibge.gov.br/brasil/{sigla}/panorama")
        webbot.maximize_window()
        webbot.wait(1000)

        getGentilico()
        getCapital()
        getGovernador()
        getPopulacao()
        getIDH()     
        
        Page_Informacoes.append(dados_coletados)
        book.save("dados_ibge.xlsx")
        sendEmail()
        

    #executa o BOT, basta digitar a sigla do estados que deseja e o bot realizará a coleta dos dados.
    searchData("ba")
           
    
    # estados = ["sp","ac","pe"]  
    
    # for sigla in estados:
    #     webbot.browse(f"https://cidades.ibge.gov.br/brasil/{sigla}/panorama")
    #     webbot.maximize_window()
    #     searchData()
        
    
    maestro.finish_task(
        task_id=execution.task_id,
        status=AutomationTaskFinishStatus.SUCCESS,
        message="Task Finished OK."
    )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()







