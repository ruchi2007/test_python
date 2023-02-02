import requests
from requests_oauthlib import OAuth1

url = 'http://localhost:8888/Spectrum/wp-json/wc/v3/customers/8?force=true'
auth = OAuth1 ('ck_72187cd74e99e9a07c4df2750725778f64bce95e', 'cs_7ce52b03d229210013cf96e1efb83273a07d0b09')

res = requests.delete(url, auth = auth)
print(res.status_code)
assert res.status_code == 200, "invalid status code"
assert res.status_code != 200, "invalid status code"
print(res.status_code)
