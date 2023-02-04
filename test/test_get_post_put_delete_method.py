import requests

from config import config as cf
from resource import testData as td


def test_get_method():
    res = requests.get(cf.url_ch, auth=cf.auth_ch)
    if res.status_code == 200:
        assert res.status_code == 200
        print(res.status_code)


    elif res.status_code != 200:
        assert res.status_code != 200, "invalid status code"
        print(res.status_code)


    if res.json() ==[]:
        assert res.json() == [], "empty list"
        print(res.json())


    elif res.json() != []:
        assert res.json() != []
        print(res.json()[0]["id"])

def test_post_method():
    res = requests.post(cf.url_ch, auth=cf.auth_ch, data=td.json_data_ch)

    if res.status_code == 201:
        assert res.status_code == 201
        print(res.status_code)

    elif res.status_code != 201:
        assert res.status_code != 201, "invalid status code"
        print(res.status_code)


def test_put_method():
    res = requests.put(cf.update_url_Ch, auth=cf.auth_ch, json=td.update_data_ch)

    if res.status_code == 200:
        assert res.status_code == 200,"valid status code"
        print(res.status_code)

    elif res.status_code != 200:
        assert res.status_code != 200,"invalid status code"
        print(res.status_code)


def test_delete_method():
    res = requests.delete(cf.delete_url_ch, auth=cf.auth_ch)

    if res.status_code == 200:
        assert res.status_code == 200, "valid status code"
        print(res.status_code)

    elif res.status_code != 200:
        assert res.status_code != 200, "invalid status code"
        print(res.status_code)