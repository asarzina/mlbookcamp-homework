#!/usr/bin/env python
# coding: utf-8

import requests

url = 'http://localhost:9696/predict'

person_id = 'xyz-123'

person = {"education_num": 10, "age": 30, "education": "Masters"}
# person = {"education_num": 8, "age": 40, "education": "11th", "capital-gain": 10000}
# person = {"education_num": 14, "age": 35, "education": "Bachelors"}

response = requests.post(url, json=person).json()
print(response)

if response['income'] == True:
    print('Income is greater than 50K for' % person_id)
else:
    print('Income is less or equal than 50K for' % person_id)
