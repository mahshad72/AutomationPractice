from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os  # برای کارکردن و عملیات مرتبط با سیستم عامل هست
from pathlib import \
    Path  # میاد برای ما آدرسی که میخوایمو میسازه و از طریق os میاد اسمی که میخوایمو جوین میکنه به path ما
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()  # اینجا قبل از اینکه درایور رو تعریف کنیم باید مشخص کنیم اینستنس درایور با چه آپشن هایی باید از کلاس درایور ساخته بشه
chrome_options.add_argument("--incognito")  # https://peter.sh/experiments/chromium-command-line-switches/
# یه آپشنن دیگه هم پاریم  که بهش میگن هدلس. یعنی کروم به صورت ویژوال برای ما باز نمیشه. برای جاهایی که مثلا رم کمی داریم خیلی به درد میخوره. در این حالت کروم در بک گروند پروسسش انجام میشه
chrome_options.add_argument("--headless")  # https://peter.sh/experiments/chromium-command-line-switches/

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options)

driver.get("http://digikala.com")
sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)

current_path = Path(
    __file__).parent  # چون نوشتیم parent میاد آدرس فولدر automationpractice رو میده. اگه نمینوشتیم تا js_test.py میومد جلو

print(type(current_path))
file_name = os.path.join(str(current_path), 'scrollSS.png')
print(type(file_name))
print(current_path)
driver.save_screenshot(file_name)
driver.quit()
