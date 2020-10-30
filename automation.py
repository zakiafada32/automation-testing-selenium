from selenium import webdriver

chrome_browser = webdriver.Chrome("./chromedriver.exe")

# chrome_browser.maximize_window()
chrome_browser.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

assert "Selenium Easy Demo" in chrome_browser.title
assert "Show Message" in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id("user-message")
user_message.clear()
user_message.send_keys("automation testing")

show_message_button = chrome_browser.find_elements_by_class_name("btn-default")
# print(show_message_button[0].get_attribute("innerHTML"))
show_message_button[0].click()
output_message = chrome_browser.find_element_by_id("display")
assert "automation testing" in output_message.text

chrome_browser.close()
