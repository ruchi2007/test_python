import random
import string
letters = string.digits
random = "".join(random.choice(letters)for i in range(3))

json_data_ch = {
  "email": "bo.doee123"+random+"@example.com",
  "first_name": "John",
  "last_name": "Doee",
  "username": "bo.doee"+random,
  "password": "johne.doe"
}


update_data_ch = {
  "first_name": "adil"+random,
    "last_name": "tasmid"+random}


json_data_sp = {
  "email": "jon.dooe123"+random+"@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "username": "jon.dooe"+random,
  "password": "johne.doe"
}

update_data_sp = {
    "first_name": "takiaa",
    "last_name": "tasmide"}