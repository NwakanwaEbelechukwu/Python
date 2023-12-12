Handling dynamic pop-up boxes with Selenium can sometimes be tricky because they might not be present in the HTML when the page initially loads. Here's a basic example using Python and Selenium to close a dynamic pop-up box that appears after a certain time:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace 'your_url' with the actual URL of the page with the dynamic pop-up
url = 'your_url'

# Replace 'your_driver_path' with the actual path to your WebDriver executable (e.g., chromedriver.exe)
driver_path = 'your_driver_path'

# Create a new instance of the Chrome driver (you can use other drivers like Firefox)
driver = webdriver.Chrome(executable_path=driver_path)

# Navigate to the URL
driver.get(url)

# Add a wait for the pop-up to appear (replace 'your_timeout' with the time it takes for the pop-up to appear)
timeout = 10
try:
    # Wait for an element to be present in the DOM
    pop_up_element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, 'your_popup_xpath'))
    )
    
    # Add any additional actions to handle the pop-up if needed
    # For example, you might click a close button:
    # close_button = driver.find_element(By.XPATH, 'your_close_button_xpath')
    # close_button.click()

except TimeoutException:
    print(f"No pop-up found within {timeout} seconds.")

# Continue with the rest of your script

# Close the browser
driver.quit()
```

Replace `'your_url'` with the actual URL of the page with the dynamic pop-up, `'your_driver_path'` with the actual path to your WebDriver executable, `'your_popup_xpath'` with the XPath of the pop-up element, and `'your_close_button_xpath'` with the XPath of the close button if needed.

This script uses `WebDriverWait` to wait for the pop-up element to be present in the DOM. If the pop-up appears within the specified timeout, you can add additional actions to handle it, such as clicking a close button or performing other actions to dismiss the pop-up.
