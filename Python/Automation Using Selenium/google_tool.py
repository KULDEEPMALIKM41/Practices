import os
import time
import requests
from bs4 import BeautifulSoup
# import shutil
from selenium import webdriver
from datetime import datetime
from requests.adapters import HTTPAdapter
from PIL import Image
from io import BytesIO
# import base64

# wait or sleep in seconds
Wait_1 = 3
Wait_2 = 5
Wait_3 = 10
Wait_4 = 20
Wait_5 = 35
unique_folder = datetime.now()

def tf_get_proxy():
    # proxies = set()
    proxy_list = list()
    try:
        url = "https://free-proxy-list.net/"
        adapter = HTTPAdapter(max_retries=2)

        request_session = requests.Session()
        request_session.mount(url, adapter)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        r = requests.get(url, headers=headers, verify=False, timeout=5)
        soup = BeautifulSoup(r.content, 'html.parser')
        proxy_data = soup.select('td:nth-child(2) , td:nth-child(1)')
        for i in range(0, 20, 2):
            proxy_list.append(str(proxy_data[i].text) + ':' + str(proxy_data[i + 1].text))
        # proxy = str(proxy_data[i].text) + ':' + str(proxy_data[i + 1].text)
        # proxies.add(proxy)
        return proxy_list
    except Exception as e:
        print(" --->", e)
        pass

def tf_proxy_driver(PROXIES):
    Chrome_path = 'chromedriver'
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('--window-position=0,0')
    options.add_argument('--disable-infobars')
    options.add_argument('--window-size=1920,1080')
    pxy = ''
    # if PROXIES:
    #     pxy = PROXIES[-1]
    # else:
    #     print("--- Proxies used up (%s)" % len(PROXIES))
    # options.add_argument('--proxy-server=%s' % pxy)
    Chromedriver = webdriver.Chrome(Chrome_path, chrome_options=options)
    Chromedriver.implicitly_wait(Wait_3)
    print("proxy is - ", pxy)
    return Chromedriver

def tf_To_url():
    # url= 'https://www.google.com/search?q=kuldeep+mali+apc+college'
    url= 'https://www.google.com/search?q=narendra+modi                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          +hd+pic'
    return url

def tf_Click_images(Chromedriver):
    duck_duck_bar = Chromedriver.find_element_by_id("hdtb-msb-vis")
    choose_image_option = duck_duck_bar.find_element_by_link_text("Images")
    choose_image_option.click()
    time.sleep(Wait_2)
        
def tf_check_folder_path(new_folder_create=""):
    path = os.getcwd()
    path = path + "/" + "Google_Tool_Output"
    # path = "/home/rails/projects/django_projects/shane/source_page_screen_shot"
    path = path + "/" + str(unique_folder).replace(':','.')
    if new_folder_create != "":
        path = path + "/" + str(new_folder_create)
    os.makedirs(path)
    return path

def tf_screen_shots(driver, scroll_delay=1):
    path = tf_check_folder_path("screenshot")
    title = driver.title
    if title != "":
        title_length = len(str(title))
        if title_length > 26:
            title = title.replace("@", "").replace("/", "").replace("$", "").replace(".", "").replace(":","").replace(
                "|", "").replace(" ", "_")
            title = str(title)[0:25]
    else:
        title = driver.current_url
        title = title.replace("@","").replace("/","").replace("$","").replace(".","").replace(":","").replace("|","").replace(" ", "_")

    file_name = path +"/"+ title + ".png"
    device_pixel_ratio = driver.execute_script('return window.devicePixelRatio')
    total_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    viewport_height = driver.execute_script('return window.innerHeight')
    total_width = driver.execute_script('return document.body.offsetWidth')
    viewport_width = driver.execute_script("return document.body.clientWidth")

    # this implementation assume (viewport_width == total_width)
    assert (viewport_width == total_width)

    # scroll the page, take screenshots and save screenshots to slices
    offset = 0  # height
    slices = {}

    while offset < total_height:
        if offset + viewport_height > total_height:
            offset = total_height - viewport_height

        driver.execute_script('window.scrollTo({0}, {1})'.format(0, offset))
        time.sleep(scroll_delay)

        img = Image.open(BytesIO(driver.get_screenshot_as_png()))
        slices[offset] = img

        offset = offset + viewport_height
        if total_height < 20000:
            update_total_height = driver.execute_script('return document.body.parentNode.scrollHeight')
            if total_height != update_total_height:
                total_height = update_total_height
    # combine image slices
    stitched_image = Image.new('RGB', (total_width * device_pixel_ratio, total_height * device_pixel_ratio))
    for offset, image in slices.items():
        stitched_image.paste(image, (0, offset * device_pixel_ratio))
    stitched_image.save(file_name)
    driver.execute_script('window.scrollTo({0}, {1})'.format(0, 0))

def tf_source_code(driver):
    path = tf_check_folder_path("sourcepage")
    title = driver.title
    if title != "":
        title_length = len(str(title))
        if title_length > 26:
            title = title.replace("@", "").replace("/", "").replace("$", "").replace(".", "").replace(":","").replace("|", "").replace(" ", "_")
            title = str(title)[0:25]
        else:
            title = title.replace("@", "").replace("/", "").replace("$", "").replace(".", "").replace(":",
                                                                                                      "").replace(
                "|", "").replace(" ", "_")
    else:
        title = driver.current_url
        title = title.replace("@","").replace("/","").replace("$","").replace(".","").replace(":","").replace("|","").replace(" ", "_")

    tf_File_name = path + "/" + title + ".html"
    pagesource = driver.page_source.encode('ascii', 'ignore')
    soup = BeautifulSoup(pagesource, 'html.parser')
    # Create text file, then write page source to the file
    fh = open(tf_File_name, 'w')
    fh.write(str(soup.prettify()))
    fh.close()

def tf_download_images(dirname, links):
    length = len(links)
    # for index, url in enumerate(links):
    #     try:
    #         index_start = index + 1
    #         print('Downloading {0} of {1} images'.format(index_start, length))
    #         response = requests.get(url, stream=True)
    #         with open('{dirname}/img_{suffix}.jpg'.format(dirname=dirname, suffix=index_start), 'wb') as out_file:
    #             shutil.copyfileobj(image.raw, out_file)
    #         del response
    #     except Exception as e:
    #         print(e)
    #         pass
    skip = 0
    for index, data in enumerate(links):
        try:
            # imgdata = base64.b64decode(data.replace('data:image/jpeg;base64,',''))
            print('{} Image Downloaded out of {}'.format(index+1,length))
            filename = dirname+'/image'+str(index)+'.jpg' 
            with open(filename, 'wb') as f:
                    f.write(data)
        except Exception as e:
            print(e)
            skip += 1
    print('Skiped images : '+str(skip))
def tf_Get_source_page_for_image(Chromedriver):
    image_collection = []
    # div_select_for_image_collections = Chromedriver.find_element_by_xpath("//div[@class='tile-wrap']")
    div_select_for_image_collections = Chromedriver.find_element_by_id("islrg")
    image_collections = div_select_for_image_collections.find_elements_by_tag_name("img")
    for image_tag in image_collections:
        image = ''
        try:
            image = image_tag.screenshot_as_png
        except Exception as e:
            print(e)
            pass
        image_collection.append(image)
    image_path = tf_check_folder_path('Images')
    ## download top ten images url
    # top_ten_url = image_collection[0:10]
    tf_download_images(image_path, image_collection)

def main():
    ALL_PROXIES = tf_get_proxy()
    Chromedriver = tf_proxy_driver(ALL_PROXIES)
    running = True
    while running:
        try:
            Chromedriver.get(tf_To_url())
            if 'This site can’t be reached' not in Chromedriver.page_source and 'Your connection was interrupted' not in Chromedriver.page_source:
                tf_Click_images(Chromedriver)
                tf_screen_shots(Chromedriver)
                tf_source_code(Chromedriver)
                tf_Get_source_page_for_image(Chromedriver)
                Chromedriver.quit()   
                running = False 
            else:
                try:
                    Chromedriver.quit()
                except:
                    pass
                new = ""
                try:
                    new = ALL_PROXIES.pop()
                except Exception as e:
                    ALL_PROXIES = tf_get_proxy()
                # reassign driver if fail to switch proxy
                Chromedriver = tf_proxy_driver(ALL_PROXIES)
                print("--- Switched proxy to: %s" % new)
                time.sleep(1)
        except Exception as e:
            running = False 
            try:
                Chromedriver.quit()
            except:
                pass
            print(e)

if __name__ == "__main__":
    main()