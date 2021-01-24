# Section02-2
# urlopen 함수 기초 사용법

import urllib.request as req
from urllib.error import URLError, HTTPError

# 다운로드 경로 및 파일명
path_list = ["E:/py_workout/test1.jpg", "E:/py_workout/index.html"]

# 다운로드 리소스 url
target_url = ["https://image.dongascience.com/Photo/2020/03/5bddba7b6574b95d37b6079c199d7101.jpg", "http://google.com"]

for i, url in enumerate(target_url):
    # 예외 처리
    try:
        # 웹 수신 정보 읽기
        response = req.urlopen(url)

        # 수신 내용
        contents = response.read()

        print("------------------------------------------------")

        # 상태 정보 중간 출력
        print('Header Info-{} : {}'.format(i, response.info()))
        print('HTTP Status Code: {}'.format(response.getcode()))
        print()
        print("------------------------------------------------")

        with open(path_list[i], 'wb') as c:
            c.write(contents)

    except HTTPError as e:
        print("Download failed .")
        print("HTTPError Code : ", e.code)
    except URLError as e:
        print("Download failed .")
        print("URL Error REason : ", e.reason)
    # 성공
    else:
        print()
        print("Download Succeed .")