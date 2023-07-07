from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/feed/")


# Aguarde o pressionamento de Enter para fechar a página
input("Pressione Enter para fechar a página...")
botao = driver.find_element_by_xpath('/html/body/div/div/div[2]')

botao.click()
# Encerre o driver do Selenium
driver.quit()