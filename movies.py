import requests
from bs4 import BeautifulSoup
import csv

url = 'https://movie.naver.com/movie/running/current.nhn#'
# for i in range()
# url_fri = 'https://movie.naver.com/movie/bi/mi/review.nhn?code='
# url_end = '188909'
# url = url_fri + url_end

response = requests.get(url)
soup_list=[]
soup = BeautifulSoup(response.text, 'html.parser')
soup_list.append(soup)
# print(soup_list)


for soup in soup_list:
    movie_section = soup.select('div[id=wrap] > div[id=container] > div[id=content] > div.article > div.obj_section > div.lst_wrap > ul.lst_detail_t1 > li')

# print(movie_section)

    for movie in movie_section:
        a_tag = movie.select_one('dl.lst_dsc > dt.tit > a')
        # print(a_tag)
        # title_list= []
        for tag in a_tag:
            # title_list.append(tag)
            tag = tag
        # movie_title= a_tag[tag]
        
        movie_code= a_tag['href']
        movie_code= movie_code[28:]

        movie_data = {
            'title' : tag,
            'code' : movie_code
        }
        print(movie_data)