#!/usr/bin/env python
# coding: utf-8

import requests

url = 'http://localhost:9696/predict'

customer_id = 'xyz-123'
# customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 19.7}
# customer = {"contract": "two_year", "tenure": 1, "monthlycharges": 10}
customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 10}

response = requests.post(url, json=customer).json()
print(response)

if response['churn'] == True:
    print('sending promo email to %s' % customer_id)
else:
    print('not sending promo email to %s' % customer_id)
