from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlencode
import os
import argparse
import time
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("--code",type=str, help="path to source code")
parser.add_argument("--theme",help="theme",default="monokai")

args = parser.parse_args()

print('File: ' + args.code)
f=open(args.code,'r')
code = f.read()
f.close()
theme = args.theme

params = {
    'bg': 'rgba(171, 184, 195, 1)',
    't': theme,
    'wt': 'none',
    'l': 'auto',
    'width': '680',
    'ds': 'true',
    'dsyoff': '20px',
    'dsblur': '68px',
    'wc': 'true',
    'wa': 'true',
    'pv': '56px',
    'ph': '56px',
    'ln': 'false',
    'fl': '1',
    'fm': 'Hack',
    'fs': '14px',
    'lh': '133%',
    'si': 'false',
    'es': '2x',
    'wm': 'false',
    'code': code
}

webdriver_path = 'G:\\x45\\chromedriver.exe'

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
  "download.default_directory": os.getcwd(),
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": False
})
chrome_options.add_argument("--log-level=3")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=webdriver_path,options=chrome_options)
url = 'https://carbon.now.sh/?' + urlencode(params)
driver.get(url)

if os.path.exists('carbon.png'):
    os.remove('carbon.png')

buttons = driver.find_elements('tag name','button')

for button in buttons:    
    if button.get_attribute('innerText').startswith('Quick'):
        button.click()

while True:
    print('.')
    if os.path.exists('./carbon.png'):
        time.sleep(3)
        break
    time.sleep(1)

shutil.copyfile('./carbon.png', args.code + '.png')
os.remove('./carbon.png')

driver.quit()
exit(0)