'''
    Contains code to fetch data about countries
'''

import requests

REST_EU_URL = "http://restcountries.eu/rest/v1"

def REST_country_request(field='all', name=None, params=None):
    headers = {'User-Agent': 'Mozilla/5.0'}

    if not params:
        params = {}

    if field == 'all':
        return requests.get(REST_EU_URL + '/all')

    url = '%s/%s/%s'%(REST_EU_URL, field, name)
    print('Requesting URL: ' + url)
    response = requests.get(url, params=params, headers=headers)

    if not response.status_code == 200:
        raise Exception('Request failed with status code ' + str(response.status_code))

    return response


if __name__ == '__main__':

    my_resp = REST_country_request('currency', 'usd')
    if my_resp.status_code == 200:
        print(my_resp.json())
