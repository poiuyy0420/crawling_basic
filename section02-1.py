# Section02-1
# 파이썬 크롤링 기초
# urllib 사용법 및 기본 스크랩핑

import urllib.request as req

# 파일 URL
img_url = 'https://lh3.googleusercontent.com/proxy/eou9Sk38GMcbKXYhJQxKk03g7As2fNnlmSpxgCO-Mp6oPRGaq0j-OfIGUXqcByiP9BpljqRaKaMPSmapxdtT0KlRFVFe1f6jKIS25PEjNE6ZB-azSw'
html_url = 'http://google.com'

# 다운받을 경로
save_path1 = 'E:/py_workout/test1.jpg'
save_path2 = 'E:/py_workout/index.html'

# 예외처리
try:
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print('Download failed')
    print(e)
else:
    # Header 정보 출력
    print(header1)
    print(header2)


    # 다운로드 파일 정보
    print('Filename1 {}'.format(file1))
    print('Filename2 {}'.format(file2))
    print

    # 성공
    print('Download Succeed')