import requests
from requests_oauthlib import OAuth1
import random
import string
letters = string.digits
random = "".join(random.choice(letters)for i in range(3))

url = 'http://localhost:8888/Spectrum/wp-json/wc/v3/customers'
auth = OAuth1 ('ck_72187cd74e99e9a07c4df2750725778f64bce95e', 'cs_7ce52b03d229210013cf96e1efb83273a07d0b09')

json_data = {
  "email": "jon.dooe123"+random+"@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "username": "jon.dooe"+random,
  "password": "johne.doe"
}
res = requests.post(url,auth=auth,data=json_data)
print(res.json())
# print(res.status_code)
#assert res.status_code == 201, 'invalid status code'
#assert res.status_code!= 201, "invalid status code"
# print(res.status_code)

# print(json_data["first_name"])
# print(json_data["last_name"])