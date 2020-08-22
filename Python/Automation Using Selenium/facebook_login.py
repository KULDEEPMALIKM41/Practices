import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from requests.adapters import HTTPAdapter
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = 'your-facebook-username'
PASSWORD = 'your-facebook-password'

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
    pxy = ''
    # if PROXIES:
    #     pxy = PROXIES[-1]
    # else:
    #     print("--- Proxies used up (%s)" % len(PROXIES))
    # options.add_argument('--proxy-server=%s' % pxy)
    Chromedriver = webdriver.Chrome(Chrome_path, chrome_options=options)
    print("proxy is - ", pxy)
    return Chromedriver

#To url
def tf_To_url():
    url= 'https://mbasic.facebook.com/'
    return url

def tf_scroll_fb(Chromedriver):
    try:
        WebDriverWait(Chromedriver, 30).until(
            EC.presence_of_element_located((By.ID, "mbasic_logout_button"))
        )
    except Exception as e:
        print(e)
    # device_pixel_ratio = Chromedriver.execute_script('return window.devicePixelRatio')
    total_height = Chromedriver.execute_script('return document.body.parentNode.scrollHeight')
    viewport_height = Chromedriver.execute_script('return window.innerHeight')/2
    total_width = Chromedriver.execute_script('return document.body.offsetWidth')
    viewport_width = Chromedriver.execute_script("return document.body.clientWidth")
    
    # this implementation assume (viewport_width == total_width)
    assert (viewport_width == total_width)

    offset = 0  # height
    while offset < total_height:
        if offset + viewport_height > total_height:
            offset = total_height - viewport_height
        Chromedriver.execute_script('window.scrollTo({0}, {1})'.format(0, offset))
        time.sleep(2)
        offset = offset + viewport_height
    Chromedriver.execute_script('window.scrollTo({0}, {1})'.format(0, 0))

def tf_fb_login(Chromedriver):
    try:
        try:
            WebDriverWait(Chromedriver, 30).until(
                EC.presence_of_element_located((By.NAME, "login"))
            )
        except Exception as e:
            print(e)
        Chromedriver.find_element_by_id("m_login_email").send_keys(USERNAME)
        Chromedriver.find_element_by_name("pass").send_keys(PASSWORD)
        Chromedriver.find_element_by_name("login").click()
        try:
            Chromedriver.find_element_by_css_selector("input[type='submit']").click()
        except:
            pass

        # account varification
        try:
            Chromedriver.find_element_by_id("mbasic_logout_button")
        except:
            Chromedriver.find_element_by_css_selector("input[type='submit']").click()
        tf_scroll_fb(Chromedriver)
    except Exception as e:
        print("Try method second", e)

def tf_overview_visit_fb(Chromedriver):
    # menu_list = ['Profile','Edit Profile','Messages','Notifications','Chat','Find Friends','Groups','COVID-19','Menu','Home']
    # for menu in menu_list:
    #     try:
    #         header = Chromedriver.find_element_by_id("header")
    #         header.find_element_by_link_text(menu).click()
    #         tf_scroll_fb(Chromedriver)
    #     except Exception as e:
    #         print(e)
    header = Chromedriver.find_element_by_id("header")
    elems = header.find_elements_by_tag_name('a')
    i = 0
    while i<len(elems):
        try:
            header = Chromedriver.find_element_by_id("header")
            elems = header.find_elements_by_tag_name('a')
            elems[i+2].click()
            tf_scroll_fb(Chromedriver)
        except:
            pass
        i+=1

def tf_fb_logout(Chromedriver):
    try:
        Chromedriver.find_element_by_id("mbasic_logout_button").click()
    except:
        pass
    
#--- YOU ONLY NEED TO CARE FROM THIS LINE ---
# creating new driver to use proxy
def main():
    ALL_PROXIES = tf_get_proxy()
    Chromedriver = tf_proxy_driver(ALL_PROXIES)
    running = True
    while running:
        try:
            Chromedriver.get(tf_To_url())
            if 'This site can’t be reached' not in Chromedriver.page_source and 'Your connection was interrupted' not in Chromedriver.page_source:
                tf_fb_login(Chromedriver)
                tf_overview_visit_fb(Chromedriver)
                tf_fb_logout(Chromedriver)
                time.sleep(2)
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