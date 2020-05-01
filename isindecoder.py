import requests
from Config import figi_api_key


def decode_isin(isin):

    headers = {
        'Content-Type': 'application/json',
        'X-OPENFIGI-APIKEY': figi_api_key
    }
    data = '[{"idType":"ID_ISIN","idValue":"'+isin+'"}]'
    response = requests.post('https://api.openfigi.com/v2/mapping', headers=headers, data=data)
    json = response.json()
    try:
        return json[0]['data'][0]['name']
    except KeyError:
        raise KeyError
