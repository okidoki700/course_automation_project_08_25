import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException, NoSuchElementException


@pytest.fixture(scope="function")
def driver_setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    yield driver, wait
    driver.quit()

@pytest.fixture(scope="function")
def go_to_home(driver_setup):
    driver, wait = driver_setup
    driver.get("https://automationexercise.com/login")
    wait = WebDriverWait(driver, 10)

    # Locate username and password fields
    username_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))

    # Enter valid credentials
    username_field.send_keys("hagai.tregerman@gmail.com")
    password_field.send_keys("KMsuTYNyY@Q5y")
    password_field.send_keys(Keys.RETURN)

    yield driver, wait


@pytest.mark.sanity
def test_login_valid_credentials(go_to_home):
    # setup WebDriver
    driver, wait = go_to_home

    try:
        # Locate username and password fields
        username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))

    except (TimeoutException, NoSuchElementException) as e:
        pytest.fail(f"Test failed due to an unexpected error: {e}")








if __name__ == "__main__":
    pytest.main()