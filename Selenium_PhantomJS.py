# Download PhantomJS: https://phantomjs.org/download.html
# Installing PhantomJS on Windows: https://testguild.com/how-to-install-phantomjs/

# pip install selenium
# $ brew install phantomjs

# example
from selenium import webdriver


driver = webdriver.PhantomJS()

driver.set_window_size(1120, 550)
driver.get("https://duckduckgo.com/")
driver.find_element_by_id('search_form_input_homepage').send_keys("cats")
driver.find_element_by_id("search_button_homepage").click()

print(driver.current_url)

driver.quit()


# same for Firefox
from selenium import webdriver


driver = webdriver.Firefox()

driver.get("https://duckduckgo.com/")
driver.find_element_by_id('search_form_input_homepage').send_keys("dogs")
driver.find_element_by_id("search_button_homepage").click()

# print(driver.current_url)
driver.quit()



