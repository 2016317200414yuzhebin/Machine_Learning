from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
import urllib.request
import uuid
 
def download_pic(url, name, path):
 
    if not os.path.exists(path):
        os.makedirs(path)
    res = urllib.request.urlopen(url, timeout = 3).read()
    with open(path + name +'.jpg', 'wb') as file:
        file.write(res)
        file.close()
 
def get_image_url(num, key_word):
 
    box = driver.find_element(By.XPATH, '//input[@class="gLFyf"]')
    box.send_keys(key_word)
    box.send_keys(Keys.ENTER)
    box = driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
 
    # scroll page
    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        new_height = driver.execute_script('return document.body.scrollHeight')
        if new_height == last_height:
            # Click to show more results
            try:
                box = driver.find_element(By.XPATH, '//*[@id="islmp"]/div/div/div/div/div[1]/div[2]/div[2]/input').click()
            except:
                break
        last_height = new_height
 
    image_urls = []
 
    for i in range(1, num):
        try:
            image = driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[' + str(i) + ']/a[1]/div[1]/img')
            # This option is to download the thumbnail
            # image_src = image.get_attribute("src")
            image.click() # Click to enlarge
            time.sleep(5) # waiting for dynamic loading
            # Get the url of the original image
            image_real = driver.find_element(By.XPATH, '//*[@id="Sva75c"]/div[2]/div[1]/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div[1]/a/img')
            image_url = image_real.get_attribute("src")
            image_urls.append(image_url)
            print(str(i) + ': ' + image_url)
        except Exception as e:
            print(str(i) + ': error ' + str(e))

    return image_urls
 
if __name__ == '__main__':
 
    # Create a parameter object to control whether chrome is opened in no interface mode
    ch_op = Options()
    # Set Google Chrome's page without visualization
    ch_op.add_argument('--headless')
    ch_op.add_argument('--disable-gpu')
 
    url = 'https://www.google.com/'
    service = Service('D:/chrome/chromedriver.exe')
    driver = webdriver.Chrome(service = service, options = ch_op)
    driver.get(url)
    driver.maximize_window()
 
    key_word = input('Please enter a keyword: ')
    num = int(input('Please enter the number of pictures to download: '))
    _path = '../Data/Download/'
 
    path = _path + key_word + '/'
    print('Getting image url...')
    image_urls = get_image_url(num, key_word)
    for index, url in enumerate(image_urls):
        try:
            print('The image ' + str(index) + ' is downloading...')
            download_pic(url, str(index), path)
        except Exception as e:
            print(e)
            print('Failed to download image ' + str(index))
            continue
    driver.quit()