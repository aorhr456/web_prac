import requests
from bs4 import BeautifulSoup
import csv

# responses = requests.get('http://www.naver.com/')

# print(responses.text)
soup_list = []
for i in range(1, 102, 10):
    url_fir = 'https://search.naver.com/search.naver?&where=news&query=%EA%B4%91%EC%A3%BC%20%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%20%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=148&start='
    url_mid = i
    url_end = '&refresh_start=0'
    url= url_fir + str(url_mid) + url_end

    response = requests.get(url)
    # print(response.text)

    
    soup= BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    soup_list.append(soup)


for soup in soup_list:
    news_section = soup.select('div[id=wrap] > div[id=container] > div[id=content] > div[id=main_pack] > div.news.mynews.section._prs_nws > ul.type01 > li')

# print(news_section)

    for new in news_section:
        a_tag =new.select_one('dl > dt > a')
    # print(a_tag)
        news_title= a_tag['title']
        news_link= a_tag['href']
        # print(news_title)
        # print(news_link, '\n')
        new_data = {
            'title': news_title,
            'link' : news_link
        }

        with open('new_list.csv', 'a', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'link']
            csvwriter = csv.DictWriter(csvfile, fieldnames)
            csvwriter.writerow(new_data)

