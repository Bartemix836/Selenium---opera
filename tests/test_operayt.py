import pytest
import allure
from selenium import webdriver
from selenium.webdriver.opera.options import Options as OperaOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from pages.base_page import BasePage
import time


# Ustawienia opcji dla Opery
@pytest.fixture(scope="function")
def setup_driver():
    options = OperaOptions()
    options.binary_location = r'A:\opera.exe'  # Ścieżka do pliku Opera
    driver = webdriver.Opera(
        executable_path=r'C:\Users\barte\PycharmProjects\selenium_kurs\test_coinsbase\driver\operadriver.exe',
        options=options
    )
    yield driver
    driver.quit()


@allure.step("Clicking and waiting for element located by {by} = {value}")
def click_and_wait(driver, by, value, wait_time=10):
    try:
        element = WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((by, value)))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((by, value)))
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
    except Exception as e:
        print(f"Error clicking element {value}: {e}")
        raise


@allure.feature("Coinbase Navigation")
@allure.story("User navigates through Coinbase and interacts with video")
def test_coinbase_navigation(setup_driver):
    driver = setup_driver  # Użycie fixture
    base_page = BasePage(driver)
    wait = WebDriverWait(driver, 20)

    try:
        with allure.step("Opening the Coinbase homepage"):
            driver.get("https://www.coinbase.com/")
            time.sleep(7)

        with allure.step("Accepting cookies"):
            accept_cookies_btn_xpath = '//*[@id="root"]/div/div[2]/div/div/button[2]'
            wait.until(EC.element_to_be_clickable((By.XPATH, accept_cookies_btn_xpath)))
            base_page.click_element(By.XPATH, accept_cookies_btn_xpath)

        with allure.step("Hovering over the Learn More tab"):
            learn_more_tab_xpath = '//*[@id="root"]/div/div/header/div[2]/div/div/nav/a[2]/div/span'
            wait.until(EC.visibility_of_element_located((By.XPATH, learn_more_tab_xpath)))
            base_page.hover_over_element(By.XPATH, learn_more_tab_xpath)
            time.sleep(4)

        with allure.step("Hovering and clicking on 'Tips and Tutorials'"):
            tips_and_tutorials_xpath = '/html/body/div[1]/div/div/header/div[2]/div/div/nav/section[1]/div/div/div[1]/a[1]'
            wait.until(EC.visibility_of_element_located((By.XPATH, tips_and_tutorials_xpath)))
            base_page.click_element(By.XPATH, tips_and_tutorials_xpath)
            time.sleep(4)

        with allure.step("Clicking on the selected article element"):
            chosen_article_xpath = '/html/body/div[1]/div/main/main/div/section/div/div/div[2]/div/div[1]/a[3]'
            wait.until(EC.visibility_of_element_located((By.XPATH, chosen_article_xpath)))
            base_page.click_element(By.XPATH, chosen_article_xpath)
            time.sleep(4)

        with allure.step("Playing the video"):
            playbtn_xpath = '/html/body/div[1]/div/main/main/div/article/div/div/div/div/div/section[1]/div/div/div/div/div/div/button'
            wait.until(EC.visibility_of_element_located((By.XPATH, playbtn_xpath)))
            base_page.click_element(By.XPATH, playbtn_xpath)
            time.sleep(10)

        with allure.step("Closing the current tab"):
            base_page.close_tab()
            time.sleep(2)

        print('-----------------------------------------------------------------------------------')
        print('Test Completed Successfully!')
        time.sleep(2)

    except Exception as e:
        print(f"Wystąpił błąd: {e}")

    finally:
        time.sleep(5)  # Optional: Give time to observe the last action
        driver.quit()
