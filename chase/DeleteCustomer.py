import requests
from requests_oauthlib import OAuth1

url = 'http://localhost:8888/chase/wp-json/wc/v3/customers/6?force=true'
auth = OAuth1('ck_bbd634babc20ad5fdd5c0fa1a97d3b63c03e5f99', 'cs_8aecb177625f82f6bdde217c046afd133862680b')

res = requests.delete(url, auth = auth)
print(res.status_code)
assert res.status_code == 400, "invalid status code"
assert res.status_code != 200, "invalid status code"
print(res.status_code)
