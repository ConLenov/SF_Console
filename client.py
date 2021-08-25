from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

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
print()

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)

driver.get("https://ru.savefrom.net/7/")

driver.find_element_by_id('sf_url').send_keys(video_link)
driver.find_element_by_id('sf_submit').click()

time.sleep(35)

element = driver.find_element_by_class_name('link-download')
print(f"[+] DOWNLOAD: {element.get_attribute('href')}")

driver.quit()
