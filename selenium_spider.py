import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import random


User_Agent = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR "
    "2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center "
    "PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET "
    "CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR "
    "3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR "
    "2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; "
    ".NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) "
    "Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 "
    "Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 "
    "Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 "
    "TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 "
    "Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET "
    "CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 "
    "Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET "
    "CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET "
    "CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; "
    "360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET "
    "CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) "
    "Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 "
    "Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) "
    "Firefox/3.6.10 "
]
headers = {
    "User_Agent": random.choice(User_Agent),
}


# 打开 Chrome
driver = webdriver.Chrome()
driver.maximize_window()
#打开网址
url = 'http://mall.ckcest.cn/mall/list.html?typeId=1002'
driver.get(url)

# 搜索 
num=driver.window_handles
print('before',num)
# driver.find_element_by_class_name("sc-title").click()
driver.find_element_by_xpath('//*[@id="result-content"]/div[1]/h2/a').click()
# driver.maximize_window()
time.sleep(5)
num=driver.window_handles
print('after',num)
driver.switch_to_window(num[1])
table_heads_arr = []
table_heads_arr.append('标题：')
# table_heas_arr.append(title.replace("\n", ""))
# div1 = driver.find_element_by_class_name('selectorgadget_selected')
summary = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[1]/i')
print(summary.text)
table_head_str = str(summary.text)
table_heads_arr.append(table_head_str.replace("\n", ""))

keywords = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[2]/i')
print(keywords.text)
table_head_str = str(keywords.text)
table_heads_arr.append(table_head_str.replace("\n", ""))

doi = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[3]/i')
print(doi.text)
table_head_str = str(doi.text)
table_heads_arr.append(table_head_str.replace("\n", ""))

classification = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[5]/i')
print(classification.text)
table_head_str = str(classification.text)
table_heads_arr.append(table_head_str.replace("\n", ""))

author = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[6]/p[1]/i')
print(author.text)
table_head_str = str(author.text)
table_heads_arr.append(table_head_str.replace("\n", ""))

institution = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[7]/i')
print(institution.text)
table_head_str = str(institution.text)
table_heads_arr.append(table_head_str.replace("\n", ""))

journal = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[8]/i')
print(journal.text)
table_head_str = str(journal.text)
table_heads_arr.append(table_head_str.replace("\n", ""))

time_ = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[9]/i')
print(time_.text) 
table_head_str = str(time_.text)
table_heads_arr.append(table_head_str.replace("\n", ""))

issue = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[10]/span/i')
print(issue.text)
table_head_str = str(issue.text)
table_heads_arr.append(table_head_str.replace("\n", ""))

main_language = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[11]/i')
print(main_language.text)
table_head_str = str(main_language.text)
table_heads_arr.append(table_head_str.replace("\n", ""))

# currentPageUrl = str(driver.current_url)
# print(currentPageUrl)
table_heads_arr.append('url：')

print(table_heads_arr)
# # 根据行和列获取表格属性
# def getTableData(r, td):
#     td.clear()
#     td.append(table_heads_arr)
#     print(td)
#     # writer.writerow(td)

# 创建数据集写入的csv文件
i = 1
j = 1
k = 1
with open("test.csv", mode="w") as csvFile:
    writer = csv.writer(csvFile, dialect='unix')
    # 写入表头
    writer.writerow(table_heads_arr)
    while (j<1000000):
        while (i<11) :
            table_data = [] 
            time.sleep(random.random()%6 + 3)
            k = random.random()%3 + 1
            time.sleep(k)
            if len(driver.find_elements_by_xpath('/html/body/div[4]/div/div[1]/h4')) :
                title = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/h4').text
                print(title)
                table_data.append(title)
            else:
                table_data.append('')

            if len(driver.find_elements_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[2]/div')) :
                summary = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[1]/span').text
                print(summary)
                table_data.append(summary)
            else:
                table_data.append('')  

            if len(driver.find_elements_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[2]/div')) :
                keywords = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[2]/div').text
                print(keywords)
                table_data.append(keywords)
            else:
                table_data.append('')  
            k = random.random()%3 + 1
            time.sleep(k)
            if len(driver.find_elements_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[3]/span')) :
                doi = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[3]/span').text
                print(doi)
                table_data.append(doi)
            else:
                table_data.append('')   

            if len(driver.find_elements_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[5]')) :
                classification = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[5]').text
                print(classification)
                table_data.append(classification)
            else:
                table_data.append('')      

            k = random.random()%3 + 2
            time.sleep(k)
            if len(driver.find_elements_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[6]/div/span')) :
                author = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[6]/div/span').text
                print(author)
                table_data.append(author)
            else:
                table_data.append('')

            if len(driver.find_elements_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[7]/div')) :
                institution = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[7]/div')
                print(institution)
                table_data.append(institution)
            else:
                table_data.append('')
            k = random.random()%5 + 2
            time.sleep(k)
            if len(driver.find_elements_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[8]/span')) :
                journal = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[8]/span').text
                print(journal)
                table_data.append(journal)
            else:
                table_data.append('')

            if len(driver.find_elements_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[9]/span')) :
                time_ = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[9]/span').text
                print(time_)
                table_data.append(time_)
            else:
                table_data.append('')

            if len(driver.find_elements_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[10]/span')) :
                issue = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[10]/span').text
                print(issue)
                table_data.append(issue)
            else:
                table_data.append('')

            if len(driver.find_elements_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[11]/span')) :
                main_language = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[11]/span').text
                print(main_language)
                table_data.append(main_language)
            else:
                table_data.append('')

            currentPageUrl = str(driver.current_url)
            print(currentPageUrl)
            table_data.append(currentPageUrl.replace("\n", ""))

            writer.writerow(table_data)
            k = random.random()%8 + 1
            time.sleep(k)
            num=driver.window_handles
            print("all handles before switch: ",num)
            driver.close()
            driver.switch_to_window(num[0])
            num=driver.window_handles
            print("all handles after switch: ",num)
            time.sleep(random.random()%15 + 5)
            i = i + 1
            if i< 11 and len(driver.find_elements_by_xpath('//*[@id="result-content"]/div['+str(i)+']/h2/a')) :
                nextpaper = driver.find_element_by_xpath('//*[@id="result-content"]/div['+str(i)+']/h2/a').click() 
                time.sleep(random.random()%5 + 2)
                num=driver.window_handles
                print(num)
                driver.switch_to_window(num[1])
        i = 1
        num = driver.window_handles
        print('beforenextpage',num)
        driver.find_element_by_class_name('nextPage').click()
        num = driver.window_handles
        print('afternextpage',num)
        j = j + 1
        time.sleep(random.random()%30 + 80)
        if i< 11 and len(driver.find_elements_by_xpath('//*[@id="result-content"]/div['+str(i)+']/h2/a')) :
            nextpaper = driver.find_element_by_xpath('//*[@id="result-content"]/div['+str(i)+']/h2/a').click() 
            time.sleep(random.random()%10 + 2)
            num=driver.window_handles
            print(num)
            driver.switch_to_window(num[1])
            k = random.random()%6 + 1
            time.sleep(k)        
    # 遍历所有页（除最后一页，因为最后一页没有按20条数据来分页），抓取所有数据
    # for page in range(1, page_num - start_page + 1):
    #     for row in range(2, 22):
    #         getTableData(row, table_data)
        
    #     driver.find_element_by_xpath('//*[@id="xiayiye"]/a/img').click()

    # 获取最后一页的数据
    # for row in range(2, 25):
    #     getTableData(row, table_data)

# # table_heads = driver.find_element_by_xpath('//*[@id="bodyTable"]/tbody/tr[1]')
# time.sleep(5)
# driver.find_element_by_id("su").click()

# close window

