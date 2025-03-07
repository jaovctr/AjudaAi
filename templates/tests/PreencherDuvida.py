# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=options, executable_path='/usr/bin/chromedriver')
class TestPreencherinformaes():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(chrome_options=options, executable_path='/usr/bin/chromedriver')
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_preencherinformaes(self):
    self.driver.get("https://ajudaai.pythonanywhere.com/")
    self.driver.set_window_size(1417, 1032)
    self.driver.find_element(By.ID, "icon-forum").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ask-question-button").click()
    self.driver.find_element(By.ID, "titulo").click()
    self.driver.find_element(By.ID, "titulo").send_keys("Grafos em python")
    self.driver.find_element(By.ID, "descricao-pergunta").click()
    self.driver.find_element(By.ID, "descricao-pergunta").send_keys("Alguma biblioteca que possibilite a visualização de grafos em python? #programacao #python")
    self.driver.find_element(By.CSS_SELECTOR, ".botao-cadastro").click()
  
