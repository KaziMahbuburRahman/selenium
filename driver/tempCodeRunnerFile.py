from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# service = Service('driver/chromedriver.exe')

#download the browser driver automatically without specifying the path
service = Service(ChromeDriverManager().install())



driver = webdriver.Chrome(service=service)



driver.get('https://www.google.com')

#keep the browser open
input('Press Enter to close the automated browser')
driver.quit()