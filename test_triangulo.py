from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import pyautogui
import pyperclip

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def inserir_dados(a, b, c, driver):
    driver.get("https://www.vanilton.net/triangulo/#")
    lado_a = driver.find_element(By.NAME,"V1")
    lado_b = driver.find_element(By.NAME,"V2")
    lado_c = driver.find_element(By.NAME,"V3")
    botao = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Identificar']")

    lado_a.send_keys(a)
    lado_b.send_keys(b)
    lado_c.send_keys(c)

    botao.click()

    resultado = coletar_resultado()

    print(resultado)

    return resultado

def coletar_resultado():
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    texto = pyperclip.paste()
    if "Equilátero" in texto:
        return "Equilátero"
    elif "Isósceles" in texto:
        return "Isósceles"
    elif "Escaleno" in texto:
        return "Escaleno"
    else:
        return False


def test_triangulo_erro(driver):
    assert inserir_dados (1, 2, 3, driver) == False
    assert inserir_dados (0, 0, 0, driver) == False
    assert inserir_dados (-1, -1, -5, driver) == False

def test_equilatero(driver):
    assert inserir_dados (1, 1, 1, driver) == 'Equilátero'
    assert inserir_dados (5, 5, 5, driver) == 'Equilátero'
    assert inserir_dados (10, 10, 10, driver) == 'Equilátero'

def test_isosceles(driver):
    assert inserir_dados (1, 1, 2, driver) == "Isósceles"
    assert inserir_dados (3, 3, 5, driver) == "Isósceles"
    assert inserir_dados (12, 12, 15, driver) == "Isósceles"

def test_escaleno(driver):
    assert inserir_dados (2, 3, 4, driver) == "Escaleno"
    assert inserir_dados (5, 4, 3, driver) == "Escaleno"
    assert inserir_dados (10, 8, 6, driver) == "Escaleno"
