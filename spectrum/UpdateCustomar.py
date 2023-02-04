import requests
from requests_oauthlib import OAuth1
import random
import string
letters = string.digits
random = "".join(random.choice(letters)for i in range(3))

url = 'http://localhost:8888/Spectrum/wp-json/wc/v3/customers/14'
auth = OAuth1 ('ck_72187cd74e99e9a07c4df2750725778f64bce95e', 'cs_7ce52b03d229210013cf96e1efb83273a07d0b09')

update_data = {
    "first_name": "masum"+random,
    "last_name": "tasmid"+random}

res = requests.put(url, auth=auth, json=update_data)
print(res.status_code)
assert res.status_code == 200, "invalid status code"
#assert res.status_code!= 200, "invalid status code"
# print(res.status_code)

