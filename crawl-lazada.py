from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Open the Lazada website
driver.get("https://www.lazada.vn")

# Find the search input element by ID
search_box = driver.find_element(By.ID, "q")

# Perform a search
search_box.send_keys("laptop")
search_box.send_keys(Keys.RETURN)

# Wait for the results to load
driver.implicitly_wait(5)

# Extract and print the titles and prices of the search results
product_names = driver.find_elements(By.CSS_SELECTOR, '.RfADt > a')
product_prices = driver.find_elements(By.CSS_SELECTOR, '.aBrP0 > .ooOxS')

# Open the SQL file in write mode
with open('data.sql', 'w', encoding="utf-8") as file:
    # Write the CREATE TABLE statement
    file.write('''CREATE TABLE IF NOT EXISTS users (
        product_name TEXT NOT NULL,
        product_price TEXT NOT NULL
    );
    ''')

    # Write INSERT INTO statements for each product
    for name, price in zip(product_names, product_prices):
        file.write(f"INSERT INTO users VALUES ('{name.text}', '{price.text}');\n")

# Close the browser
driver.quit()