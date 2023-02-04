from requests_oauthlib import OAuth1

url_ch = 'http://localhost:8888/chase/wp-json/wc/v3/customers'
update_url_Ch = 'http://localhost:8888/chase/wp-json/wc/v3/customers/5'
delete_url_ch = 'http://localhost:8888/chase/wp-json/wc/v3/customers/8?force=true'
auth_ch = OAuth1('ck_bbd634babc20ad5fdd5c0fa1a97d3b63c03e5f99', 'cs_8aecb177625f82f6bdde217c046afd133862680b')

url_sp = 'http://localhost:8888/Spectrum/wp-json/wc/v3/customers'
update_url_sp = 'http://localhost:8888/Spectrum/wp-json/wc/v3/customers/14'
delete_url_sp = 'http://localhost:8888/Spectrum/wp-json/wc/v3/customers/8?force=true'
auth_sp = OAuth1 ('ck_72187cd74e99e9a07c4df2750725778f64bce95e', 'cs_7ce52b03d229210013cf96e1efb83273a07d0b09')