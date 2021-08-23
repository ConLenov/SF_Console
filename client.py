from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def out_red(text):
    print("\033[38;5;196m {}" .format(text))
def out_orange(text):
    print("\033[38;5;202m {}" .format(text))
def out_yellow(text):
    print("\033[38;5;226m {}" .format(text))
def out_green(text):
    print("\033[38;5;46m {}".format(text))
def out_aqua(text):
    print("\033[38;5;45m {}" .format(text))
def out_blue(text):
    print("\033[38;5;20m {}".format(text))
def out_violet(text):
    print("\033[38;5;201m {}".format(text))
def out_white(text):
    print("\033[37m {}".format(text))

out_red(" ::::::::  ::::::::::           ::::::::   ::::::::  ::::    :::  ::::::::   ::::::::  :::        ::::::::::")
out_orange(":+:    :+: :+:                 :+:    :+: :+:    :+: :+:+:   :+: :+:    :+: :+:    :+: :+:        :+:       ")
out_yellow("+:+        +:+                 +:+        +:+    +:+ :+:+:+  +:+ +:+        +:+    +:+ +:+        +:+       ")
out_green("+#++:++#++ :#::+::#            +#+        +#+    +:+ +#+ +:+ +#+ +#++:++#++ +#+    +:+ +#+        +#++:++#  ")
out_aqua("       +#+ +#+                 +#+        +#+    +#+ +#+  +#+#+#        +#+ +#+    +#+ +#+        +#+       ")
out_blue("#+#    #+# #+#                 #+#    #+# #+#    #+# #+#   #+#+# #+#    #+# #+#    #+# #+#        #+#       ")
out_violet(" ########  ###       ########## ########   ########  ###    ####  ########   ########  ########## ##########")
out_white("")

video_link = input('[+] INPUT LINK: ')

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(
    ChromeDriverManager().install(),
    options=options,
)

driver.get('https://ru.savefrom.net/7/')
driver.find_element_by_id('sf_url').send_keys(video_link)
driver.find_element_by_id('sf_submit').click()
element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "link-download")))
print(f"[+] DOWNLOAD: {element.get_attribute('href')}")
driver.quit()
