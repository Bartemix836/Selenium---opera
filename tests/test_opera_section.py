import pytest
import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.opera.options import Options as OperaOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.base_page import BasePage
import time

# Browser setup for Opera
@pytest.fixture(scope="function")
def setup_driver():
    options = OperaOptions()
    options.binary_location = r'A:\opera.exe'
    driver = webdriver.Opera(
        executable_path=r'driver\operadriver.exe',
        options=options
    )
    yield driver
    driver.quit()


@allure.feature("Coinbase Navigation")
@allure.story("User navigates through Coinbase")
def test_opera_section(setup_driver):
    driver = setup_driver
    base_page = BasePage(driver)
    wait = WebDriverWait(driver, 20)

    try:
        with allure.step("Opening Coinbase homepage"):
            driver.get("https://www.coinbase.com/")
            time.sleep(7)

        with allure.step("Accepting cookies"):
            accept_cookies_btn_xpath = '//*[@id="root"]/div/div[2]/div/div/button[2]'
            wait.until(EC.element_to_be_clickable((By.XPATH, accept_cookies_btn_xpath)))
            base_page.click_element(By.XPATH, accept_cookies_btn_xpath)

        with allure.step("Navigating to the cryptocurrencies tab"):
            crypto_tab_xpath = '//*[@id="root"]/div/div[1]/header/div[2]/div/div/nav/a[1]/div/span'
            wait.until(EC.visibility_of_element_located((By.XPATH, crypto_tab_xpath)))
            base_page.click_element(By.XPATH, crypto_tab_xpath)
            time.sleep(5)

        with allure.step("Navigating to the 'Learn more' tab"):
            # learn_tab_xpath = '/html/body/div[1]/div/div/header/div/header/div[2]/div/div/nav/a[2]/div/span'
            # wait.until(EC.visibility_of_element_located((By.XPATH, learn_tab_xpath)))
            # base_page.hover_over_element(By.XPATH, learn_tab_xpath)
            # time.sleep(3)
            learn_element_xpath = '//a[@data-testid="main-nav-link-learn"]'
            learn_element = wait.until(EC.presence_of_element_located((By.XPATH, learn_element_xpath)))
            # Użycie ActionChains do najechania kursorem
            actions = ActionChains(driver)
            actions.move_to_element(learn_element).perform()
            time.sleep(2)

        with allure.step("Opening the crypto basics"):
            # xpath_glossary = '/html/body/div[1]/div/div/header/div/header/div[2]/div/div/nav/section[1]/div/div/div[1]/a[2]'
            # base_page.click_element(By.XPATH, xpath_glossary)
            # time.sleep(5)
            print("Clicking on the 'Crypto basics' link...")
            crypto_basics_xpath = '//a[@title="Crypto Basics - Explaining the fundamentals"]'
            crypto_basics_element = wait.until(EC.element_to_be_clickable((By.XPATH, crypto_basics_xpath)))
            crypto_basics_element.click()
            time.sleep(2)

        with allure.step("Selecting 'What is Bitcoin' article"):
            xpath_defi1 = '//*[@id="main"]/div/section/div/div/div[2]/div/div[1]/a[1]'
            wait.until(EC.visibility_of_element_located((By.XPATH, xpath_defi1)))
            base_page.click_element(By.XPATH, xpath_defi1)
            time.sleep(2)

        with allure.step("Returning to the glossary page"):
            glossary_url = 'https://www.coinbase.com/learn/crypto-glossary'
            base_page.load_page(glossary_url)
            time.sleep(2)

        with allure.step("Selecting the NFT article"):
            nft_article_xpath = '//*[@id="main"]/div/section/div/div/div[2]/div/div[1]/a[2]'
            wait.until(EC.visibility_of_element_located((By.XPATH, nft_article_xpath)))
            base_page.click_element(By.XPATH, nft_article_xpath)
            time.sleep(2)

        # Steps to navigate through each article section
        with allure.step("Navigating through each article section"):
            print("11. Navigating through each section...")

            chapter1_xpath = '/html/body/div[1]/div/main/main/div/article/div/div/aside/section/nav/ul/li[1]/a'
            wait.until(EC.visibility_of_element_located((By.XPATH, chapter1_xpath)))
            base_page.click_element(By.XPATH, chapter1_xpath)
            time.sleep(2)

            chapter2_xpath = '/html/body/div[1]/div/main/main/div/article/div/div/aside/section/nav/ul/li[2]/a'
            wait.until(EC.visibility_of_element_located((By.XPATH, chapter2_xpath)))
            base_page.click_element(By.XPATH, chapter2_xpath)
            time.sleep(2)

            chapter3_xpath = '/html/body/div[1]/div/main/main/div/article/div/div/aside/section/nav/ul/li[3]/a'
            wait.until(EC.visibility_of_element_located((By.XPATH, chapter3_xpath)))
            base_page.click_element(By.XPATH, chapter3_xpath)
            time.sleep(2)

            chapter4_xpath = '/html/body/div[1]/div/main/main/div/article/div/div/aside/section/nav/ul/li[4]/a'
            wait.until(EC.visibility_of_element_located((By.XPATH, chapter4_xpath)))
            base_page.click_element(By.XPATH, chapter4_xpath)
            time.sleep(2)

            chapter5_xpath = '/html/body/div[1]/div/main/main/div/article/div/div/aside/section/nav/ul/li[5]/a'
            wait.until(EC.visibility_of_element_located((By.XPATH, chapter5_xpath)))
            base_page.click_element(By.XPATH, chapter5_xpath)
            time.sleep(2)

        with allure.step("Returning to the homepage"):
            homepage_xpath = '//*[@id="root"]/div/header/div[2]/div/div/div[1]/a'
            wait.until(EC.visibility_of_element_located((By.XPATH, homepage_xpath)))
            base_page.click_element(By.XPATH, homepage_xpath)

        print('Test completed successfully!')

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        time.sleep(5)  # Optional: pause to observe the last action
        driver.quit()
