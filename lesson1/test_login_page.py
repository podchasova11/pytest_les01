from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPage: # Название тестового класса

    def test_open_login_page(self): # Название нашего теста
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.freeconferencecall.com/login")
        assert driver.title == "Страница входа | FreeConferenceCall.com", "Страница логина не была открыта"

    def test_open_login_page(self):  # Название нашего теста
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        assert driver.title == "OrangeHRM", "Страница логина не была открыта"