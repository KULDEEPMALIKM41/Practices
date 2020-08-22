from bs4 import BeautifulSoup
# from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os, json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor

def call_selenium_method(url):
    try:
        docs = None
        filepath = os.path.dirname(__file__)
        chrome_path = filepath + "/chromedriver"
        capa = DesiredCapabilities.CHROME
        capa["pageLoadStrategy"] = "none"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-infobars")
        # display = Display(visible=0, size=(950, 650))
        # display.start()
        driver = webdriver.Chrome(chrome_path, desired_capabilities=capa, chrome_options=chrome_options)

        driver.get("https://www.giftofspeed.com")
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "testing1"))
            )
        except Exception as e:
            print(e)
        driver.find_element_by_id("testing1").send_keys(url)
        driver.find_element_by_id("testing2").click()
        try:
            WebDriverWait(driver, 180).until(
                EC.presence_of_element_located((By.ID, "accordion"))
            )
        except Exception as e:
            print(e)

        try:
            driver.find_element_by_id("oshowmore").click()
        except Exception as e:
            print(e)
        try:
            driver.find_element_by_id("otshowmore").click()
        except Exception as e:
            print(e)
        try:
            eb = driver.find_elements_by_class_name("panel-group")
            for webElement in eb:
                webElement.click()

        except Exception as e:
            print(e)
        docs = driver.page_source
        driver.quit()
        return docs
    except Exception as e:
        print(e)
        return None

class WebPerformanceInfo:
    def __init__(self,domain_name):
        self.response_doc = call_selenium_method(domain_name)

    def Web_Performance_data(self):
        try:
            soup = BeautifulSoup(self.response_doc, 'html.parser')
            parserObj = Performance_parser(soup)
            json_data = {}
            json_data['status'] = 200
            json_data['data'] = parserObj.getData()
            print("Task done for website performance section.")
            return json_data
        except Exception as e:
            json_data = {}
            json_data['status'] = 500
            json_data['data'] = print(e)
            print("Having issue on website performance section --->", e)
            return json_data



class Performance_parser:
    def __init__(self,soup):
        self.overalldata = {}
        try:
            def Main_First():
                print("Start ThreadPoolExecutor for website performance section.")
                with ThreadPoolExecutor(max_workers=8) as executor:
                    executor.submit(self.headerInfo, soup)
                    executor.submit(self.requestWaterfall, soup)
                    executor.submit(self.sizeBreakdown, soup)
                    executor.submit(self.requestBreakdown, soup)
                    executor.submit(self.slowestLocalResources, soup)
                    executor.submit(self.slowestExternalResources, soup)
                    executor.submit(self.requestWaterfallFooter, soup)
                    executor.submit(self.performance, soup)
            Main_First()
        except Exception as e:
            print(e)

    # header_info
    def headerInfo(self,soup):
        try:
            header_info = {}
            headerTemp = []
            tags = soup.find_all("div", {'class': ['text-center']})
            for element in tags:
                headerTemp.append(element.text)
            if "requests" in headerTemp[0].lower():
                header_info.update({"requests": headerTemp[9]})
            if "total size" in headerTemp[1].lower():
                header_info.update({"total_size": headerTemp[10]})
            if "content" in headerTemp[2].lower():
                header_info.update({"content_visible_note": headerTemp[2]})
                header_info.update({"content_visible": headerTemp[11]})
            if "fully loaded" in headerTemp[3].lower():
                header_info.update({"fully_loaded": headerTemp[12]})
            if "optim" in headerTemp[4].lower():
                header_info.update({"optim_score_note": headerTemp[4]})
                header_info.update({"optim_score": headerTemp[13]})
            del headerTemp
            self.overalldata.update({"header_info" : header_info})
        except Exception as e:
            header_info = {}
            self.overalldata.update({"header_info": header_info})
            print(e)

    # request_waterfall
    def requestWaterfall(self,soup):
        try:
            request_waterfall = []
            tags = soup.find_all("div", {'class': ['expandable']})
            for element in tags:
                link, reference, size = "", "", ""
                if element != None:
                    anchor_div = element.find("div", {'class': ['timel1']})
                    if anchor_div != None:
                        anchor = anchor_div.find("a")
                        if anchor != None:
                            link = anchor.get("href")
                    reference_div = element.find("div", {'class': ['timel2']})
                    if reference_div != None:
                        span = reference_div.find("span")
                        if span != None:
                            reference = span.text
                    size_div = element.find("div", {'class': ['timel3']})
                    if size_div != None:
                        span = size_div.find("span")
                        if span != None:
                            size = span.text
                    request_waterfall.append({"link": link, "reference": reference, "size": size})
            self.overalldata.update({"request_waterfall" : request_waterfall})
        except Exception as e:
            request_waterfall = []
            self.overalldata.update({"request_waterfall" : request_waterfall})
            print(e)

    # size_breakdown
    def sizeBreakdown(self,soup):
        try:
            size_breakdown = []
            table = soup.find("div", {'class': ['one-stack']})
            if table != None:
                table_body = table.find("tbody")
                table_row = table_body.find_all("tr")
                if table_row != None:
                    for row in table_row:
                        temp = []
                        table_data = row.find_all("span", {'class': ['breakdown1']})
                        if table_data != None:
                            for td in table_data:
                                data = td.text
                                if data != None and data != "":
                                    temp.append(data)
                        if len(temp) > 0:
                            size_breakdown.append(temp)
            self.overalldata.update({"size_breakdown" : size_breakdown})
        except Exception as e:
            size_breakdown = []
            self.overalldata.update({"size_breakdown" : size_breakdown})
            print(e)

    # request_breakdown
    def requestBreakdown(self,soup):
        try:
            request_breakdown = []
            table = soup.find("div", {'class': ['two-stack']})
            if table != None:
                table_body = table.find("tbody")
                table_row = table_body.find_all("tr")
                if table_row != None:
                    for row in table_row:
                        temp = []
                        table_data = row.find_all("span", {'class': ['breakdown1']})
                        if table_data != None:
                            for td in table_data:
                                data = td.text
                                if data != None and data != "":
                                    temp.append(data)
                        if len(temp) > 0:
                            request_breakdown.append(temp)
            self.overalldata.update({"request_breakdown" : request_breakdown})
        except Exception as e:
            request_breakdown = []
            self.overalldata.update({"request_breakdown" : request_breakdown})
            print(e)

    # slowest_local_resources
    def slowestLocalResources(self,soup):
        try:
            slowest_local_resources = []
            table = soup.find("table", {'id': ['tlocal']})
            if table != None:
                table_body = table.find("tbody")
                if table_body != None:
                    table_row = table_body.find_all("tr")
                    if table_row != None:
                        for row in table_row:
                            temp = []
                            anchor = row.find("a")
                            sec_tag = row.find("span", {'class': ['breakdown1']})
                            if anchor != None and sec_tag != None:
                                url = anchor.get("href")
                                sec = sec_tag.text
                                if url != None and sec != None:
                                    sec = sec.strip()
                                    temp = [url, sec]
                            if len(temp) > 0:
                                slowest_local_resources.append(temp)
            self.overalldata.update({"slowest_local_resources" : slowest_local_resources})
        except Exception as e:
            slowest_local_resources = []
            self.overalldata.update({"slowest_local_resources" : slowest_local_resources})
            print(e)

    # slowest_external_resources
    def slowestExternalResources(self,soup):
        try:
            slowest_external_resources = []
            table = soup.select(".row+ .row .urlbreak a , .row+ .row .breakdown1")
            if table != None:
                for i in range(1, len(table), 2):
                    temp = []
                    url = table[i - 1].get("href")
                    sec = table[i].text
                    if url != None and sec != None:
                        sec = sec.strip()
                        temp = [url, sec]
                    if len(temp) > 0:
                        slowest_external_resources.append(temp)
            self.overalldata.update({"slowest_external_resources" : slowest_external_resources})
        except Exception as e:
            slowest_external_resources = []
            self.overalldata.update({"slowest_external_resources" : slowest_external_resources})
            print(e)

    # request_waterfall_footer
    def requestWaterfallFooter(self,soup):
        try:
            request_waterfall_footer = {}
            footer_row = soup.select_one("#results .center-block .row-n")
            if footer_row != None:
                request_tag = footer_row.select_one(".timel1 h4")
                if request_tag != None:
                    request = request_tag.text
                    request_waterfall_footer.update({"request": request})
                size_tag = footer_row.select_one(".timel3 h4")
                if size_tag != None:
                    size = size_tag.text
                    request_waterfall_footer.update({"size": size})
                time_tag = footer_row.select_one(".timel4 h4")
                if time_tag != None:
                    time = time_tag.text
                    request_waterfall_footer.update({"time": time})
            self.overalldata.update({"request_waterfall_footer" : request_waterfall_footer})
        except Exception as e:
            request_waterfall_footer = {}
            self.overalldata.update({"request_waterfall_footer" : request_waterfall_footer})
            print(e)

    # performance
    def performance(self,soup):
        try:
            performance = {}
            tags = soup.find_all("div", {"class": ["panel-group"]})
            for tag in tags:
                heading = None
                heading_tag = tag.select_one(".panel-title")
                if heading_tag != None:
                    heading = heading_tag.text
                    if heading != None:
                        heading = heading.strip()
                url_data_container = []
                li_tag_list = tag.select(".url_list li")
                if li_tag_list != None:
                    if len(li_tag_list) > 0:
                        for li_tag in li_tag_list:
                            url_tag_list = li_tag.find_all("span", {"class": ["urlbreak"]})
                            for url_tag in url_tag_list:
                                url = None
                                anchor = url_tag.find("a")
                                if anchor != None:
                                    if anchor.get("href") != None:
                                        url = anchor.get("href")
                                elif url_tag.text != None:
                                    url = url_tag.text
                                if url != None:
                                    url_data_container.append(url)
                            data = None
                            data_tag = li_tag.find("div", {"class": ["url_data"]})
                            if data_tag != None:
                                data = data_tag.text
                                if data != None:
                                    data = data.replace("∟", "@")
                            if data != None:
                                url_data_container.append(data)
                    else:
                        body_data = tag.select_one(".panel-body")
                        if body_data != None:
                            data = body_data.text
                            data = data.strip()
                            url_data_container.append(data)
                if heading != None:
                    performance.update({heading: url_data_container})
            self.overalldata.update({"performance" : performance})
        except Exception as e:
            performance = {}
            self.overalldata.update({"performance" : performance})
            print(e)

    def getData(self):
        return self.overalldata

web_per = WebPerformanceInfo('seo.com')
result_json = web_per.Web_Performance_data()
print(json.dumps(result_json,indent=4, sort_keys=True))