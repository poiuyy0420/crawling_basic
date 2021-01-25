from urllib import parse

parse.unquote('https://api.frientrip.com/Products/v5?filter=%7B%22perPage%22%3A20%2C%22currentPage%22%3A1%2C%22filtering%22%3A%7B%22order%22%3A%22popular%22%2C%22socialTypeIds%22%3A%5B%5D%2C%22isSuperhost%22%3Afalse%2C%22isInstant%22%3Afalse%2C%22searchString%22%3A%22%EC%9A%94%EB%A6%AC%22%7D%7D')

print(parse.unquote('https://api.frientrip.com/Products/v5?filter=%7B%22perPage%22%3A20%2C%22currentPage%22%3A1%2C%22filtering%22%3A%7B%22order%22%3A%22popular%22%2C%22socialTypeIds%22%3A%5B%5D%2C%22isSuperhost%22%3Afalse%2C%22isInstant%22%3Afalse%2C%22searchString%22%3A%22%EC%9A%94%EB%A6%AC%22%7D%7D'))