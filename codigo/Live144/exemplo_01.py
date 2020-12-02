from appium.webdriver import Remote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


driver = Remote(
    'http://localhost:4723/wd/hub',
    {"app": "/root/tmp/app2.apk",
     "platformName": "android"}
)

wait = WebDriverWait(driver, 10)

text_views = '//android.widget.TextView'
batata = '//android.widget.EditText'
btn = '//android.widget.Button'


# sleep(5)  # Wait

wait.until(
    EC.presence_of_element_located((By.XPATH, text_views))
)

for text in driver.find_elements_by_xpath(text_views):
    print(text.text)

bat = driver.find_element_by_xpath(batata)
print(bat.text)
bat.send_keys('frita')
but = driver.find_element_by_xpath(btn)
print(but.text)
but.click()

wait.until(
    EC.presence_of_element_located((By.XPATH, text_views))
)

but = driver.find_element_by_xpath(btn)
print(but.text)
but.click()


driver.quit()
