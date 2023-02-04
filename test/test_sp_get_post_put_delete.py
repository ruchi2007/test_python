#from pprint import pprint

import requests

from config import config as cf
from resource import testData as td


def test_get_all_customer():
    res = requests.get(cf.url_sp, auth=cf.auth_sp)
    print(res.json())


def test_post_creat_customer():
    res = requests.post(cf.url_sp, auth=cf.auth_sp, json=td.json_data_sp)
    print(res.json())


def test_put_all_customer():
    res = requests.put(cf.update_url_sp, auth=cf.auth_sp, json=td.update_data_sp)
    print(res.json())


def test_delete_customer():
    res = requests.delete(cf.delete_url_sp, auth=cf.auth_sp)
    print(res.json())
