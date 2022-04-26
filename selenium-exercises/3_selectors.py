from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://google.com")

# driver.maximize_window()
#
# window_title = driver.title  # moshahede title safhe
# print(window_title)
#
# driver.find_element('name', 'q').send_keys('wikipedia')
# driver.find_element('name', 'q').send_keys(Keys.ENTER)
#
# sleep(1)
# driver.back()
# sleep(1)
# driver.forward()
# sleep(1)
# driver.refresh()
# sleep(1)
#
# # **************Browser Action 2 => Open new window & switch to it**************************
# # اگر یک ویندو ۳ تا تب داشته باشه میگن ۳تا هنندل داره
#
# driver.switch_to.new_window('tab')
# sleep(1)
# driver.switch_to.new_window('window')
# driver.get('http://yahoo.com')
# sleep(1)
#
# print("all handles: " + str(driver.window_handles))
# print("current handle: " + str(driver.current_window_handle))
#
# driver.switch_to.window(driver.window_handles[0])
# sleep(1)
# driver.switch_to.window(driver.window_handles[1])
# sleep(1)
# driver.close()
# sleep(1)
#
# # **************Browser Action 3 => Change Window size**************************
#
# window_size = driver.get_window_size(driver.current_window_handle)  # {'width': 945, 'height': 1020}
#
# driver.set_window_size(800, 600)
# assert driver.get_window_size()['width'] == 800
#
# # **************Browser Action 3 => Change Window position **************************
#
# current_position = driver.get_window_position()  # {'x': 10, 'y': 10}
#
# driver.set_window_position(100, 200)
# assert driver.get_window_position()['x'] == 100
#
# # **************Browser Action 3 => Change Window status **************************
# driver.maximize_window()
# sleep(1)
# driver.fullscreen_window()
# sleep(1)
# driver.fullscreen_window()
# sleep(1)
# # ******************************************

driver.quit()
