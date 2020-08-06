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
    final_movie_list = []
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
        final_movie_list.append(movie_data)
        
# print(final_movie_list)




for i in range(len(final_movie_list)):
    movie_code = final_movie_list[i]['code']
    # print(movie_code)
    print('\n', '{0}번째 영화: {1}'.format (i+1, final_movie_list[i]['title']) )

    headers = {
        'authority': 'movie.naver.com',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'iframe',
        'referer': f'https://movie.naver.com/movie/bi/mi/point.nhn?code={movie_code}',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'NNB=C7QVSVSIZEHV6; NRTK=ag#all_gr#0_ma#-2_si#-2_en#-2_sp#-2; nx_ssl=2; MM_NEW=1; NFS=2; MM_NOW_COACH=1; NM_THUMB_PROMOTION_BLOCK=Y; page_uid=UyWxvlprvN8ssdL02asssssst1G-184181; JSESSIONID=6716FDB46597DBEE06A9F8C3D35D13C3; csrf_token=d660793a-16e4-46cb-916b-4b0c3abfdce7',
    }

    params = (
        ('code', f'{movie_code}'),
        ('type', 'after'),
        ('isActualPointWriteExecute', 'false'),
        ('isMileageSubscriptionAlready', 'false'),
        ('isMileageSubscriptionReject', 'false'),
    )

    response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', headers=headers, params=params)
    soup_list= []
    soup= BeautifulSoup(response.text, 'html.parser')
    soup_list.append(soup)

    for soup in soup_list:
        review_section = soup.select('body > div > div > div.score_result > ul > li ')

        count= 0
        for review in review_section:
            score = review.select_one('div.star_score > em').text

            if review.select_one(f'div.score_reple > p > span#_filtered_ment_{count} > span#_unfold_ment{count}') is None:
                content = review.select_one(f'div.score_reple > p > span#_filtered_ment_{count}').text.strip()
            elif review.select_one(f'div.score_reple > p > span#_filtered_ment_{count} > span#_unfold_ment{count}'): 
                content = review.select_one(f'div.score_reple > p > span#_filtered_ment_{count} > span#_unfold_ment{count} > a')['data-src']
            
            print(score, content)

            count += 1


     