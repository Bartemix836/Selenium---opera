from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def hover_over_element(self, by, value):
        try:
            element_to_hover_over = self.driver.find_element(by, value)
            hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
            hover.perform()
            print("Hovered over element")
        except Exception as e:
            print(f"Failed to hover over element: {e}")

    def click_element(self, by, value):
        try:
            element_to_click = self.driver.find_element(by, value)
            element_to_click.click()
            print("Clicked on element")
        except Exception as e:
            print(f"Failed to click on element: {e}")

    def right_click_and_select_option(driver, element, option_xpath):
        # Inicjalizacja ActionChains
        action_chains = ActionChains(driver)

        # Kliknięcie prawym przyciskiem myszy na elemencie
        action_chains.context_click(element).perform()

        # Czekamy na pojawienie się opcji menu
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, option_xpath)))
        #
        # # Kliknięcie opcji z menu
        # driver.find_element(By.XPATH, option_xpath).click()


    def click_element_js(self, by, value):
        try:
            element = self.driver.find_element(by, value)
            self.driver.execute_script("arguments[0].click();", element)
            print(f"Element clicked using JavaScript: {value}")
        except Exception as e:
            print(f"Failed to click element using JavaScript: {e}")

    def click_elementtarget(self, by, value, href=None):
        try:
            # Jeśli href jest podane, otwórz nowy URL w nowej karcie
            if href:
                self.driver.execute_script("window.open(arguments[0], '_blank');", href)
                print(f"Opened '{href}' in new tab without clicking on element")
            else:
                # Znajdź element i kliknij go, jeśli href nie jest podane
                element_to_click = self.driver.find_element(by, value)
                element_to_click.click()  # Kliknięcie w element
                print("Clicked on element without opening a new tab")

        except Exception as e:
            print(f"Failed to click on element: {e}")




    def fill_text_field(self, by, value, text):
        try:
            text_field = self.driver.find_element(by, value)
            text_field.send_keys(text)
            print(f"Entered text '{text}' into text field")
        except Exception as e:
            print(f"Failed to enter text into text field: {e}")

    def select_radio_button(self, by, value):
        try:
            radio_button = self.driver.find_element(by, value)
            if not radio_button.is_selected():
                radio_button.click()
                print(f"Selected radio button with XPATH: {value}")
            else:
                print(f"Radio button with XPATH: {value} is already selected")
        except Exception as e:
            print(f"Failed to select radio button: {e}")

    def select_dropdown_option_by_index(self, dropdown_xpath, index):
        try:
            # Find the dropdown element based on XPath
            dropdown_element = self.driver.find_element(By.XPATH, dropdown_xpath)

            # Initialize Select for the dropdown element
            dropdown = Select(dropdown_element)

            # Select the option based on the provided index
            dropdown.select_by_index(index)

            print(f"Selected option with index {index} from dropdown.")
        except Exception as e:
            print(f"Failed to select option from dropdown: {e}")

    def load_page(self, url):
        try:
            # Load the page with the given URL
            self.driver.get(url)
            print(f"Loaded page with URL: {url}")
        except Exception as e:
            print(f"Failed to load page: {e}")

    def switch_to_tab(self, tab_index):
        # Przełącz się na kartę o danym indeksie
        try:
            if tab_index < len(self.driver.window_handles):
                self.driver.switch_to.window(self.driver.window_handles[tab_index])
                print(f"Switched to tab at index {tab_index}")
            else:
                print(f"No tab exists at index {tab_index}")
        except Exception as e:
            print(f"Failed to switch to tab: {e}")

    def close_current_tab(self):
        # Zamknij aktualną kartę
        self.driver.close()
        # Przełącz się z powrotem na oryginalną kartę
        self.switch_to_tab(0)  # Załóżmy, że 0 to oryginalna karta

    def switch_to_tab_by_title(driver, expected_title):
        # Pobierz uchwyty wszystkich otwartych kart
        window_handles = driver.window_handles

        for handle in window_handles:
            # Przełącz na kolejną kartę
            driver.switch_to.window(handle)
            # Pobierz tytuł aktualnej karty
            if driver.title == expected_title:
                print(f"Switched to the tab with title: {expected_title}")
                return
        print(f"Tab with title '{expected_title}' not found.")

        # Metoda zamykająca bieżącą kartę
    def close_tab(self):
        self.driver.close()

        # Metoda przełączająca się na kartę o podanym indeksie
    def switch_to_tab(self, index):
        window_handles = self.driver.window_handles
        if index < len(window_handles):
            self.driver.switch_to.window(window_handles[index])
        else:
            raise IndexError(f"Nie ma karty o indeksie {index}. Dostępne indeksy: 0 - {len(window_handles) - 1}")

    def scroll_to_element(self, by, value):
        element = self.driver.find_element(by, value)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)  # Dodaj krótkie opóźnienie, aby upewnić się, że element został przewinięty

    def ctrl_click_element(driver, element):
        """Kliknij element z użyciem klawisza Ctrl, aby otworzyć link w nowej karcie"""
        action_chains = ActionChains(driver)

        # Przytrzymaj klawisz Ctrl i kliknij element
        action_chains.key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()

    def scroll_to_bottom(self):
        # Użycie JavaScript do przewinięcia strony na dół
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


