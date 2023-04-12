

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
       
    

    #lista para armazenar os dados a serem coletados
    dados_coletados = []  


    #Funcoes de coleta de dados
    def getGentilico():        
        gentilico = webbot.find_element('//*[@id="dados"]/panorama-resumo/div/div[1]/div[2]/div/p',By.XPATH).text
        dados_coletados.append(gentilico)

    def getCapital():
        capital = webbot.find_element('//*[@id="dados"]/panorama-resumo/div/div[1]/div[3]/div/p',By.XPATH).text
        dados_coletados.append(capital)

    
    def getGovernador():       
        governador = webbot.find_element('//*[@id="dados"]/panorama-resumo/div/div[1]/div[4]/div/p',By.XPATH).text
        dados_coletados.append(governador)       

    def getPopulacao():       
       populacao = webbot.find_element('//*[@id="dados"]/panorama-resumo/div/table/tr[2]/td[3]/valor-indicador/div/span[1]',By.XPATH).text
       dados_coletados.append(populacao)

    def getIDH():
        webbot.find_element('//*[@id="dados"]/panorama-resumo/div/table/tr[40]/th[2]',By.XPATH).click()
        idh = webbot.find_element('//*[@id="dados"]/panorama-resumo/div/table/tr[41]/td[3]/valor-indicador/div/span[1]',By.XPATH).text
        dados_coletados.append(idh)          

    
    def searchData():
        estados = ["ac","al","ap","am","ba","ce","es","go","ma","mt","ms","mg","pa","pb","pr","pe","pi","rj","rn","rs","ro","rr","sc","sp","se","to","df"]
        for sigla in estados:   
            webbot.browse(f"https://cidades.ibge.gov.br/brasil/{sigla}/panorama")   
            getGentilico()
            getCapital()
            getGovernador()
            getPopulacao()
            getIDH()
            Page_Informacoes.append(dados_coletados)
            dados_coletados.clear()
            book.save("dados_ibge.xlsx")          

        sendEmail() 
    
    searchData()    
    
    maestro.finish_task(
        task_id=execution.task_id,
        status=AutomationTaskFinishStatus.SUCCESS,
        message="Task Finished OK."
    )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()







