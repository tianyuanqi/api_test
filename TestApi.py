import requests


class TestApi:
    def test_get_news(self):
        url="http://v.juhe.cn/toutiao/index"
        params={
            "key":"4b989e8ee98b7869d5c189fba9072f30",
            "type":"junshi",
            "page":1,
            "page_size": 30,
            "in_filter": 1,
        }
        resp=requests.get(url=url,params=params)
        print(resp.json())

if __name__ == '__main__':
    TestApi().test_get_news()