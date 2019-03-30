import requests


def test():
    response = requests.get("http://www.baidu.com")
    print(response.status_code)
    print(response.request.url)
    print(response.request.headers)


test()
