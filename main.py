# for single line comments and ''' for multi line comments
# by my knowledge, there are 3 main ways to scrape data from a website:
# 1. using requests and BeautifulSoup to get the HTML content of the page and parse it to extract the data
# 2. using Selenium to automate the browser and interact with the page to get the data (especially for dynamic content that is loaded with JavaScript)
# 3. using an API if the website provides one to get the data in a structured format (like JSON)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import time


LIMIT = 100

# ---------- browser ----------
options = webdriver.FirefoxOptions()
# options.add_argument("--headless")

driver = webdriver.Firefox(options=options)

wait = WebDriverWait(driver, 20)

driver.get("https://zipnet.delhipolice.gov.in/Victims/MissingPersons")

all_data = []

while True:
    wait.until(EC.invisibility_of_element_located(
        (By.ID, "missingPersonGrid_processing")
    ))

    dropdown = wait.until(EC.element_to_be_clickable(
        (By.NAME, "missingPersonGrid_length")
    ))
    Select(dropdown).select_by_value("50")
    # wait for REAL data rows
    wait.until(EC.invisibility_of_element_located(
        (By.ID, "missingPersonGrid_processing")
    ))
    wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "odd")
    ))
    
    table = driver.find_element(By.ID, "missingPersonGrid")
    # TODO  : click on the dropdown to show 50 records per page
    # TODO  : click on the next page button and repeat the process until we have almost all records

    # ranges = table.find_element(By.NAME, "missingPersonGrid_length")
    # ranges.click()
    # click on all the plus icons to expand the rows
    
    rows = table.find_elements(
        By.CSS_SELECTOR, ".fa.fa-plus-circle.fa-lg.justify-content-center"
    )

    for row in rows:
        row.click()

    # now we have all the data in the table, we can extract it
    rows_with_data = table.find_elements(By.CLASS_NAME,"row.mt-2")
    i = 1
    for row in rows_with_data:
        sub_titles = []
        val = []
        cells = row.find_elements(By.CLASS_NAME, "col-md-3.mb-2")
        for cell in cells:
            if i == 1:
                label = cell.find_element(By.TAG_NAME,"label")
                sub_titles.append(label.text)
                value = cell.find_element(By.TAG_NAME,"span")
                val.append(value.text)
            else:
                value = cell.find_element(By.TAG_NAME,"span")
                val.append(value.text)

        if len(sub_titles) > 0:
            all_data.append(sub_titles)
        i += 1
        all_data.append(val)
    time.sleep(2)
    
    # check if there is a next page button
    try:
        next_page = driver.find_element(By.LINK_TEXT, "Next")
        if next_page.is_enabled():
            next_page.click()
            wait.until(EC.invisibility_of_element_located((By.ID, "missingPersonGrid_processing")))
        else:
            pass
    except:
        pass

        # css selector can be used to select elements based on their class, id, attributes, etc.

        
        # how is it diff from By.CLASS_NAME, By.ID, etc.?
        # css selector is more powerful and flexible than By.CLASS_NAME, By.ID, etc. because it can select elements based on multiple criteria, 
        # while By.CLASS_NAME, By.ID, etc. can only select elements based on a single criterion. 
        # For example, you can use a css selector to select all elements with a certain class and a certain attribute value, 
        # while you cannot do this with By.CLASS_NAME or By.ID.