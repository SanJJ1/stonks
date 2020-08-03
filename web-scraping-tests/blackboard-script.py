from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def wait_until_load(element_wait_for_load):
    def link_has_gone_stale():
        try:
            # poll the link with an arbitrary call
            exec(element_wait_for_load)
            return False
        except Exception as e:
            return True

    while link_has_gone_stale():
        time.sleep(.1)
        pass


browser = webdriver.Firefox(executable_path=r'geckodriver.exe')

url = 'https://courses.cscc.edu/webapps/login/'
browser.get(url)

# login page click
browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/div/p[3]/a').click()

# login to blackboard
user = 'sjanardhan'
pw = 'Krisna3227'
browser.find_element_by_css_selector("#userNameInput").send_keys(user)
browser.find_element_by_css_selector("#passwordInput").send_keys(pw)

# Submit login info
browser.find_element_by_css_selector("#submitButton").click()

# wait until blackboard page loads and clicks course Multivar
wait_until_load('browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div[2]/div/div/div/div[4]/div[1]/div[2]/div/div/ul/li[1]/a")')
browser.find_element_by_xpath(
    "/html/body/div[5]/div/div/div[2]/div[2]/div/div/div/div[4]/div[1]/div[2]/div/div/ul/li[1]/a").click()

# Click Lectures and Notes button on sidebar
browser.find_element_by_xpath("/html/body/div[5]/div[2]/nav/div/div[2]/div/div[2]/ul/li[6]/a/span").click()

# Find the link and title for resource and try downloading the pdf for it.
base_url = 'https://courses.cscc.edu/'


def check_element(element):
    try:
        # poll the link with an arbitrary call
        exec(element)
        return True
    except Exception as e:
        return False


# Creates a loop that continues as long as the element exists.
i = 1
while check_element(f'browser.find_element_by_xpath(f"/html/body/div[5]/div[2]/div/div/div/div/div[2]/ul/li[{i}]")'):
    list_element = browser.find_element_by_xpath(f"/html/body/div[5]/div[2]/div/div/div/div/div[2]/ul/li[{i}]")
    try:
        list_element_name = list_element.find_element_by_xpath('.//div[1]/h3/a/span').get_attribute('innerHTML')
        list_element_link = list_element.find_element_by_xpath('.//div[1]/h3/a').get_attribute('href')
        print(list_element_name, list_element_link)
    except Exception as e:
         pass
    i+=1

"""
/html/body/div[5]/div[2]/div/div/div/div/div[2]/ul/li[1]/div[1]/h3/a

/html/body/div[5]/div[2]/div/div/div/div/div[2]/ul/li[1]/div[1]/h3/a/span
/html/body/div[5]/div[2]/div/div/div/div/div[2]/ul/li[2]/div[1]/h3/a/span
/html/body/div[5]/div[2]/div/div/div/div/div[2]/ul/li[3]/div[1]/h3/a/span
/html/body/div[5]/div[2]/div/div/div/div/div[2]/ul/li[4]/div[2]/div[1]/div[2]/ul/li/a
/html/body/div[5]/div[2]/div/div/div/div/div[2]/ul/li[5]/div[1]/h3/a/span
/html/body/div[5]/div[2]/div/div/div/div/div[2]/ul/li[6]/div[2]/div[1]/div[2]/ul/li/a
"""

x = input('Type here to exit:  ')
browser.quit()
