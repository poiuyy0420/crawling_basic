# Section05-1
# BeautifulSoup
# BeautifulSoup 사용 스크랩핑(1) - 기본 사용법

from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <h1>this is h1 area</h1>
        <h2>this is h2 area</h2>
        <p class="title"><b>The Dormouse's story</b></p>
        <p class="story">Once upon a time there were three little sisters.
            <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            <a data-io="link3" href="http://example.com/tillie" class="sister" id="link3">Title</a>
        </p>
        <p class="story">
            story...
        </p>
    </body>
</html>
"""

# 예제1(BeautifulSoup 기초)
# bs4 초기화
# soup = BeautifulSoup(request.get('http').text)
soup = BeautifulSoup(html, 'html.parser')

# 타입 확인
print('soup', type(soup))
# print('prettify', soup.prettify())

# h1 태그 접근
h1 = soup.html.body.h1
print('h1', h1)

# p 태그 접근
p1 = soup.html.body.p
print('p1', p1)

# 다음 태그
p2 = p1.next_sibling.next_sibling
print('p2', p2)

# 텍스트 출력1
print('h1 >> ', h1.string)

# 텍스트 출력2
print('p1 >> ', p1.string)

# 함수 확인
# print(dir(p2))

# 다음 엘리먼트 확인
# print(list(p2.next_element))
print(p2.next_element)


# 반복 출력 확인
for v in p2.next_element:
    pass
    # print(v)



# 예제2(Find, Find_all)
# bs4 초기화

soup2 = BeautifulSoup(html, 'html.parser')

# a 태그 모두 선택
# link1 = soup.find_all('a', limit=2)
link1 = soup2.find_all('a')

# 타입 확인
# print(type(link1))

# 리스트 요소 확인
print('links', link1)

# 중요
link2 = soup2.find_all("a", class_='sister') # id="link2", string="title", string=["Elsie"]
# link2 = soup2.find_all("a", string=["Elsie"])
# link2 = soup2.find_all("a", string=["Elsie","Title"])
print('link2 >>>', link2)

for t in link2:
    print(t)


# 처음 발견한 a 태그 선택
link3 = soup2.find("a")

print()
print(link3)
print(link3.string)
print(link3.text)

# 다중 조건(중요)
link4 = soup2.find("a", {"class": "sister", "data-io": "link3"})

print()
print(link4)
print(link4.string)
print(link4.text)


# CSS 선택자 : select, select_one
# 태그로 접근 : find, find_all
# 예제3(select, select_one)

# 태그 + 클래스 + 자식선택자

link5 = soup2.select_one('p.title > b')
print()
print(link5)
print(link5.text)
print(link5.string)

link6 = soup2.select_one("a#link1")
print()
print(link6)
print(link6.text)
print(link6.string)

link7 = soup2.select_one("a[data-io='link3']")
print()
print(link7)
print(link7.text)
print(link7.string)

# . : 클래스, # : id
# 선택자에 맞는 전체 선택
link8 = soup2.select('p.story > a')
print()
print(link8)
# print(link8.string)

# for t in link8:
#     print(t)


link9 = soup2.select('p.story > a:nth-of-type(2)')
print()
print(link9)


link10 = soup2.select('p.story')
print()
print(link10)

# for t in soup2.select('p.story'):
for t in link10:
    temp = t.find_all("a")
    print(temp)

    if temp:
        for v in temp:
            print('>>>>>', v)
            print('>>>>>', v.string)
    else:
        print('-----', t)
        print('-----', t.string)
