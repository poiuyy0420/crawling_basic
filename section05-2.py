# Section05-2
# BeautifulSoup
# BeautifulSoup 사용 스크랩핑(2) - 이미지 다운로드

import os
import urllib.parse as rep
import urllib.request as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# Header 정보 초기화
opener = req.build_opener()
# User-Agent 정보
opener.addheaders = [('User-agent', UserAgent().chrome)]
# Header 정보 삽입
req.install_opener(opener)

# 네이버 이미지 기본 URL(크롬 개발자 도구)
# base = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
# base = 'https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q='
base = 'https://www.naver.com'

# 검색어
# quote = rep.quote_plus('호랑이')
# quote = rep.quote_plus('요리')

# URL 완성
# url = base + quote
url = base

# 요청 URL 확인
print('Request URL : {}'.format(url))

# Request
res = req.urlopen(url)

# 이미지 저장 경로
savePath = "E:/py_workout/imagedown/" 
# C:\\imagedown\\

# 폴더 생성 예외처리(문제 발생 시 프로그램 종료)
try:
    # 기본 폴더가 있는지 체크
    if not (os.path.isdir(savePath)):
        # 없으면 폴더 생성
        os.makedirs(os.path.join(savePath))
except OSError as e:
    # 에러 내용
    print("folder creation failed.")
    print("folder name : {}".format(e.filename))

    # 런타임 에러
    raise RuntimeError("System Exit!")
else:
    # 폴더 생성이 되었거나, 존재할 경우
    print("folder is created!")

# bs4 초기화
soup = BeautifulSoup(res, "html.parser")
# print(soup.prettify())

# select 사용
# img_list = soup.select('div.photo_group._listGrid > div.photo_tile._grid > div.tile_item._item > div.photo_bx.api_ani_send._photoBox > div.thumb > a.link_thumb._imageBox._infoBox > img')
# img_list = soup.select('div#main_pack > section')
# img_list = soup.select('div#main_pack > section > div._contentRoot.image_wrap > div.photo_group._listGrid > div.photo_tile._grid > div:nth-child(2) > div > div.thumb > a > img')


# img_list = soup.select('div#NM_NEWSSTAND_DEFAULT_THUMB > div._NM_UI_PAGE_CONTAINER > div:nth-child(4)')
img_list = soup.select('img.news_logo')

# img_list2 = soup.find_all("a", class_="thumb _thumb")
# for v in img_list2:
#     img_t = v.find('img')
#     print(img_t.attrs['data-source'])

# print(img_list)

for i, img in enumerate(img_list, 1):
    # 속성 확인
    # print(img['src'], i)

    # 저장 파일명 몇 및 경로
    fullFileName = os.path.join(savePath, savePath + str(i) + '.png')

    # 파일명
    print(fullFileName) 

    # 다운로드 요청(URL, 다운로드 경로)
    req.urlretrieve(img['src'], fullFileName)

print("download seccede! ")