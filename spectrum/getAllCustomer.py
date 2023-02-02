import requests
from requests_oauthlib import OAuth1

url = 'http://localhost:8888/Spectrum/wp-json/wc/v3/customers'
auth = OAuth1 ('ck_72187cd74e99e9a07c4df2750725778f64bce95e', 'cs_7ce52b03d229210013cf96e1efb83273a07d0b09')

res = requests.get(url, auth=auth)

print(res.json())
# assert res.status_code == 200, "invalid status code"
# print(res.status_code)

# content_type = res.headers["Content-type"]
# assert content_type == "application/json; charset=UTF-8", "invalid content type"
# print(content_type)
# customer_list = res.json()
# assert customer_list != [],"no existing customer"

print(res.json()[3]['id'])
print(res.json()[0]['first_name'])
print(res.json()[1]['last_name'])
print(res.json()[2]['username'])
print(res.json()[3]['email'])

for a in res.json():
    # print(a["id"])
    # print(a['first_name'])
    print(a['username'])
