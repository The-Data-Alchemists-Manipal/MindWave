from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
import pandas as pd
import pyautogui

# Creating Web Driver using Firefox or Chrome
def create_driver():
    driver = None
    try:
        # Configuring Firefox options
        firefox_options = FirefoxOptions()
        firefox_options.add_argument('--no-sandbox')
        firefox_options.add_argument('--disable-dev-shm-usage')
        firefox_options.set_preference("extensions.enabledScopes", False)
        # creating webdriver object with Firefox options
        driver = webdriver.Firefox(options=firefox_options)
    except:
        try:
            # Configuring Chrome options
            chrome_options = ChromeOptions()
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-extensions')
            driver = webdriver.Chrome(options=chrome_options)
        except:
            raise Exception('No supported browser found.')

    # Close any existing driver instances
    if len(webdriver.Chrome().window_handles) > 1:
        driver.quit()

    return driver

# Terminating WebDriver
def close_driver(driver):
    try:
        if len(driver.window_handles) > 0:
            driver.close()
        driver.quit()
    except:
        raise Exception('Unable to close webdriver')

# Scraping Query search pages from Google Search
def search_queries(driver, queries):
    results = []
    for query in queries:
        driver.get(f'https://www.google.com/search?q={query}')

        # Wait for up to 10 seconds for all elements located by the XPath expression to be present on the page
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="yuRUbf"]/a')))
        time.sleep(0.5)

        # Add mouse movement to make automation less detectable
        x, y = pyautogui.position()
        pyautogui.moveTo(x+500, y+500, duration=0.5)
        pyautogui.moveTo(x - 10, y - 10, duration=0.5)

        links = driver.find_elements(By.XPATH, '//div[@class="yuRUbf"]/a')

        for link in links:
            results.append({
                'query': query,
                'source_link': link.get_attribute('href')
            })

    return results

# Main Program Execution
driver = create_driver()
queries = ['webhosting','ai books','webscraping']

# Calling Function to scrape Data of Query Searches from Google Search
results = search_queries(driver, queries)
print(f'Results found: {len(results)}')
close_driver(driver)

#Converting data into Pandas dataframe
if len(results)>0:
    df = pd.DataFrame(results)
    # saving the dataframe into excel file
    #df.to_excel('search_results.xlsx', index=False)
    print(df)
else:
    # If no "search results" found then handling it here
    print("No Search Results Found")
