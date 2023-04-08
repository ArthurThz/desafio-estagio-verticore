


# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    desktop_bot = DesktopBot()


    webbot = WebBot()

    webbot.headless = False

   
   
    webbot.driver_path = "chromedriver_win32/chromedriver.exe"

    # Opens the BotCity website.
    webbot.browse("https://cidades.ibge.gov.br/")

    
    webbot.wait(1000)
   
    if not webbot.find( "comece", matching=0.97, waiting_time=10000):
        not_found("comece")
    webbot.click()
    
    if not webbot.find( "find_estados", matching=0.97, waiting_time=10000):
        not_found("find_estados")
    webbot.click()

    webbot.wait(1000)
    
    if not webbot.find( "acre", matching=0.97, waiting_time=10000):
        not_found("acre")
    webbot.click()

    webbot.wait(1000)
    
    if not webbot.find( "find_gentilico", matching=0.97, waiting_time=10000):
        not_found("find_gentilico")   
    
    webbot.double_click_relative(25, 23)
    webbot.control_c()    

    gentilico = webbot.get_clipboard()
    print(gentilico)
    webbot.wait(1000)

    if not webbot.find( "find_capital", matching=0.97, waiting_time=10000):
        not_found("find_capital")

    webbot.triple_click_relative(25, 23)
    webbot.control_c() 
    capital =  webbot.get_clipboard()      
    print(capital)

    webbot.wait(1000)
    
    if not webbot.find( "find_governador", matching=0.97, waiting_time=10000):
        not_found("find_governador")    
    
    webbot.triple_click_relative(25, 23)
    webbot.control_c() 
    governador =  webbot.get_clipboard()      
    print(governador)
    webbot.wait(2000)

    if not webbot.find( "find_populacao", matching=0.97, waiting_time=10000):
        not_found("find_populacao")
    
    webbot.double_click_relative(275, 6)
       
    
    
    
    
    
    

  
   

 

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()

